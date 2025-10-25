# Copilot Instructions for eLearning_TAP

## Projektüberblick
- Interaktive Single-File-HTML-Schulungsunterlage für das ambulante Tarifsystem der Schweiz (TARDOC, LKAAT, Ambulante Pauschalen, ICD-10).
- Ziel: Wissensvermittlung, Quiz, Navigation und Design in einer Datei, keine externen Abhängigkeiten.

## Architektur & Struktur
- Hauptdatei: `ambulantes-tarifsystem-schulung-komplett.html` (enthält HTML, CSS, JS, Base64-Bilder)
- Alle Kapitel als `<div class="chapter" id="chapterX">` im Content-Bereich, Navigation über Buttons und JS-Funktion `showChapter()`
- Interaktive Komponenten: Quiz (mit JS-Auswertung), Akkordeon, Info-Boxen, Fortschrittsbalken
- Design- und Inhaltsvorgaben: Siehe `GUIDELINES.md` (Schriftarten, Farben, Komponenten, Content-Templates)

## Entwicklungs- und Content-Workflow
- Neue Kapitel: Button in `<nav>`, neues `<div class="chapter" ...>`, Quiz-Logik in JS ergänzen, `totalChapters` anpassen
- Quiz: Fragen als `.quiz-question`, Antworten/Feedback in den JS-Objekten `answers` und `feedbackTexts` pflegen
- Designänderungen: Direkt im `<style>`-Block der HTML-Datei, Vorgaben in `GUIDELINES.md` beachten
- Testing: Checkliste in `GUIDELINES.md` nutzen, HTML lokal im Browser oder via `python3 -m http.server` testen
- Deployment: Datei umbenennen/kopieren, auf Intranet/Webserver hochladen

## Konventionen & Besonderheiten
- Keine externen Libraries, keine Webfonts, alles embedded
- Commit-Typen: `feat:`, `fix:`, `content:`, `style:`, `refactor:`, `docs:`
- Responsive Design, mobile-friendly
- Alle relevanten Vorgaben und Beispiele: `GUIDELINES.md`

## Beispiele & Referenzen
- Siehe `GUIDELINES.md` für Templates (Kapitel, Quiz, Info-Boxen, Akkordeon, Tabellen)
- Siehe `README.md` für Projektstruktur und Quick Start

## Wichtige Dateien
- `ambulantes-tarifsystem-schulung-komplett.html` (zentral)
- `GUIDELINES.md` (alle Vorgaben)
- `README.md` (Schnellstart, Übersicht)

> Bei Unsicherheiten immer zuerst `GUIDELINES.md` konsultieren!