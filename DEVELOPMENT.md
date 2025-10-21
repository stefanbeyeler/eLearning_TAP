# Entwicklungsdokumentation - eLearning TAP

**Projekt:** eLearning für TARDOC und ambulante Pauschalen
**Version:** 1.0
**Letzte Aktualisierung:** 2025-10-21

---

## 📋 Inhaltsverzeichnis

1. [Projekt-Übersicht](#projekt-übersicht)
2. [Technologie-Stack](#technologie-stack)
3. [Projekt-Struktur](#projekt-struktur)
4. [Entwicklungsworkflow](#entwicklungsworkflow)
5. [Coding Standards](#coding-standards)
6. [Testing & Qualitätssicherung](#testing--qualitätssicherung)
7. [Deployment](#deployment)
8. [Wartung & Updates](#wartung--updates)
9. [Troubleshooting](#troubleshooting)

---

## 🎯 Projekt-Übersicht

### Zweck
Interaktive HTML-basierte Schulungsunterlagen für das ambulante Tarifsystem der Schweiz, die im Intranet bereitgestellt werden.

### Hauptkomponenten
- **LKAAT** - Leistungskatalog ambulanter Behandlungen und Abklärungen in Spitälern und Kliniken
- **TARDOC** - Einzelleistungstarif für ambulante ärztliche Behandlungen
- **Ambulante Pauschalen** - Pauschaliertes Abrechnungssystem

### Zielgruppe
Medizinisches Personal, Verwaltungsmitarbeitende, Codierer/innen in Schweizer Spitälern

---

## 🛠 Technologie-Stack

### Frontend
- **HTML5** - Strukturierung
- **CSS3** - Styling (embedded, keine externen Stylesheets)
- **JavaScript (ES6+)** - Interaktivität (embedded, keine externen Libraries)

### Besonderheiten
- **Single-File-Application**: Alle Ressourcen in einer HTML-Datei
- **Keine externen Abhängigkeiten**: Funktioniert offline und im Intranet
- **Keine Build-Tools erforderlich**: Direktes Arbeiten am HTML-File
- **Cross-Browser kompatibel**: Chrome, Firefox, Safari, Edge

### Entwicklungstools
- **Code-Editor**: VS Code, Sublime, Notepad++ (beliebig)
- **Browser-DevTools**: Für Debugging und Testing
- **Git**: Versionskontrolle

---

## 📁 Projekt-Struktur

```
eLearning_TAP/
├── README.md                                      # Projekt-Beschreibung
├── DEVELOPMENT.md                                 # Diese Datei
├── PROMPT-Schulungsunterlage-Vorgaben.md         # Inhaltliche Vorgaben für AI-Generierung
├── ambulantes-tarifsystem-schulung-komplett.html # Hauptdatei (Schulungsunterlage)
├── Vorgaben/                                      # Referenzmaterialien
│   ├── Anwenderschulung_Basis_H__final.pdf
│   ├── Schulungsunterlagen.pdf
│   ├── Webinar Schulungsfolien_09.09.2025.pdf
│   ├── preview.webp
│   └── preview (1).webp
└── .git/                                          # Git-Repository
```

### Datei-Verantwortlichkeiten

| Datei | Zweck | Bearbeitung |
|-------|-------|-------------|
| `ambulantes-tarifsystem-schulung-komplett.html` | Hauptschulungsunterlage | Bei Content-Updates |
| `PROMPT-Schulungsunterlage-Vorgaben.md` | Vorgaben für KI-generierte Inhalte | Bei strukturellen Änderungen |
| `DEVELOPMENT.md` | Entwicklungsdokumentation | Bei Prozess-Änderungen |
| `Vorgaben/*` | Referenzmaterialien | Read-only |

---

## 🔄 Entwicklungsworkflow

### 1. Neues Feature entwickeln

```bash
# Repository Status prüfen
git status

# Änderungen vornehmen
# -> HTML-Datei bearbeiten

# Lokales Testing
# -> HTML-Datei im Browser öffnen

# Änderungen committen
git add ambulantes-tarifsystem-schulung-komplett.html
git commit -m "feat: Beschreibung der Änderung"

# Optional: Push zu Remote
git push origin main
```

### 2. Neues Kapitel hinzufügen

**Schritt-für-Schritt:**

#### A. Planung
1. Lernziele definieren (siehe `PROMPT-Schulungsunterlage-Vorgaben.md`)
2. Inhaltsstruktur skizzieren
3. Quiz-Fragen vorbereiten (inkl. Antworten und Feedback)

#### B. HTML-Struktur erweitern

```html
<!-- 1. Navigation erweitern (im <nav>-Bereich) -->
<button class="nav-btn" onclick="showChapter(X)">
    Kapitel X: Titel
</button>

<!-- 2. Neues Kapitel erstellen (im <div class="content">-Bereich) -->
<div class="chapter" id="chapterX" style="display: none;">
    <h2>Kapitel X: Titel</h2>

    <!-- Inhalte hier einfügen -->
    <h3>Unterkapitel</h3>
    <p>Text...</p>

    <!-- Info-Box -->
    <div class="info-box">
        <h4>📋 Wichtig</h4>
        <ul class="list-styled">
            <li>Punkt 1</li>
            <li>Punkt 2</li>
        </ul>
    </div>

    <!-- Quiz-Sektion -->
    <div class="quiz-section">
        <h3>Verständnisfragen Kapitel X</h3>
        <!-- Quiz-Fragen hier -->
    </div>

    <!-- Navigation -->
    <div class="navigation-footer">
        <button class="nav-footer-btn" onclick="showChapter(X-1)">◄ Vorheriges</button>
        <button class="nav-footer-btn" onclick="showChapter(X+1)">Nächstes ►</button>
    </div>
</div>
```

#### C. JavaScript anpassen

```javascript
// 1. totalChapters erhöhen
const totalChapters = X+1; // Alte Zahl + 1

// 2. Quiz-Antworten hinzufügen
const answers = {
    // ... bestehende Einträge
    X: {
        1: 'a',  // Richtige Antwort für Frage 1
        2: 'c',  // Richtige Antwort für Frage 2
        // ...
    }
};

// 3. Feedback-Texte hinzufügen
const feedbackTexts = {
    // ... bestehende Einträge
    X: {
        1: {
            correct: "✓ Richtig! Erklärung...",
            incorrect: "✗ Falsch. Die richtige Antwort ist... weil..."
        },
        2: {
            correct: "✓ Richtig! ...",
            incorrect: "✗ Falsch. ..."
        }
    }
};
```

#### D. Testing
1. Alle Kapitel durchklicken (Navigation vor/zurück)
2. Quiz-Fragen durchgehen (alle Optionen testen)
3. Fortschrittsbalken prüfen
4. Responsive Design testen (Desktop, Tablet, Mobile)
5. Browser-Kompatibilität prüfen

### 3. Content-Updates

**Für bestehende Kapitel:**

1. Entsprechendes `<div class="chapter" id="chapterX">` lokalisieren
2. Inhalte anpassen (Text, Listen, Tabellen, etc.)
3. Bei Quiz-Änderungen: Auch JavaScript `answers` und `feedbackTexts` anpassen
4. Speichern und testen
5. Committen mit sinnvollem Commit-Message

**Commit-Message-Konventionen:**
```
feat: Neue Funktion
fix: Bugfix
content: Inhaltliche Änderung
style: Design-Anpassung
refactor: Code-Umstrukturierung
docs: Dokumentations-Update
```

### 4. Design-Anpassungen

**Farben ändern:**

Im `<style>`-Bereich die CSS-Variablen oder direkten Werte anpassen:

```css
/* Primärfarbe */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Info-Box Farben */
.info-box { border-left: 5px solid #667eea; }
.warning-box { border-left: 5px solid #ffc107; }
.success-box { border-left: 5px solid #28a745; }
```

**Typography ändern:**

```css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 16px;
    line-height: 1.6;
}
```

### 5. Akkordeon hinzufügen

```html
<div class="accordion">
    <div class="accordion-item">
        <div class="accordion-header" onclick="toggleAccordion(this)">
            <strong>📖 Titel des ausklappbaren Bereichs</strong>
            <span class="accordion-icon">▼</span>
        </div>
        <div class="accordion-content">
            <p>Versteckter Inhalt, der ausgeklappt werden kann.</p>
            <ul>
                <li>Punkt 1</li>
                <li>Punkt 2</li>
            </ul>
        </div>
    </div>
</div>
```

**Keine JavaScript-Änderung nötig** - Funktion `toggleAccordion()` ist bereits implementiert.

---

## 📐 Coding Standards

### HTML

**Struktur:**
- Semantisches HTML verwenden
- Klare Hierarchie mit H2 > H3 > H4
- IDs für Kapitel: `chapterX` (X = 0-basierter Index)
- Konsistente Klassennamen (siehe unten)

**Klassennamen:**

| Element | Klasse | Verwendung |
|---------|--------|------------|
| Container | `.container` | Haupt-Container |
| Kapitel | `.chapter` | Kapitel-Wrapper |
| Info-Box | `.info-box` | Standard-Infobox (blau) |
| Warning-Box | `.warning-box` | Warnungs-Box (gelb) |
| Success-Box | `.success-box` | Erfolgs-Box (grün) |
| Liste | `.list-styled` | Gestylte Liste |
| Tabelle | `.comparison-table` | Vergleichstabelle |
| Quiz-Sektion | `.quiz-section` | Quiz-Container |
| Quiz-Frage | `.quiz-question` | Einzelne Frage |
| Quiz-Option | `.quiz-option` | Radio-Button Option |
| Akkordeon | `.accordion` | Akkordeon-Container |
| Navigation | `.navigation-footer` | Kapitel-Navigation |

**Attribut-Standards:**
- `data-chapter`: Kapitelnummer (bei Quiz)
- `data-question`: Fragennummer (bei Quiz)
- `name`: Format `qX_Y` (Kapitel X, Frage Y)
- `onclick`: JavaScript-Funktionsaufruf

### CSS

**Organisation:**
```css
/* 1. Reset & Base Styles */
* { margin: 0; padding: 0; box-sizing: border-box; }

/* 2. Typography */
body { font-family: ...; }
h1, h2, h3 { ... }

/* 3. Layout */
.container { ... }
.header { ... }

/* 4. Components */
.info-box { ... }
.accordion { ... }

/* 5. Interactive Elements */
button { ... }
.quiz-option { ... }

/* 6. Responsive */
@media (max-width: 768px) { ... }
```

**Namenskonventionen:**
- Kebab-case: `.info-box`, `.quiz-section`
- BEM wenn komplex: `.accordion__header`, `.accordion__content`
- Keine IDs für Styling (nur für JavaScript-Referenzen)

**Wichtige Werte:**
- Border-radius: `10px` (Boxen), `15px` (Header)
- Box-shadow: `0 4px 6px rgba(0,0,0,0.1)`
- Transitions: `all 0.3s ease`
- Padding: `20px` (Standard), `15px` (Mobile)

### JavaScript

**Funktions-Organisation:**

```javascript
// 1. Globale Variablen
let currentChapter = 0;
const totalChapters = 8;

// 2. Initialisierung
document.addEventListener('DOMContentLoaded', function() {
    showChapter(0);
});

// 3. Navigation
function showChapter(index) { ... }
function updateProgress() { ... }

// 4. Interaktive Elemente
function toggleAccordion(header) { ... }

// 5. Quiz-Funktionen
function checkChapterQuiz(chapter) { ... }
function checkFinalQuiz() { ... }

// 6. Hilfsfunktionen
function scrollToTop() { ... }
function resetTraining() { ... }
```

**Best Practices:**
- Keine globalen Variablen außer `currentChapter`, `totalChapters`
- Konstanten in UPPER_CASE: `const PASSING_SCORE = 10;`
- Sprechende Funktionsnamen: `checkChapterQuiz()` statt `check()`
- Kommentare für komplexe Logik
- Error-Handling mit `try-catch` wo sinnvoll

**Quiz-Datenstruktur:**

```javascript
// Antworten: Verschachtelte Objekte
const answers = {
    1: { 1: 'a', 2: 'b' },  // Kapitel 1, Frage 1+2
    2: { 1: 'c', 2: 'd' },  // Kapitel 2, Frage 1+2
    // ...
    final: { 1: 'a', 2: 'b', /* ... */ 12: 'x' }
};

// Feedback: Dreifach verschachelt
const feedbackTexts = {
    1: {  // Kapitel 1
        1: {  // Frage 1
            correct: "Richtig weil...",
            incorrect: "Falsch weil..."
        }
    }
};
```

---

## 🧪 Testing & Qualitätssicherung

### Manuelle Test-Checkliste

**Navigation:**
- [ ] Alle Kapitel über Navigation-Buttons erreichbar
- [ ] "Vorheriges" Button funktioniert (außer bei Kapitel 1)
- [ ] "Nächstes" Button funktioniert (außer bei letztem Kapitel)
- [ ] Fortschrittsbalken aktualisiert sich korrekt
- [ ] Scroll-to-Top beim Kapitelwechsel

**Quiz:**
- [ ] Alle Radio-Buttons auswählbar
- [ ] "Antworten überprüfen" Button zeigt Feedback
- [ ] Richtiges Feedback bei korrekter Antwort
- [ ] Richtiges Feedback bei falscher Antwort
- [ ] Prozentuale Auswertung korrekt
- [ ] Abschlusstest: Bestanden/Nicht-bestanden korrekt

**Interaktive Elemente:**
- [ ] Akkordeons öffnen/schließen
- [ ] Akkordeon-Icon dreht sich
- [ ] Smooth Transitions

**Responsive Design:**
- [ ] Desktop (>1200px): Optimale Darstellung
- [ ] Tablet (768px-1199px): Lesbar, keine Überlappungen
- [ ] Mobile (375px-767px): Vertikale Navigation, lesbare Schrift

**Browser-Kompatibilität:**
- [ ] Chrome (neueste Version)
- [ ] Firefox (neueste Version)
- [ ] Safari (neueste Version)
- [ ] Edge (neueste Version)

**Performance:**
- [ ] Ladezeit < 2 Sekunden
- [ ] Keine Verzögerungen bei Kapitelwechsel
- [ ] Keine Konsolenfehler (F12 > Console)

### Validierung

**HTML-Validierung:**
```bash
# Online: https://validator.w3.org/
# Datei hochladen und prüfen
```

**CSS-Validierung:**
```bash
# Online: https://jigsaw.w3.org/css-validator/
# Embedded CSS extrahieren und prüfen
```

**Accessibility:**
- Keyboard-Navigation möglich (Tab-Navigation)
- Semantisches HTML verwendet
- Alt-Texte für Bilder (falls vorhanden)
- Ausreichende Farbkontraste

### Fehlersuche (Debugging)

**Browser DevTools verwenden:**

```javascript
// 1. Console öffnen (F12)
// 2. Fehler im "Console"-Tab suchen
// 3. Bei Quiz-Problemen: Antworten prüfen
console.log(answers[1]);  // Antworten Kapitel 1

// 4. Bei Navigation-Problemen: currentChapter prüfen
console.log(currentChapter);
```

**Häufige Fehlerquellen:**
- **Quiz zeigt immer "falsch"**: `answers` Objekt prüfen (Groß-/Kleinschreibung)
- **Kapitel wird nicht angezeigt**: `style="display: none;"` und `showChapter()` prüfen
- **Navigation funktioniert nicht**: `onclick` Attribut und Index prüfen
- **Akkordeon klappt nicht**: `toggleAccordion(this)` - `this` nicht vergessen

---

## 🚀 Deployment

### Intranet-Deployment

**Voraussetzungen:**
- Webserver (Apache, Nginx, IIS) ODER einfacher File-Share
- Keine serverseitige Technologie erforderlich (PHP, Node.js, etc.)

**Deployment-Schritte:**

1. **Datei vorbereiten**
   ```bash
   # Version in Dateinamen aufnehmen
   cp ambulantes-tarifsystem-schulung-komplett.html \
      ambulantes-tarifsystem-schulung-v1.0.html
   ```

2. **Upload zum Server**
   ```bash
   # Per FTP, SFTP oder File-Share
   # Zielort: z.B. /intranet/schulungen/
   ```

3. **Zugriff konfigurieren**
   ```
   URL: https://intranet.example.ch/schulungen/ambulantes-tarifsystem-schulung-v1.0.html
   ```

4. **Testing in Produktionsumgebung**
   - Von verschiedenen Arbeitsplätzen aufrufen
   - Mit verschiedenen Browsern testen
   - Netzwerk-Performance prüfen

### Alternativer Zugriff

**Option 1: Direkter File-Share**
```
\\server\schulungen\ambulantes-tarifsystem-schulung-v1.0.html
```
Mitarbeitende können Datei direkt öffnen (Doppelklick).

**Option 2: E-Mail-Versand**
Als Anhang an Teilnehmende senden (bei Dateigröße <2 MB).

**Option 3: USB/Offline**
Datei auf USB-Stick für Offline-Nutzung.

### Rollback-Strategie

Bei Problemen:
```bash
# 1. Alte Version wiederherstellen
git log                    # Commit-ID finden
git checkout <commit-id> ambulantes-tarifsystem-schulung-komplett.html

# 2. Neu deployen
# 3. Nutzer informieren
```

---

## 🔧 Wartung & Updates

### Versionierung

**Versionsschema:** `MAJOR.MINOR.PATCH`

- **MAJOR** (1.0.0): Neue Kapitel, große Umstrukturierungen
- **MINOR** (1.1.0): Neue Inhalte, erweiterte Quiz-Fragen
- **PATCH** (1.0.1): Bugfixes, Tippfehler, kleine Anpassungen

**Beispiele:**
```
1.0.0 → Initial Release
1.0.1 → Tippfehler in Kapitel 3 korrigiert
1.1.0 → Neues Praxisbeispiel in Kapitel 5 hinzugefügt
2.0.0 → Zwei neue Kapitel hinzugefügt
```

### Changelog pflegen

In HTML-Header kommentieren:
```html
<!--
CHANGELOG

Version 1.1.0 - 2025-11-15
- [Neu] Praktisches Beispiel in Kapitel 5 ergänzt
- [Geändert] Quiz Kapitel 3, Frage 2 präzisiert
- [Behoben] Akkordeon in Kapitel 4 öffnet korrekt

Version 1.0.1 - 2025-10-25
- [Behoben] Tippfehler in Kapitel 3, Absatz 2
- [Behoben] Quiz-Feedback Kapitel 7, Frage 1

Version 1.0.0 - 2025-10-21
- Initial Release
-->
```

### Update-Workflow

**Monatlicher Review:**
1. Feedback von Nutzern sammeln
2. Verbesserungspotenzial identifizieren
3. Updates planen und priorisieren

**Quartalsweise:**
1. Inhaltliche Aktualität prüfen (Tarif-Änderungen?)
2. Browser-Kompatibilität testen
3. Neue Features evaluieren

**Jährlich:**
1. Komplette Inhaltsprüfung
2. Design-Refresh erwägen
3. Technologie-Update (moderne JavaScript-Features)

### Backup-Strategie

**Git-Repository:**
```bash
# Täglich automatisch (via Git-Host wie GitHub/GitLab)
git push origin main

# Manuell vor größeren Änderungen
git commit -m "Pre-update backup"
git push
```

**Lokale Backups:**
```bash
# Vor Major-Updates
cp ambulantes-tarifsystem-schulung-komplett.html \
   backups/ambulantes-tarifsystem-schulung-v1.0-backup-$(date +%Y%m%d).html
```

---

## ⚠️ Troubleshooting

### Häufige Probleme und Lösungen

#### Problem: Quiz-Antworten werden nicht korrekt ausgewertet

**Symptom:** Alle Antworten werden als falsch markiert oder Feedback erscheint nicht.

**Lösung:**
1. Browser-Console öffnen (F12)
2. Quiz absenden und auf JavaScript-Fehler achten
3. Prüfen:
   ```javascript
   // Sind die Antworten korrekt definiert?
   console.log(answers);

   // Stimmt der Kapitel-Index?
   // data-chapter="3" → answers[3]

   // Stimmen die value-Attribute?
   // <input type="radio" name="q3_1" value="a">
   // answers[3][1] sollte 'a' sein (als String!)
   ```

#### Problem: Kapitel wird nicht angezeigt

**Symptom:** Nach Klick auf Navigation-Button bleibt Bildschirm leer.

**Lösung:**
```javascript
// 1. Console-Log hinzufügen
function showChapter(index) {
    console.log("Switching to chapter:", index);
    // ... Rest der Funktion
}

// 2. Prüfen ob Kapitel-ID korrekt ist
// <div class="chapter" id="chapter3">
// → showChapter(3)

// 3. Display-Property prüfen
// Alle Kapitel sollten initial style="display: none;" haben
```

#### Problem: Fortschrittsbalken zeigt falsche Prozente

**Symptom:** Fortschrittsbalken bei 120% oder negativen Werten.

**Lösung:**
```javascript
// totalChapters anpassen
const totalChapters = 8;  // Anzahl ALLER Kapitel (inkl. Abschlusstest)

// In updateProgress():
const percentage = ((currentChapter + 1) / totalChapters * 100).toFixed(1);
```

#### Problem: Akkordeon klappt nicht auf/zu

**Symptom:** Klick auf Akkordeon-Header hat keine Wirkung.

**Lösung:**
```html
<!-- onclick muss "this" übergeben -->
<div class="accordion-header" onclick="toggleAccordion(this)">
    <!-- NICHT onclick="toggleAccordion()" -->
</div>
```

#### Problem: Responsive Design bricht auf Mobile

**Symptom:** Text überlappt, Buttons sind zu klein, horizontales Scrollen nötig.

**Lösung:**
```css
/* Media Query prüfen */
@media (max-width: 768px) {
    .container { padding: 10px; }
    .content { padding: 15px; }
    .nav-buttons { flex-direction: column; }
    button { width: 100%; margin: 5px 0; }
}

/* Viewport Meta-Tag prüfen */
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

#### Problem: Datei zu groß (>2 MB)

**Symptom:** Lange Ladezeiten, E-Mail-Versand scheitert.

**Lösungen:**
1. **CSS minifizieren**
   ```css
   /* Vorher */
   .info-box {
       background-color: #e8f4f8;
       border-left: 5px solid #667eea;
       padding: 20px;
   }

   /* Nachher */
   .info-box{background-color:#e8f4f8;border-left:5px solid #667eea;padding:20px}
   ```

2. **JavaScript minifizieren** (Online Tool: https://javascript-minifier.com/)

3. **Eingebettete Bilder komprimieren**
   - WebP statt PNG/JPG
   - Maximale Breite: 800px
   - Qualität: 70-80%

4. **Unnötige Kommentare entfernen**

### Debug-Modus aktivieren

Für detailliertes Debugging:

```javascript
// Am Anfang des <script>-Bereichs hinzufügen
const DEBUG = true;

function log(...args) {
    if (DEBUG) console.log(...args);
}

// Dann in Funktionen verwenden:
function showChapter(index) {
    log("showChapter called with index:", index);
    log("currentChapter before:", currentChapter);
    // ... Rest der Funktion
}
```

### Browser-spezifische Probleme

**Internet Explorer (Legacy):**
- Falls Unterstützung nötig: ES6 Features vermeiden
- Arrow Functions `() =>` durch normale Functions ersetzen
- `const`/`let` durch `var` ersetzen

**Safari (iOS):**
- `onclick` funktioniert manchmal nicht → `addEventListener` verwenden
- Transitions können ruckeln → `transform` statt `top/left` verwenden

---

## 📞 Support & Kontakt

### Bei technischen Problemen

1. **Dokumentation prüfen**
   - Diese Datei durchlesen
   - `PROMPT-Schulungsunterlage-Vorgaben.md` konsultieren

2. **Git-History durchsuchen**
   ```bash
   git log --oneline
   git show <commit-id>
   ```

3. **Community/Team fragen**
   - Internes Forum
   - Entwickler-Team kontaktieren

### Weitere Ressourcen

- **HTML/CSS/JavaScript Referenz:** [MDN Web Docs](https://developer.mozilla.org)
- **Browser-Kompatibilität:** [Can I Use](https://caniuse.com)
- **Validator:** [W3C Validator](https://validator.w3.org)

---

## 📝 Anhang

### Schnellreferenz: Wichtige Code-Snippets

**Neue Info-Box:**
```html
<div class="info-box">
    <h4>📋 Titel</h4>
    <p>Text...</p>
</div>
```

**Neue Tabelle:**
```html
<table class="comparison-table">
    <thead>
        <tr>
            <th>Spalte 1</th>
            <th>Spalte 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Wert 1</td>
            <td>Wert 2</td>
        </tr>
    </tbody>
</table>
```

**Neue Quiz-Frage:**
```html
<div class="quiz-question" data-chapter="3" data-question="1">
    <h4>Frage 1: Fragetext?</h4>
    <div class="quiz-options">
        <label class="quiz-option">
            <input type="radio" name="q3_1" value="a">
            Antwort A
        </label>
        <label class="quiz-option">
            <input type="radio" name="q3_1" value="b">
            Antwort B
        </label>
        <label class="quiz-option">
            <input type="radio" name="q3_1" value="c">
            Antwort C
        </label>
        <label class="quiz-option">
            <input type="radio" name="q3_1" value="d">
            Antwort D
        </label>
    </div>
    <div class="quiz-feedback"></div>
</div>
```

### Git-Befehle Cheat Sheet

```bash
# Status prüfen
git status

# Änderungen anzeigen
git diff

# Änderungen stagen
git add .

# Commit erstellen
git commit -m "Beschreibung"

# Push zu Remote
git push origin main

# Letzte Commits anzeigen
git log --oneline -10

# Datei auf alten Stand zurücksetzen
git checkout HEAD~1 -- datei.html

# Änderungen verwerfen
git restore datei.html
```

---

**Version:** 1.0
**Erstellt:** 2025-10-21
**Nächste Review:** 2025-11-21

---

*Diese Entwicklungsdokumentation ist ein lebendes Dokument und sollte bei Änderungen am Entwicklungsprozess aktualisiert werden.*
