# Hinweise für Claude

Dieses Projekt ist die Website eines Auftraggebers ohne technische Vorkenntnisse.

1. Zuerst `website-projekt.md` lesen. Das ist die Projektakte: Zweck, Seiten,
   Entscheidungen des Auftraggebers, Hosting, zuletzt hochgeladener Stand, offene
   Punkte. Jede neue Entscheidung sofort dort eintragen, damit andere Sitzungen
   denselben Stand haben.
2. Für alle Arbeiten an der Website den Skill `website-bauen` verwenden. Vor dem
   Veröffentlichen und nach größeren Änderungen den Skill `website-sicherheitscheck`.
3. Hochgeladen wird nur der Inhalt von `public/`. Zugangsdaten
   (`public/api/config.php`, `.env`) gehören nie ins Projekt und nie in den Chat.
4. Vorschau am eigenen Computer: Der Auftraggeber arbeitet am Mac mit dem
   Terminal. Er lädt den Stand des Zweigs als ZIP von GitHub und startet im
   Projektordner `npm start` (dann im Browser http://127.0.0.1:4173).
   `package.json` hat keine Pakete und startet `werkzeuge/vorschau.js`, eine
   Kopie des Vorschauprogramms aus dem Skill website-bauen. Diese Dateien nicht
   entfernen; sie werden nicht hochgeladen.
