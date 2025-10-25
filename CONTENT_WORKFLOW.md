# Content Workflow - MD → HTML

**Version:** 1.0
**Erstellt:** 2025-10-25

---

## Übersicht

Dieses Dokument beschreibt den Workflow für die Content-Verwaltung des eLearning TAP Projekts. Der Content wird zentral in der Datei [content.md](content.md) verwaltet und kann von dort in [eLearning.html](eLearning.html) übertragen werden.

---

## Workflow-Diagramm

```
┌─────────────────┐
│   content.md    │  ← Manuelle Bearbeitung durch Sie
│  (Content-      │
│   Quelle)       │
└────────┬────────┘
         │
         │ Änderungen vorgenommen
         ▼
┌─────────────────┐
│   Claude Code   │  ← Konvertierung MD → HTML
│  (Automatische  │
│   Übertragung)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ eLearning.html  │  ← Aktualisierte Schulungsunterlage
│  (Output)       │
└─────────────────┘
```

---

## 1. Content bearbeiten (Manuell)

### Datei öffnen

Öffnen Sie [content.md](content.md) in einem Texteditor Ihrer Wahl (VS Code, Sublime Text, etc.)

### Inhalte anpassen

Bearbeiten Sie die Markdown-Datei nach Belieben. Sie können:

**Texte ändern:**
```markdown
### Was ist der LKAAT?

LKAAT steht für "Leistungskatalog ambulante Arzttarife"...
```

**INFO-Boxen hinzufügen:**
```markdown
**INFO-BOX: Titel der Box**

Inhalt der Info-Box...
- Listenpunkt 1
- Listenpunkt 2
```

**INFO-BOX Varianten:**
- `**INFO-BOX:**` → Normale blaue Info-Box
- `**INFO-BOX WARNUNG:**` → Gelbe Warn-Box
- `**INFO-BOX SUCCESS:**` → Grüne Erfolgs-Box

**Akkordeons erstellen:**
```markdown
**ACCORDION:**

**Titel des ersten Eintrags**

Inhalt des ersten Akkordeon-Eintrags...

**Titel des zweiten Eintrags**

Inhalt des zweiten Akkordeon-Eintrags...
```

**Tabellen einfügen:**
```markdown
**TABELLE: Titel der Tabelle**

| Spalte 1 | Spalte 2 | Spalte 3 |
|----------|----------|----------|
| Wert 1   | Wert 2   | Wert 3   |
| Wert 4   | Wert 5   | Wert 6   |
```

**Quiz-Fragen anpassen:**
```markdown
### QUIZ

**Frage 1: Was ist LKAAT?**
- a) Falsche Antwort
- b) Korrekte Antwort ✓
- c) Falsche Antwort
- d) Falsche Antwort
```

**Wichtig:** Die korrekte Antwort wird mit ✓ markiert!

---

## 2. Änderungen an Claude übergeben

### Einfache Änderung (ein Kapitel)

Wenn Sie nur ein Kapitel geändert haben:

```
@content.md wurde aktualisiert.
Bitte übertrage die Änderungen von Kapitel 3 in @eLearning.html
```

### Mehrere Kapitel geändert

Wenn Sie mehrere Kapitel geändert haben:

```
@content.md wurde aktualisiert.
Bitte übertrage die Änderungen folgender Kapitel in @eLearning.html:
- Kapitel 2
- Kapitel 5
- Kapitel 7
```

### Vollständige Aktualisierung

Wenn Sie viele Änderungen vorgenommen haben:

```
@content.md wurde vollständig überarbeitet.
Bitte synchronisiere alle Kapitel mit @eLearning.html
```

---

## 3. Claude's Konvertierungsprozess

Claude wird dann:

1. **content.md lesen** und die geänderten Kapitel identifizieren
2. **Markdown → HTML konvertieren:**
   - `**INFO-BOX:**` → `<div class="info-box">`
   - `**INFO-BOX WARNUNG:**` → `<div class="info-box warning">`
   - `**ACCORDION:**` → `<div class="accordion">`
   - Markdown-Tabellen → HTML `<table>`
   - Quiz-Fragen → HTML-Quiz-Struktur
3. **eLearning.html aktualisieren:**
   - Alte Kapitelinhalte ersetzen
   - Quiz-Antworten im JavaScript aktualisieren
   - Feedback-Texte anpassen

---

## 4. Struktur-Konventionen

### Kapitel-Struktur

Jedes Kapitel in [content.md](content.md) hat folgende Struktur:

```markdown
## KAPITEL X: Titel

### Abschnitt 1

Text...

**INFO-BOX: ...**

**ACCORDION:**

### Abschnitt 2

Text...

### QUIZ

**Frage 1: ...**
- a) ...
- b) ... ✓
```

### HTML-Mapping

| Markdown-Element | HTML-Output |
|------------------|-------------|
| `## KAPITEL X:` | `<div class="chapter" id="chapterY">` |
| `### Überschrift` | `<h3>Überschrift</h3>` |
| `**fett**` | `<strong>fett</strong>` |
| `**INFO-BOX:**` | `<div class="info-box">` |
| `**INFO-BOX WARNUNG:**` | `<div class="info-box warning">` |
| `**INFO-BOX SUCCESS:**` | `<div class="info-box success">` |
| `**ACCORDION:**` | `<div class="accordion">` |
| Markdown-Tabelle | HTML `<table class="comparison-table">` |
| Quiz-Frage mit ✓ | Korrekte Antwort in JavaScript |

---

## 5. Beispiel-Workflow

### Szenario: Sie möchten Kapitel 4 erweitern

**Schritt 1:** Öffnen Sie [content.md](content.md)

**Schritt 2:** Navigieren Sie zu Kapitel 4:
```markdown
## KAPITEL 4: Diagnosen als ICD-10 Code
```

**Schritt 3:** Fügen Sie einen neuen Abschnitt hinzu:
```markdown
### Neue Best Practices

**INFO-BOX SUCCESS: Tipps für die Praxis**
- Tipp 1: Verwenden Sie immer die aktuelle ICD-10-GM Version
- Tipp 2: Dokumentieren Sie Diagnosen zeitnah
- Tipp 3: Bevorzugen Sie organspezifische Codes
```

**Schritt 4:** Speichern Sie [content.md](content.md)

**Schritt 5:** Sagen Sie Claude:
```
@content.md wurde aktualisiert.
Bitte übertrage die Änderungen von Kapitel 4 in @eLearning.html
```

**Schritt 6:** Claude wird:
- [content.md](content.md) lesen
- Kapitel 4 extrahieren
- HTML generieren:
  ```html
  <h3>Neue Best Practices</h3>
  <div class="info-box success">
      <h4>✅ Tipps für die Praxis</h4>
      <ul class="list-styled">
          <li>Tipp 1: Verwenden Sie immer die aktuelle ICD-10-GM Version</li>
          <li>Tipp 2: Dokumentieren Sie Diagnosen zeitnah</li>
          <li>Tipp 3: Bevorzugen Sie organspezifische Codes</li>
      </ul>
  </div>
  ```
- Kapitel 4 in [eLearning.html](eLearning.html) aktualisieren

---

## 6. Quiz-Verwaltung

### Quiz-Fragen in content.md

```markdown
### QUIZ

**Frage 1: Was bedeutet ICD?**
- a) Internal Classification Diagnosis
- b) Internationale statistische Klassifikation der Krankheiten ✓
- c) International Code Database
- d) Interne Code Diagnose
```

### Was Claude macht

Claude wird:

1. **Richtige Antwort identifizieren** (durch ✓ markiert)
2. **Quiz-HTML generieren:**
   ```html
   <div class="quiz-question" data-chapter="4" data-question="1">
       <h4>Frage 1: Was bedeutet ICD?</h4>
       <div class="quiz-options">
           <label class="quiz-option">
               <input type="radio" name="q4_1" value="a">
               Internal Classification Diagnosis
           </label>
           <label class="quiz-option">
               <input type="radio" name="q4_1" value="b">
               Internationale statistische Klassifikation der Krankheiten
           </label>
           ...
       </div>
   </div>
   ```

3. **JavaScript answers-Objekt aktualisieren:**
   ```javascript
   const answers = {
       ...
       4: { 1: 'b', 2: 'c', 3: 'd', 4: 'b' },
       ...
   };
   ```

4. **Feedback-Texte generieren:**
   ```javascript
   4: {
       1: {
           correct: "Richtig! ICD steht für Internationale statistische Klassifikation der Krankheiten.",
           incorrect: "Falsch. ICD steht für Internationale statistische Klassifikation der Krankheiten."
       }
   }
   ```

---

## 7. Häufige Anwendungsfälle

### Neues Kapitel hinzufügen

1. In [content.md](content.md) neues Kapitel erstellen:
   ```markdown
   ## KAPITEL 10: Neues Thema

   ### Einführung

   Text...

   ### QUIZ

   **Frage 1: ...**
   - a) ...
   - b) ... ✓
   ```

2. Claude beauftragen:
   ```
   Neues Kapitel 10 wurde in @content.md erstellt.
   Bitte füge es in @eLearning.html ein und aktualisiere:
   - Navigation
   - Kapitelnummerierung
   - Quiz-System
   - GUIDELINES.md
   ```

### Bestehenden Inhalt ändern

1. In [content.md](content.md) Text anpassen
2. Claude beauftragen:
   ```
   Kapitel 3, Abschnitt "LKN-Nummern verstehen" wurde aktualisiert.
   Bitte übertrage in @eLearning.html
   ```

### Quiz-Fragen ändern

1. In [content.md](content.md) Quiz anpassen (✓ für richtige Antwort)
2. Claude beauftragen:
   ```
   Quiz-Fragen in Kapitel 5 wurden geändert.
   Bitte aktualisiere @eLearning.html (HTML + JavaScript)
   ```

---

## 8. Qualitätssicherung

### Nach der Aktualisierung testen

1. **eLearning.html im Browser öffnen:**
   ```bash
   open eLearning.html
   ```

2. **Prüfen Sie:**
   - ✅ Sind die Texte korrekt übertragen?
   - ✅ Werden Info-Boxen korrekt angezeigt?
   - ✅ Funktionieren Akkordeons (auf-/zuklappen)?
   - ✅ Sind Tabellen korrekt formatiert?
   - ✅ Funktioniert das Quiz?
   - ✅ Sind die richtigen Antworten im Quiz markiert?
   - ✅ Wird das korrekte Feedback angezeigt?

3. **Bei Problemen:**
   ```
   In Kapitel X wird die Info-Box nicht korrekt angezeigt.
   Bitte prüfe die Konvertierung in @eLearning.html
   ```

---

## 9. Best Practices

### Do's ✅

- ✅ Verwenden Sie konsistente Formatierung in [content.md](content.md)
- ✅ Markieren Sie korrekte Antworten immer mit ✓
- ✅ Verwenden Sie die vordefinierten INFO-BOX-Typen
- ✅ Testen Sie nach jeder Aktualisierung im Browser
- ✅ Nutzen Sie sprechende Überschriften
- ✅ Halten Sie die Kapitelstruktur konsistent

### Don'ts ❌

- ❌ Nicht direkt in [eLearning.html](eLearning.html) bearbeiten (außer Design/CSS)
- ❌ Keine HTML-Tags in [content.md](content.md) verwenden (außer explizit gefordert)
- ❌ Quiz-Antworten nicht ohne ✓-Markierung
- ❌ Keine inkonsistenten INFO-BOX-Bezeichnungen
- ❌ Nicht mehrere ✓ pro Frage (nur eine korrekte Antwort!)

---

## 10. Troubleshooting

### Problem: Info-Box wird nicht angezeigt

**Ursache:** Falsche Markdown-Syntax

**Lösung:**
```markdown
# Falsch:
INFO-BOX: Titel

# Richtig:
**INFO-BOX: Titel**
```

### Problem: Akkordeon klappt nicht auf

**Ursache:** Fehlende ACCORDION-Kennzeichnung

**Lösung:**
```markdown
# Falsch:
**Titel 1**
Text...

# Richtig:
**ACCORDION:**

**Titel 1**
Text...
```

### Problem: Quiz zeigt falsche Antwort als korrekt

**Ursache:** ✓ fehlt oder an falscher Stelle

**Lösung:**
```markdown
# Falsch:
- a) Falsche Antwort
- b) Richtige Antwort

# Richtig:
- a) Falsche Antwort
- b) Richtige Antwort ✓
```

### Problem: Tabelle wird nicht formatiert

**Ursache:** Fehlender "TABELLE:"-Präfix

**Lösung:**
```markdown
# Falsch:
| Spalte 1 | Spalte 2 |
|----------|----------|

# Richtig:
**TABELLE: Titel**

| Spalte 1 | Spalte 2 |
|----------|----------|
```

---

## 11. Versionsverwaltung

### content.md Versionen

Bei größeren Änderungen empfiehlt sich ein Backup:

```bash
# Backup erstellen
cp content.md content_backup_2025-10-25.md

# Änderungen vornehmen
# ...

# Bei Bedarf wiederherstellen
cp content_backup_2025-10-25.md content.md
```

### Git Commits

Nach erfolgreicher Aktualisierung:

```bash
git add content.md eLearning.html
git commit -m "feat: Kapitel 4 erweitert mit Best Practices"
git push
```

---

## 12. Zusammenfassung

**Workflow in 3 Schritten:**

1. **Bearbeiten:** [content.md](content.md) in Texteditor öffnen und anpassen
2. **Übertragen:** Claude beauftragen, Änderungen nach [eLearning.html](eLearning.html) zu übertragen
3. **Testen:** [eLearning.html](eLearning.html) im Browser öffnen und Änderungen prüfen

**Vorteile dieses Workflows:**
- ✅ Einfache Content-Verwaltung in Markdown
- ✅ Keine HTML-Kenntnisse erforderlich
- ✅ Automatische Konvertierung durch Claude
- ✅ Konsistente Formatierung
- ✅ Schnelle Änderungen möglich

---

**Bei Fragen oder Problemen:** Fragen Sie Claude!

```
Ich habe eine Frage zum Content-Workflow...
```

---

**Version:** 1.0
**Letzte Aktualisierung:** 2025-10-25
