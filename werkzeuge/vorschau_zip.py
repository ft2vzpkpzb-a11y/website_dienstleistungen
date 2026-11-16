#!/usr/bin/env python3
"""Baut eine Vorschau der Website, die sich am eigenen Computer per Doppelklick öffnen lässt.

Aufruf (im Projektordner):  python3 werkzeuge/vorschau_zip.py

Ergebnis: vorschau/website-vorschau.zip (wird nie hochgeladen und nicht gespeichert).

Warum es das braucht: Die echten Seiten verweisen so aufeinander, wie es der
Server erwartet (/kontakt statt kontakt.html, /assets/… vom Hauptordner aus).
Öffnet man eine Seite direkt von der Festplatte, findet der Browser deshalb
weder Stil noch Schriften noch die anderen Seiten. Dieses Programm legt eine
Kopie an, in der alle Verweise auf Dateien nebeneinander zeigen (kontakt.html,
assets/…). An den echten Dateien in public/ ändert es nichts.

In der Kopie versendet das Kontaktformular nichts, sondern sagt, dass es eine
Vorschau ist. Formular-Skript (PHP), .htaccess, robots.txt und sitemap.xml
gehören nicht in die Vorschau.
"""
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

PROJEKT = Path(__file__).resolve().parent.parent
QUELLE = PROJEKT / 'public'
ZIEL = PROJEKT / 'vorschau' / 'website-vorschau.zip'
WEGLASSEN = {'api', '.htaccess', '.user.ini', 'robots.txt', 'sitemap.xml', '404.html'}

ANLEITUNG = """So öffnen Sie die Vorschau der Website
==========================================

1. Die ZIP-Datei entpacken: am Mac doppelt anklicken, unter Windows mit
   der rechten Maustaste „Alle extrahieren …“ wählen, dann „Extrahieren“.
2. Im entpackten Ordner die Datei „Website ansehen“ doppelt anklicken.
   Die Website öffnet sich im Browser (am besten Safari, Chrome oder Edge).
3. Von dort aus lässt sich durch alle Seiten klicken, auch am Handy-Format
   (Browserfenster schmal ziehen).

Gut zu wissen:
- Das ist nur eine Vorschau auf Ihrem Computer. Niemand sonst sieht sie.
- Das Kontaktformular versendet in der Vorschau nichts.
- Alles in doppelten eckigen Klammern [[…]] ist noch Platzhalter.
"""

WEITERLEITUNG = """<!doctype html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="0; url=website/index.html">
<title>Website ansehen</title>
</head>
<body>
<p><a href="website/index.html">Zur Vorschau der Website</a></p>
</body>
</html>
"""

# Wird in der Kopie von main.js vor den Versand gesetzt: In der Vorschau kein Versand.
FORMULAR_HINWEIS = (
    "if (location.protocol === 'file:') {\n"
    "        submitBtn.disabled = false;\n"
    "        submitBtn.textContent = 'Anfrage senden';\n"
    "        setStatus('Vorschau: Hier wird nichts versendet. Das Formular funktioniert erst auf dem Server.', 'success');\n"
    "        return;\n"
    "      }\n\n"
    "      post('/api/contact')"
)


def seiten_namen(ordner):
    return {p.stem for p in ordner.glob('*.html')}


def verweis_umbauen(wert, seiten):
    """/kontakt#x -> kontakt.html#x, / -> index.html, /assets/… -> assets/…"""
    if not wert.startswith('/') or wert.startswith('//'):
        return wert
    pfad, trenner, rest = re.match(r'([^?#]*)([?#]?)(.*)', wert).groups()
    if pfad.startswith('/assets/'):
        return pfad[1:]                      # Versionsangabe ?v=… weglassen
    name = pfad.strip('/')
    if name == '':
        name = 'index'
    if name in seiten:
        return name + '.html' + (trenner + rest if trenner == '#' else '')
    return wert


def main():
    if not QUELLE.is_dir():
        sys.exit(f'Ordner fehlt: {QUELLE}')
    seiten = seiten_namen(QUELLE)
    with tempfile.TemporaryDirectory() as tmp:
        basis = Path(tmp) / 'website-vorschau'
        web = basis / 'website'
        shutil.copytree(QUELLE, web, ignore=lambda d, namen: [n for n in namen if Path(d) == QUELLE and n in WEGLASSEN])

        for html in web.glob('*.html'):
            text = html.read_text(encoding='utf-8')
            text = re.sub(r'\b(href|src)="([^"]*)"', lambda m: f'{m.group(1)}="{verweis_umbauen(m.group(2), seiten)}"', text)
            text = re.sub(r"url\('(/assets/[^']*)'\)", lambda m: f"url('{m.group(1)[1:]}')", text)
            html.write_text(text, encoding='utf-8')

        for css in (web / 'assets' / 'css').glob('*.css'):
            text = css.read_text(encoding='utf-8')
            text = re.sub(r'url\((["\']?)/assets/', r'url(\1../', text)
            css.write_text(text, encoding='utf-8')

        js = web / 'assets' / 'js' / 'main.js'
        text = js.read_text(encoding='utf-8')
        if text.count("post('/api/contact')") != 1:
            sys.exit('main.js: Stelle für den Vorschau-Hinweis nicht gefunden (Formular geändert?)')
        js.write_text(text.replace("post('/api/contact')", FORMULAR_HINWEIS), encoding='utf-8')

        # Kontrolle: Es darf kein Verweis mehr vom Hauptordner aus übrig sein.
        reste = []
        for datei in list(web.glob('*.html')) + list((web / 'assets' / 'css').glob('*.css')):
            for m in re.finditer(r'(?:href|src)="(/[^/"][^"]*)"|url\(["\']?(/[^/][^)"\']*)', datei.read_text(encoding='utf-8')):
                reste.append(f'{datei.name}: {m.group(1) or m.group(2)}')
        if reste:
            sys.exit('Nicht umgebaute Verweise:\n  ' + '\n  '.join(reste))

        (basis / 'Website ansehen.html').write_text(WEITERLEITUNG, encoding='utf-8')
        (basis / 'Anleitung.txt').write_text(ANLEITUNG.replace('\n', '\r\n'), encoding='utf-8')

        ZIEL.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(ZIEL, 'w', zipfile.ZIP_DEFLATED) as z:
            for datei in sorted(basis.rglob('*')):
                if datei.is_file():
                    z.write(datei, datei.relative_to(basis.parent).as_posix())
        anzahl = sum(1 for p in basis.rglob('*') if p.is_file())
    print(f'Vorschau gebaut: {ZIEL} ({anzahl} Dateien, {ZIEL.stat().st_size // 1024} KB)')


if __name__ == '__main__':
    main()
