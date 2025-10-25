# Scripts für eLearning TAP

Dieser Ordner enthält alle Python-Skripte zur Generierung und Verwaltung der HTML-Dateien.

## Übersicht

### Hauptskript (empfohlen)

`**build_html.py**` - Vollständiger Markdown zu HTML Konverter

*   **Funktion:** Konvertiert `content/content.md` zu `eLearning.html`
*   **Status:** ✅ Produktiv, vollständig funktional
*   **Verwendung:**
*   **Features:**
    *   Parst alle 13 Kapitel (Vorwort + 10 Kapitel + Abschlusstest + FAQ)
    *   Konvertiert Markdown-Elemente zu HTML:
        *   INFO-Boxen (Standard, Warning, Success)
        *   Accordions mit Sub-Headings
        *   Tabellen
        *   Quiz-Sektionen
        *   Code-Beispiele
        *   Listen und Paragraphen
    *   Generiert vollständiges HTML mit CSS und JavaScript
    *   Ausgabe: `eLearning.html` (bereit für Deployment)

### Legacy-Skripte

`**convert_content_to_html.py**`

*   **Status:** ⚠️ Legacy, möglicherweise veraltet
*   **Hinweis:** Wurde durch `build_html.py` ersetzt

`**update_html.py**`

*   **Status:** ⚠️ Legacy, möglicherweise veraltet
*   **Hinweis:** Wurde durch `build_html.py` ersetzt

`**generate_html.py**`

*   **Status:** ⚠️ Unvollständig
*   **Hinweis:** Prototyp, wurde durch `build_html.py` ersetzt

## Empfohlener Workflow

### Content-Updates durchführen

**Content bearbeiten:**

**HTML neu generieren:**

**Ergebnis prüfen:**

**Änderungen committen:**

## Technische Details

### build\_html.py Funktionen

**Hauptfunktionen:**

*   `parse_content_md(content)` - Extrahiert Kapitel aus Markdown
*   `process_markdown_content(md_text, chapter_num)` - Konvertiert Markdown zu HTML
*   `process_accordion_content(content)` - Verarbeitet Accordion-Inhalte mit Sub-Headings
*   `process_list_content(content)` - Verarbeitet Listen in Info-Boxen
*   `process_table(lines)` - Konvertiert Markdown-Tabellen zu HTML
*   `convert_inline_md(text)` - Konvertiert Inline-Markdown (Bold, Italic)
*   `generate_html(chapters)` - Generiert vollständiges HTML-Dokument

**HTML-Template:**

*   Header mit CSS (alle Styles embedded)
*   Navigation mit allen 13 Kapiteln
*   Content-Bereich mit Chapter-Divs
*   Footer mit JavaScript (Quiz-Logik, Navigation, Accordions)

### Markdown-Konventionen

Die Skripte erwarten folgende Markdown-Struktur in `content/content.md`:

```
## KAPITEL 1: Titel

### Unterüberschrift

Normaler Text mit **Bold** und *Italic*.

**INFO-BOX: Titel**

*   Listenpunkt 1
*   Listenpunkt 2

**ACCORDION:**

**Accordion Header 1**

Inhalt des ersten Accordions.

**Accordion Header 2**

Inhalt des zweiten Accordions.

| Spalte 1 | Spalte 2 |
| --- | --- |
| Wert A | Wert B |

### QUIZ

**Frage 1: Fragetext?**

*   a) Antwort A
*   b) Antwort B
*   c) Antwort C ✓
*   d) Antwort D

---
```

**Wichtig:**

*   `✓` markiert die korrekte Antwort im Quiz
*   INFO-BOX Typen: `INFO-BOX:`, `INFO-BOX WARNUNG:`, `INFO-BOX SUCCESS:`
*   Tabellen verwenden Markdown-Syntax mit `|`
*   Accordions müssen nach `**ACCORDION:**` starten
*   Quiz-Sektionen beginnen mit `### QUIZ`

## Fehlerbehebung

### Problem: Skript findet content.md nicht

**Lösung:**

```
# Stelle sicher, dass du im Projekt-Root bist
cd /Users/sbeyeler/GIT/eLearning_TAP
python3 scripts/build_html.py
```

### Problem: Kapitel fehlen oder sind unvollständig

**Lösung:**

*   Überprüfe die Markdown-Syntax in `content/content.md`
*   Stelle sicher, dass alle Kapitel mit `## KAPITEL X:` oder `## Vorwort` beginnen
*   Prüfe die Konsolen-Ausgabe auf Fehler

### Problem: Quiz-Fragen werden nicht angezeigt

**Lösung:**

*   Quiz-Sektion muss mit `### QUIZ` beginnen
*   Fragen müssen mit `**Frage X: Text?**` formatiert sein
*   Antworten müssen mit `* a) ...` formatiert sein
*   Korrekte Antwort mit `✓` markieren

## Wartung

### Skript aktualisieren

Falls neue Markdown-Features hinzugefügt werden sollen:

1.  `scripts/build_html.py` bearbeiten
2.  Neue Parsing-Funktion hinzufügen
3.  In `process_markdown_content()` integrieren
4.  Testen mit `python3 scripts/build_html.py`
5.  Diese README aktualisieren

### Version History

*   **v1.0** (2025-10-25): Initial `build_html.py` mit vollständiger MD→HTML Konvertierung
*   Ersetzt alle Legacy-Skripte
*   Unterstützt alle 13 Kapitel
*   Vollständige Unterstützung für INFO-Boxen, Accordions, Tabellen, Quiz

---

**Zuletzt aktualisiert:** 2025-10-25  
**Maintainer:** Claude (via @DEVELOPMENT.md Workflow)

```
git add content/content.md eLearning.html
git commit -m "content: Beschreibung der Änderung"
git push
```

```
# HTML im Browser öffnen
open eLearning.html
```

```
# Von der Projekt-Root ausführen
python3 scripts/build_html.py
```

```
# Öffne content.md in deinem Editor
open content/content.md

# Bearbeite die Inhalte
# Speichern
```

```
python3 scripts/build_html.py
```