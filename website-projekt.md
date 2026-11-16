# Projektakte: [[NAME]] (Website für KI-Dienstleistungen)

Diese Datei ist das Gedächtnis des Projekts. Claude liest sie zu Beginn jeder
Sitzung und trägt Entscheidungen sofort ein, damit auch eine neue Sitzung weiß,
was gilt. Nichts aus dieser Datei wird hochgeladen. Keine Passwörter eintragen.

## Worum es geht

- Auftraggeber: (Name noch offen)
- Zweck der Website: Dienstleistungen anbieten. Kleinen und mittleren Unternehmen
  helfen, Arbeitsabläufe mit KI und KI-Tools zu verbessern und lästige
  Tätigkeiten abzunehmen, damit sie sich um Wichtigeres kümmern können.
- Wer soll angesprochen werden: kleine und mittlere Unternehmen (KMU), vor allem
  Inhaber, Geschäftsführung und Büroleitung ohne eigene Technikabteilung
- Adresse (Domain): noch offen
- Vorbild für den Stil: drweiser.at (ruhig, viel Luft, eine Akzentfarbe);
  gewählt: Dunkelblau mit Serifenschrift in den Überschriften
- Ansprache: Besucher mit „Sie“, das Unternehmen spricht als „wir“ (bestätigt)

## Seiten

| Seite | Adresse | Datei | Stand |
|---|---|---|---|
| Startseite | / | public/index.html | Entwurf |
| Leistungen | /leistungen | public/leistungen.html | Entwurf |
| Beispiele aus dem Alltag | /beispiele | public/beispiele.html | Entwurf |
| Ablauf und häufige Fragen | /ablauf | public/ablauf.html | Entwurf |
| Kontakt | /kontakt | public/kontakt.html | Entwurf, Kontaktdaten fehlen |
| Impressum | /impressum | public/impressum.html | Text fehlt |
| Datenschutzerklärung | /datenschutz | public/datenschutz.html | Text fehlt |

## Entscheidungen des Auftraggebers

Neueste zuerst, mit Datum. Wünsche möglichst wörtlich festhalten.

- 16.11.2026: Seite „Über uns“ vorbereiten, mit Platzhaltern für Foto, Werdegang
  und Beweggründe (Text und Foto kommen vom Auftraggeber).
- 16.11.2026: Ansprache bleibt „wir“ (bestätigt).
- 16.11.2026: Gestaltung Variante B „Blau, klassisch“: Dunkelblau als
  Akzentfarbe (#1E4B8F), kühler heller Hintergrund, Überschriften mit Serifen
  (Playfair Display) wie bei drweiser.at. Abgewählt: A Petrol modern,
  C Terrakotta warm (Dateien in vorschau/varianten, nicht im Projekt).
- 16.11.2026: Auftrag: „eine Website, die Dienstleistungen anbietet. Die
  Zielgruppe dieser Dienstleistungen sollen vor allem kleine und mittlere
  Unternehmen sein. Und primär soll es darum gehen, Unternehmen dabei zu helfen,
  mit KI, KI-Tools etc. pp. […] Arbeitsabläufe zu verbessern […] Tätigkeiten, die
  nervig sind, […] erleichtern“, damit sich das Unternehmen um wichtigere Dinge
  kümmern kann. Zu den Texten: „Lob dich da ruhig aus.“
- 16.11.2026: Name des Unternehmens noch offen, vorerst Platzhalter [[NAME]].
- 16.11.2026: Kein kostenloses Erstgespräch. Hauptknopf heißt „Anfrage senden“,
  ohne Zusage zu Kosten. Das Wort „kostenlos“ nirgends verwenden.
- 16.11.2026: Wörter mit „KI-“ (KI-Tools, KI-Assistent …) dürfen den Bindestrich
  behalten, sonst gilt: keine Striche im Text.
- 16.11.2026: Keine Google-Karte. Die Website lädt nichts von fremden Diensten.

## Texte und Bilder

- Texte: Formulierungen des Auftraggebers wörtlich übernehmen, nichts erfinden.
  Die Texte zu den Leistungen hat Claude auf Wunsch entworfen; sie beschreiben
  das Angebot und müssen vom Auftraggeber geprüft werden. Keine erfundenen
  Zahlen, Kundenstimmen, Referenzen oder Zusagen zu Preisen und Fristen.
- Erlaubte Wörter mit Bindestrich: E-Mail, KI-
  („KI-“ steht für alle Wörter, die mit KI beginnen, etwa KI-Tools oder KI-Assistent.)
- Fotos: bisher keine. Gestaltung mit Zeichen (Symbolen) statt Fotos. Fotos nur
  zuschneiden, nie bearbeiten. Herkunft und Rechte: noch keine Fotos.
- Bewertungen (nur die genannten, wörtlich): keine

## Dienste von Dritten

Jeder Dienst lädt erst nach Zustimmung und hat einen eigenen Schalter im Cookie-Fenster.

| Dienst | Zweck | Schalter im Cookie-Fenster | Absatz in der Datenschutzerklärung | Adressen in der .htaccess |
|---|---|---|---|---|
| (keiner) | | | | |

Google Maps wurde am 16.11.2026 abgewählt und aus Kontaktseite, Cookie-Fenster
und .htaccess entfernt.

## Hosting und Veröffentlichung

- Anbieter: noch offen
- Zielordner auf dem Server: httpdocs
- HTTPS im Kundenbereich eingeschaltet:
- PHP-Version auf dem Server:
- Zugangsdatei `config.php`: liegt nur auf dem Server im Ordner `api`
- Zuletzt hochgeladener Stand: noch nichts
- Frühere Adressen, die weitergeleitet werden: keine (neue Website)

## Offene Punkte

- [ ] Name des Unternehmens (Platzhalter [[NAME]])
- [x] Gestaltung gewählt: Variante B, Blau klassisch (16.11.2026)
- [ ] Kontaktdaten: Adresse, Telefon, E-Mail
- [ ] Domain und Hosting
- [ ] Texte der Leistungen prüfen und freigeben (von Claude entworfen)
- [x] Ansprache „wir“ bestätigt (16.11.2026)
- [ ] Texte für Impressum und Datenschutzerklärung vom Auftraggeber
- [ ] Cookie-Fenster: Die Website setzt keine Cookies und lädt nichts von
      Dritten. Klären, ob das Fenster bleiben soll und mit welchem Wortlaut.
- [ ] Seite „Über uns“: Foto, Werdegang und Beweggründe vom Auftraggeber
- [ ] Platzhalter `[[…]]` in allen Seiten ersetzen
