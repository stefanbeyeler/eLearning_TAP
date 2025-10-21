# Richtlinien für eLearning TAP - Schulungsunterlagen

**Projekt:** eLearning für TARDOC und ambulante Pauschalen
**Version:** 2.0
**Letzte Aktualisierung:** 2025-10-21

> Diese Datei konsolidiert alle Design-, Entwicklungs- und Inhaltsvorgaben für die interaktiven HTML-Schulungsunterlagen zum ambulanten Tarifsystem.

---

## 📋 Inhaltsverzeichnis

1. [Projekt-Übersicht](#projekt-übersicht)
2. [Typography-System](#typography-system)
3. [Design-System](#design-system)
4. [Technische Architektur](#technische-architektur)
5. [Content-Struktur](#content-struktur)
6. [Interaktive Komponenten](#interaktive-komponenten)
7. [Entwicklungsworkflow](#entwicklungsworkflow)
8. [Testing & Qualitätssicherung](#testing--qualitätssicherung)
9. [Deployment & Wartung](#deployment--wartung)

---

## 🎯 Projekt-Übersicht

### Zweck
Interaktive HTML-basierte Schulungsunterlagen für das ambulante Tarifsystem der Schweiz (LKAAT, TARDOC, Ambulante Pauschalen), die im Intranet bereitgestellt werden.

### Hauptziele
- ✅ Vermittlung von Basiswissen zum ambulanten Tarifsystem
- ✅ Interaktive Lernelemente mit sofortigem Feedback
- ✅ Professionelles, konsistentes Design
- ✅ Single-File HTML (keine externen Abhängigkeiten)
- ✅ Mobile-responsive Darstellung
- ✅ Intuitive Navigation zwischen Kapiteln
- ✅ Integrierte Wissensüberprüfung

### Zielgruppe
- Medizinisches Personal
- Verwaltungsmitarbeitende
- Codierer/innen in Schweizer Spitälern
- Alle Anwender:innen des ambulanten Tarifsystems

---

## 🔤 Typography-System

### Schriftarten

#### Überschriften (h1-h3)
**Font-Family:** DTL Documenta WT Bold

```css
h1, h2, h3 {
    font-family: 'DTL Documenta WT', Georgia, 'Times New Roman', serif;
    font-weight: 700;
}
```

**Fallback-Schriften:** Georgia, Times New Roman, serif

#### Body-Text & Kleinere Überschriften (h4-h6)
**Font-Family:** Typ 1451 LL

```css
body, p, h4, h5, h6, li, td, th {
    font-family: 'Typ 1451 LL', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-weight: 400;
}
```

**Fallback-Schriften:** Segoe UI, Tahoma, Geneva, Verdana, sans-serif

### Typografische Hierarchie

#### Responsive Heading-Größen

| Element | XL (>1440px) | LG (1025-1440px) | SM (431-1024px) | XS (<430px) |
|---------|--------------|------------------|-----------------|-------------|
| **h1** | 60px / 1.2em | 48px / 1.2em | 36px / 1.2em | 28px / 1.2em |
| **h2** | 36px / 1.2em | 28px / 1.2em | 24px / 1.2em | 21px / 1.2em |
| **h3** | 24px / 1.2em | 24px / 1.2em | 21px / 1.2em | 21px / 1.2em |
| **h4** | 18px / 1.4em<br>Tracking: 2px | 16px / 1.4em<br>Tracking: 2px | 14px / 1.4em<br>Tracking: 2px | 14px / 1.4em<br>Tracking: 2px |
| **h5** | 20px / 1.5em | 18px / 1.5em | 16px / 1.5em | 16px / 1.5em |
| **h6** | 14px / 1.3em<br>Tracking: 2px | 14px / 1.3em<br>Tracking: 2px | 12px / 1.3em<br>Tracking: 2px | 12px / 1.3em<br>Tracking: 2px |

#### Body-Text

```css
body {
    font-family: 'Typ 1451 LL', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 16px;
    line-height: 1.6;
    color: #333333;
}

p {
    margin-bottom: 1em;
    line-height: 1.6;
}
```

### Hyperlinks

#### Überschriften-Links (h1-h3)

**Standard-State:**
```css
h1 a, h2 a, h3 a {
    color: inherit; /* Erbt Farbe von Überschrift */
    text-decoration: underline;
    transition: color 0.3s ease;
}
```

**Hover-State:**
```css
h1 a:hover, h2 a:hover, h3 a:hover {
    color: #2A64B0; /* Blauton */
    text-decoration: underline;
}
```

#### Body-Links

**Standard-State:**
```css
a {
    color: #2A64B0; /* Primärer Link-Blauton */
    text-decoration: underline;
    transition: color 0.3s ease;
}
```

**Hover-State:**
```css
a:hover {
    color: #282828; /* Dunkelgrau */
    text-decoration: underline;
}
```

### Typografische Best Practices

1. **Hierarchie einhalten**: H1 > H2 > H3 > H4 > H5 > H6 (nicht überspringen)
2. **Line-Height**: Mindestens 1.2em für Überschriften, 1.6 für Body-Text
3. **Letter-Spacing (Tracking)**: Nur bei H4 und H6 (2px)
4. **Konsistenz**: Immer dieselben Font-Families verwenden
5. **Responsive Anpassung**: Schriftgrößen bei kleineren Viewports reduzieren

---

## 🎨 Design-System

### Farbpalette

#### Primärfarben
```css
/* Hauptfarben für Branding */
--primary-blue: #667eea;
--primary-violet: #764ba2;
--primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

#### UI-Farben
```css
/* Content & Hintergrund */
--background-white: #ffffff;
--text-dark: #333333;
--text-medium: #666666;
--text-light: #999999;

/* Status-Farben */
--success-green: #28a745;
--warning-yellow: #ffc107;
--error-red: #dc3545;
--info-blue: #e8f4f8;
```

#### Interaktive Elemente
```css
/* Links */
--link-default: #2A64B0;
--link-hover: #282828;

/* Buttons */
--button-primary: #667eea;
--button-primary-hover: #5568d3;
--button-secondary: #6c757d;
--button-secondary-hover: #5a6268;
```

### Layout-System

#### Container & Spacing

```css
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* Responsive Spacing */
@media (max-width: 768px) {
    .container {
        padding: 10px;
    }
}

/* Standard-Abstände */
--spacing-xs: 5px;
--spacing-sm: 10px;
--spacing-md: 15px;
--spacing-lg: 20px;
--spacing-xl: 30px;
```

#### Grid-System (falls benötigt)

```css
.grid {
    display: grid;
    gap: 20px;
}

.grid-2-cols {
    grid-template-columns: repeat(2, 1fr);
}

.grid-3-cols {
    grid-template-columns: repeat(3, 1fr);
}

@media (max-width: 768px) {
    .grid-2-cols,
    .grid-3-cols {
        grid-template-columns: 1fr;
    }
}
```

### Komponenten-Styling

#### Header
```css
header {
    background: #ffffff;
    border-radius: 15px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    padding: 30px;
    margin-bottom: 20px;
    text-align: center;
}
```

#### Navigation
```css
nav {
    background: #ffffff;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding: 15px;
    margin-bottom: 20px;
}

.nav-buttons {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
}

.nav-btn {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 12px 20px;
    font-size: 14px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.nav-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(102, 126, 234, 0.3);
}

.nav-btn.active {
    background: #764ba2;
    font-weight: bold;
}

@media (max-width: 768px) {
    .nav-buttons {
        flex-direction: column;
    }

    .nav-btn {
        width: 100%;
    }
}
```

#### Content-Bereiche
```css
.content {
    background: #ffffff;
    border-radius: 10px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    padding: 30px;
    margin-bottom: 20px;
    min-height: 500px;
}

@media (max-width: 768px) {
    .content {
        padding: 15px;
    }
}
```

#### Info-Boxen
```css
/* Standard Info-Box (Blau) */
.info-box {
    background-color: #e8f4f8;
    border-left: 5px solid #667eea;
    border-radius: 5px;
    padding: 20px;
    margin: 20px 0;
}

/* Warning-Box (Gelb) */
.warning-box {
    background-color: #fff3cd;
    border-left: 5px solid #ffc107;
    border-radius: 5px;
    padding: 20px;
    margin: 20px 0;
}

/* Success-Box (Grün) */
.success-box {
    background-color: #d4edda;
    border-left: 5px solid #28a745;
    border-radius: 5px;
    padding: 20px;
    margin: 20px 0;
}

.info-box h4,
.warning-box h4,
.success-box h4 {
    margin-top: 0;
    margin-bottom: 15px;
}
```

#### Tabellen
```css
.comparison-table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.comparison-table thead {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
}

.comparison-table th,
.comparison-table td {
    padding: 12px 15px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}

.comparison-table tbody tr:hover {
    background-color: #f5f5f5;
}

@media (max-width: 768px) {
    .comparison-table {
        font-size: 14px;
    }

    .comparison-table th,
    .comparison-table td {
        padding: 8px 10px;
    }
}
```

#### Listen
```css
.list-styled {
    list-style: none;
    padding-left: 0;
}

.list-styled li {
    padding-left: 25px;
    position: relative;
    margin-bottom: 10px;
}

.list-styled li::before {
    content: "▸";
    position: absolute;
    left: 0;
    color: #667eea;
    font-weight: bold;
}
```

### Buttons

```css
/* Primärer Button */
button, .btn {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 12px 24px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
}

button:hover, .btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(102, 126, 234, 0.4);
}

button:active, .btn:active {
    transform: translateY(0);
}

button:disabled, .btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

/* Sekundärer Button */
.btn-secondary {
    background: #6c757d;
}

.btn-secondary:hover {
    background: #5a6268;
}

/* Footer-Navigation-Buttons */
.navigation-footer {
    display: flex;
    justify-content: space-between;
    margin-top: 30px;
    gap: 10px;
}

.nav-footer-btn {
    flex: 1;
    max-width: 200px;
}

@media (max-width: 768px) {
    .navigation-footer {
        flex-direction: column;
    }

    .nav-footer-btn {
        max-width: 100%;
        width: 100%;
    }
}
```

### Fortschrittsbalken

```css
.progress-container {
    width: 100%;
    background-color: #e0e0e0;
    border-radius: 10px;
    overflow: hidden;
    margin-top: 15px;
}

.progress-bar {
    height: 20px;
    background: linear-gradient(90deg, #667eea, #764ba2);
    border-radius: 10px;
    transition: width 0.5s ease;
    text-align: center;
    color: white;
    font-size: 12px;
    line-height: 20px;
    font-weight: bold;
}
```

---

## 🛠 Technische Architektur

### Single-File-Application

**Dateiformat:** HTML5 mit embedded CSS und JavaScript

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Schulung: Ambulantes Tarifsystem</title>
    <style>
        /* Alle CSS-Styles hier einbetten */
    </style>
</head>
<body>
    <div class="container">
        <!-- Content hier -->
    </div>

    <script>
        /* Alle JavaScript-Funktionen hier einbetten */
    </script>
</body>
</html>
```

### Browser-Kompatibilität

**Unterstützte Browser:**
- Chrome (neueste Version)
- Firefox (neueste Version)
- Safari (neueste Version)
- Edge (neueste Version)

**Nicht unterstützt:** Internet Explorer

### Technologie-Stack

| Komponente | Technologie | Version |
|------------|-------------|---------|
| Markup | HTML5 | - |
| Styling | CSS3 | - |
| Scripting | JavaScript | ES6+ |
| Encoding | UTF-8 | - |

### Keine externen Abhängigkeiten

**Wichtig:** Alle Ressourcen müssen inline/embedded sein:
- ❌ KEINE CDN-Links (jQuery, Bootstrap, etc.)
- ❌ KEINE externen CSS-Dateien
- ❌ KEINE externen JavaScript-Dateien
- ❌ KEINE externen Schriftarten (Web Fonts von Google, etc.)
- ✅ Alle Styles im `<style>`-Tag
- ✅ Alle Scripts im `<script>`-Tag
- ✅ Bilder als Base64-encoded Data-URLs (falls benötigt)

---

## 📚 Content-Struktur

### Kapitel-Übersicht

```javascript
const chapters = [
    { id: 0, title: "Kapitel 1: Einführung" },
    { id: 1, title: "Kapitel 2: Ambulante Behandlung" },
    { id: 2, title: "Kapitel 3: LKAAT" },
    { id: 3, title: "Kapitel 4: TARDOC" },
    { id: 4, title: "Kapitel 5: Ambulante Pauschalen" },
    { id: 5, title: "Kapitel 6: Vergleich" },
    { id: 6, title: "Kapitel 7: Praxisanwendung" },
    { id: 7, title: "Abschlusstest" }
];
```

### Standard-Kapitel-Template

```html
<div class="chapter" id="chapterX" style="display: none;">
    <h2>Kapitel X: [Titel]</h2>

    <!-- 1. Einleitung -->
    <p>Einleitungstext zum Kapitel...</p>

    <!-- 2. Hauptinhalt mit Unterkapiteln -->
    <h3>Unterkapitel-Titel</h3>
    <p>Inhalt...</p>

    <!-- 3. Info-Box für wichtige Punkte -->
    <div class="info-box">
        <h4>📋 Wichtige Information</h4>
        <ul class="list-styled">
            <li>Punkt 1</li>
            <li>Punkt 2</li>
            <li>Punkt 3</li>
        </ul>
    </div>

    <!-- 4. Akkordeon für erweiterte Inhalte -->
    <div class="accordion">
        <div class="accordion-item">
            <div class="accordion-header" onclick="toggleAccordion(this)">
                <strong>📖 Erweiterte Informationen</strong>
                <span class="accordion-icon">▼</span>
            </div>
            <div class="accordion-content">
                <p>Zusätzliche Details...</p>
            </div>
        </div>
    </div>

    <!-- 5. Vergleichstabelle (optional) -->
    <table class="comparison-table">
        <thead>
            <tr>
                <th>Kriterium</th>
                <th>Option A</th>
                <th>Option B</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Beispiel</td>
                <td>Wert A</td>
                <td>Wert B</td>
            </tr>
        </tbody>
    </table>

    <!-- 6. Praktisches Beispiel -->
    <div class="success-box">
        <h4>💡 Praxisbeispiel</h4>
        <p><strong>Situation:</strong> Beschreibung...</p>
        <p><strong>Vorgehen:</strong> Schritt-für-Schritt...</p>
        <p><strong>Ergebnis:</strong> Fazit...</p>
    </div>

    <!-- 7. Quiz-Sektion -->
    <div class="quiz-section">
        <h3>Verständnisfragen Kapitel X</h3>

        <!-- Quiz-Fragen hier -->

        <button class="submit-quiz" onclick="checkChapterQuiz(X)">
            Antworten überprüfen
        </button>
        <div class="quiz-result" id="result-chapterX"></div>
    </div>

    <!-- 8. Kapitel-Navigation -->
    <div class="navigation-footer">
        <button class="nav-footer-btn" onclick="showChapter(X-1)">
            ◄ Vorheriges Kapitel
        </button>
        <button class="nav-footer-btn" onclick="showChapter(X+1)">
            Nächstes Kapitel ►
        </button>
    </div>
</div>
```

### Inhaltliche Vorgaben pro Kapitel

#### Kapitel 1: Einführung
**Lernziele:**
- Überblick über das Gesamt-Tarifsystem
- Die drei Komponenten vorstellen
- Notwendigkeit und Vorteile erklären

**Inhalte:**
1. Was ist das ambulante Gesamt-Tarifsystem?
2. Komponenten des Systems (LKAAT, TARDOC, Pauschalen)
3. Warum verschiedene Komponenten?
4. Lernziele des Moduls

**Quiz:** 2 Fragen

---

#### Kapitel 2: Ambulante Behandlung
**Lernziele:**
- Definition ambulanter Behandlungen verstehen
- Abgrenzung zu stationären Behandlungen kennen
- Typische Anwendungsbereiche identifizieren

**Inhalte:**
1. Was ist eine ambulante Behandlung?
2. Abgrenzung: Ambulant vs. Stationär (Vergleichstabelle)
3. Wichtige Abgrenzungsfälle
4. Typische ambulante Behandlungen (Akkordeon)
5. Vorteile ambulanter Behandlungen
6. Trend zur Ambulantisierung
7. Besonderheiten bei der Abrechnung
8. Praktisches Beispiel (Fallbeispiel)

**Quiz:** 4 Fragen

---

#### Kapitel 3: LKAAT
**Lernziele:**
- Funktion des LKAAT verstehen
- Leistungstypen unterscheiden können
- Triggerpositionen erkennen

**Inhalte:**
1. Was ist der LKAAT?
2. Struktur und Aufbau (Tabelle: Typen E, EZ, P, PZ)
3. Entscheidung TARDOC vs. Pauschale (Akkordeon mit 3 Schritten)
4. LKN-Nummern verstehen (8-stellig vs 9-stellig)
5. Triggerpositionen - Das Herzstück des Systems
6. Praktisches Beispiel (Fallbeispiel: Zwei Behandlungen)
7. Tools für die Arbeit mit dem LKAAT
8. Häufige Fehler beim LKAAT

**Quiz:** 4 Fragen

---

#### Kapitel 4: TARDOC
**Lernziele:**
- TARDOC als Einzelleistungstarif verstehen
- Berechnungsformel anwenden können
- Wichtige Regelungen kennen

**Inhalte:**
1. Was ist TARDOC?
2. Hauptmerkmale (Info-Box)
3. Struktur des TARDOC-Tarifs (Akkordeon)
4. Berechnung der Vergütung (Formel + Beispiel)
5. Wichtige Regelungen (Kumulation, Zuschläge, Limitationen, Dignität)
6. Häufige Fehlerquellen

**Quiz:** 3 Fragen

---

#### Kapitel 5: Ambulante Pauschalen
**Lernziele:**
- Prinzip der Pauschalen verstehen
- Anwendungsbereiche kennen
- Vor- und Nachteile beurteilen können

**Inhalte:**
1. Was sind Ambulante Pauschalen?
2. Kernprinzip (Info-Box)
3. Anwendungsbereiche
4. Struktur (Akkordeon: AP-Gruppen, Inkludierte Leistungen, Zusatzentgelte)
5. Vorteile für Leistungserbringer und Kostenträger
6. Praktisches Beispiel: Kataraktoperation
7. Wichtige Abgrenzungen

**Quiz:** 3 Fragen

---

#### Kapitel 6: Vergleich
**Lernziele:**
- TARDOC und Pauschalen gegenüberstellen
- Entscheidungskriterien anwenden
- Kombinationsmöglichkeiten kennen

**Inhalte:**
1. Gegenüberstellung der Systeme (Vergleichstabelle)
2. Wann welches System? (Info-Box mit Entscheidungshilfe)
3. Kombinationsmöglichkeiten (Akkordeon)
4. Praktische Fallbeispiele (3 Beispiele)

**Quiz:** 3 Fragen

---

#### Kapitel 7: Praxisanwendung
**Lernziele:**
- Workflow in der Praxis kennen
- Fehlerquellen vermeiden
- Effizient arbeiten können

**Inhalte:**
1. Der Workflow in der Praxis (Akkordeon: 3 Schritte)
2. Häufige Fehlerquellen und deren Vermeidung (Top 5)
3. Tipps für effizientes Arbeiten
4. Rechtliche und ethische Aspekte
5. Zukunftsperspektiven

**Quiz:** 3 Fragen

---

#### Kapitel 8: Abschlusstest
**Format:** 12 Multiple-Choice-Fragen aus allen Kapiteln
**Bestehensgrenze:** 10 von 12 richtigen Antworten (83%)
**Feedback:** Detailliertes Ergebnis mit Bestanden/Nicht bestanden

---

## ⚙️ Interaktive Komponenten

### Akkordeon

**HTML-Struktur:**
```html
<div class="accordion">
    <div class="accordion-item">
        <div class="accordion-header" onclick="toggleAccordion(this)">
            <strong>📖 Titel des Akkordeons</strong>
            <span class="accordion-icon">▼</span>
        </div>
        <div class="accordion-content">
            <p>Versteckter Inhalt...</p>
            <ul>
                <li>Detail 1</li>
                <li>Detail 2</li>
            </ul>
        </div>
    </div>
</div>
```

**CSS:**
```css
.accordion {
    margin: 20px 0;
}

.accordion-item {
    border: 1px solid #ddd;
    border-radius: 5px;
    margin-bottom: 10px;
    overflow: hidden;
}

.accordion-header {
    background: #f8f9fa;
    padding: 15px;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: background 0.3s ease;
}

.accordion-header:hover {
    background: #e9ecef;
}

.accordion-icon {
    transition: transform 0.3s ease;
    font-size: 12px;
}

.accordion-item.active .accordion-icon {
    transform: rotate(180deg);
}

.accordion-content {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease;
    padding: 0 15px;
}

.accordion-item.active .accordion-content {
    max-height: 1000px;
    padding: 15px;
}
```

**JavaScript:**
```javascript
function toggleAccordion(header) {
    const accordionItem = header.parentElement;
    accordionItem.classList.toggle('active');
}
```

### Quiz-System

**HTML-Struktur:**
```html
<div class="quiz-section">
    <h3>Verständnisfragen Kapitel X</h3>

    <div class="quiz-question" data-chapter="X" data-question="1">
        <h4>Frage 1: Was ist das ambulante Tarifsystem?</h4>
        <div class="quiz-options">
            <label class="quiz-option">
                <input type="radio" name="qX_1" value="a">
                Antwort A
            </label>
            <label class="quiz-option">
                <input type="radio" name="qX_1" value="b">
                Antwort B
            </label>
            <label class="quiz-option">
                <input type="radio" name="qX_1" value="c">
                Antwort C (korrekt)
            </label>
            <label class="quiz-option">
                <input type="radio" name="qX_1" value="d">
                Antwort D
            </label>
        </div>
        <div class="quiz-feedback"></div>
    </div>

    <button class="submit-quiz" onclick="checkChapterQuiz(X)">
        Antworten überprüfen
    </button>
    <div class="quiz-result" id="result-chapterX"></div>
</div>
```

**CSS:**
```css
.quiz-section {
    background: #f8f9fa;
    border-radius: 10px;
    padding: 25px;
    margin-top: 30px;
}

.quiz-question {
    background: white;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.quiz-question h4 {
    margin-top: 0;
    color: #333;
}

.quiz-options {
    margin: 15px 0;
}

.quiz-option {
    display: block;
    padding: 12px;
    margin: 8px 0;
    background: #f8f9fa;
    border: 2px solid transparent;
    border-radius: 5px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.quiz-option:hover {
    background: #e9ecef;
    border-color: #667eea;
}

.quiz-option input[type="radio"] {
    margin-right: 10px;
}

.quiz-feedback {
    margin-top: 15px;
    padding: 15px;
    border-radius: 5px;
    display: none;
}

.quiz-feedback.correct {
    display: block;
    background: #d4edda;
    border: 1px solid #28a745;
    color: #155724;
}

.quiz-feedback.incorrect {
    display: block;
    background: #f8d7da;
    border: 1px solid #dc3545;
    color: #721c24;
}

.submit-quiz {
    margin-top: 20px;
}

.quiz-result {
    margin-top: 20px;
    padding: 20px;
    border-radius: 8px;
    text-align: center;
    font-weight: bold;
}

.quiz-result.pass {
    background: #d4edda;
    border: 2px solid #28a745;
    color: #155724;
}

.quiz-result.fail {
    background: #f8d7da;
    border: 2px solid #dc3545;
    color: #721c24;
}
```

**JavaScript:**
```javascript
// Antworten-Objekt
const answers = {
    1: { 1: 'c', 2: 'b' },  // Kapitel 1
    2: { 1: 'b', 2: 'a', 3: 'c', 4: 'b' },  // Kapitel 2
    3: { 1: 'a', 2: 'c', 3: 'b', 4: 'd' },  // Kapitel 3
    4: { 1: 'b', 2: 'c', 3: 'a' },  // Kapitel 4
    5: { 1: 'c', 2: 'b', 3: 'a' },  // Kapitel 5
    6: { 1: 'b', 2: 'a', 3: 'c' },  // Kapitel 6
    7: { 1: 'c', 2: 'b', 3: 'a' },  // Kapitel 7
    final: { 1: 'a', 2: 'b', 3: 'c', /* ... */ 12: 'b' }  // Abschlusstest
};

// Feedback-Texte
const feedbackTexts = {
    1: {
        1: {
            correct: "✓ Richtig! Das ambulante Tarifsystem besteht aus drei Komponenten.",
            incorrect: "✗ Falsch. Das ambulante Tarifsystem umfasst LKAAT, TARDOC und Ambulante Pauschalen."
        },
        2: {
            correct: "✓ Richtig! Der LKAAT ist der Leistungskatalog.",
            incorrect: "✗ Falsch. LKAAT steht für Leistungskatalog ambulanter Behandlungen und Abklärungen in Spitälern und Kliniken."
        }
    },
    // ... für alle Kapitel
};

// Quiz-Auswertung
function checkChapterQuiz(chapter) {
    const questions = document.querySelectorAll(`.quiz-question[data-chapter="${chapter}"]`);
    let correct = 0;
    let total = questions.length;

    questions.forEach(question => {
        const questionNum = question.dataset.question;
        const selectedOption = question.querySelector('input[type="radio"]:checked');
        const feedbackDiv = question.querySelector('.quiz-feedback');

        if (!selectedOption) {
            feedbackDiv.className = 'quiz-feedback incorrect';
            feedbackDiv.textContent = '⚠ Bitte wählen Sie eine Antwort.';
            return;
        }

        const userAnswer = selectedOption.value;
        const correctAnswer = answers[chapter][questionNum];

        if (userAnswer === correctAnswer) {
            correct++;
            feedbackDiv.className = 'quiz-feedback correct';
            feedbackDiv.innerHTML = feedbackTexts[chapter][questionNum].correct;
        } else {
            feedbackDiv.className = 'quiz-feedback incorrect';
            feedbackDiv.innerHTML = feedbackTexts[chapter][questionNum].incorrect;
        }
    });

    // Ergebnis anzeigen
    const resultDiv = document.getElementById(`result-chapter${chapter}`);
    const percentage = ((correct / total) * 100).toFixed(0);

    resultDiv.innerHTML = `
        <strong>Ergebnis:</strong> ${correct} von ${total} Fragen richtig (${percentage}%)
        <br>
        ${percentage >= 66
            ? '✓ Gut gemacht! Sie können zum nächsten Kapitel übergehen.'
            : '⚠ Bitte wiederholen Sie dieses Kapitel.'}
    `;

    if (percentage >= 66) {
        resultDiv.className = 'quiz-result pass';
    } else {
        resultDiv.className = 'quiz-result fail';
    }

    // Scroll to result
    resultDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}
```

### Navigation-System

**JavaScript:**
```javascript
// Globale Variablen
let currentChapter = 0;
const totalChapters = 8;

// Initialisierung
document.addEventListener('DOMContentLoaded', function() {
    showChapter(0);
});

// Kapitel anzeigen
function showChapter(index) {
    // Validierung
    if (index < 0 || index >= totalChapters) return;

    // Alle Kapitel ausblenden
    const chapters = document.querySelectorAll('.chapter');
    chapters.forEach(chapter => {
        chapter.style.display = 'none';
    });

    // Gewähltes Kapitel anzeigen
    const selectedChapter = document.getElementById(`chapter${index}`);
    if (selectedChapter) {
        selectedChapter.style.display = 'block';
    }

    // Navigation-Buttons aktualisieren
    const navButtons = document.querySelectorAll('.nav-btn');
    navButtons.forEach((btn, i) => {
        if (i === index) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });

    // Aktuelles Kapitel speichern
    currentChapter = index;

    // Fortschritt aktualisieren
    updateProgress();

    // Nach oben scrollen
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Fortschrittsbalken aktualisieren
function updateProgress() {
    const percentage = ((currentChapter + 1) / totalChapters * 100).toFixed(1);
    const progressBar = document.getElementById('progress-bar');

    if (progressBar) {
        progressBar.style.width = percentage + '%';
        progressBar.textContent = percentage + '%';
    }
}

// Schulung zurücksetzen
function resetTraining() {
    if (confirm('Möchten Sie die Schulung wirklich zurücksetzen?')) {
        // Alle Radio-Buttons deselektieren
        document.querySelectorAll('input[type="radio"]').forEach(radio => {
            radio.checked = false;
        });

        // Alle Feedbacks ausblenden
        document.querySelectorAll('.quiz-feedback').forEach(feedback => {
            feedback.style.display = 'none';
        });

        // Alle Ergebnisse ausblenden
        document.querySelectorAll('.quiz-result').forEach(result => {
            result.innerHTML = '';
            result.className = 'quiz-result';
        });

        // Zurück zu Kapitel 1
        showChapter(0);
    }
}
```

---

## 🔄 Entwicklungsworkflow

### 1. Neues Kapitel hinzufügen

**Schritt-für-Schritt-Anleitung:**

#### A. Planung (5-10 Minuten)
1. Lernziele definieren (3-5 Ziele)
2. Inhaltsstruktur skizzieren
3. Quiz-Fragen vorbereiten (2-4 Fragen)
4. Praktische Beispiele überlegen

#### B. HTML-Struktur erstellen (15-20 Minuten)

**1. Navigation erweitern:**
```html
<!-- In der <nav>-Sektion -->
<button class="nav-btn" onclick="showChapter(X)">
    Kapitel X: [Titel]
</button>
```

**2. Kapitel-Inhalt erstellen:**
```html
<!-- Im Content-Bereich -->
<div class="chapter" id="chapterX" style="display: none;">
    <!-- Kapitel-Inhalt gemäß Template -->
</div>
```

#### C. JavaScript anpassen (5-10 Minuten)

**1. totalChapters erhöhen:**
```javascript
const totalChapters = X + 1;  // Neue Anzahl
```

**2. Quiz-Antworten hinzufügen:**
```javascript
const answers = {
    // ... bestehende
    X: {
        1: 'a',  // Richtige Antwort für Frage 1
        2: 'c',  // Richtige Antwort für Frage 2
        // ...
    }
};
```

**3. Feedback-Texte hinzufügen:**
```javascript
const feedbackTexts = {
    // ... bestehende
    X: {
        1: {
            correct: "✓ Richtig! Erklärung...",
            incorrect: "✗ Falsch. Die richtige Antwort ist..."
        },
        // ...
    }
};
```

#### D. Testing (10-15 Minuten)
- [ ] Kapitel über Navigation erreichbar
- [ ] Vor/Zurück-Buttons funktionieren
- [ ] Quiz-Fragen auswählbar
- [ ] Quiz-Auswertung korrekt
- [ ] Fortschrittsbalken aktualisiert sich
- [ ] Responsive auf Mobile

#### E. Git-Commit
```bash
git add ambulantes-tarifsystem-schulung-komplett.html
git commit -m "feat: Kapitel X - [Titel] hinzugefügt"
git push
```

### 2. Content-Update durchführen

**Für Textänderungen:**
1. Entsprechendes Kapitel-`<div>` lokalisieren
2. Text anpassen
3. Speichern und im Browser testen
4. Committen mit: `content: Kapitel X - [Beschreibung] aktualisiert`

**Für Quiz-Änderungen:**
1. HTML-Fragentext anpassen
2. JavaScript `answers` Objekt aktualisieren
3. JavaScript `feedbackTexts` aktualisieren
4. Testen (alle Antwortoptionen durchgehen)
5. Committen mit: `fix: Kapitel X Quiz korrigiert`

### 3. Design-Anpassungen

**Farben ändern:**
```css
/* Im <style>-Bereich */
:root {
    --primary-blue: #667eea;
    --primary-violet: #764ba2;
    /* ... weitere Variablen */
}
```

**Schriftarten anpassen:**
```css
/* Überschriften */
h1, h2, h3 {
    font-family: 'DTL Documenta WT', Georgia, 'Times New Roman', serif;
}

/* Body-Text */
body, p, h4, h5, h6 {
    font-family: 'Typ 1451 LL', 'Segoe UI', Tahoma, sans-serif;
}
```

### 4. Git-Workflow

```bash
# Status prüfen
git status

# Änderungen anzeigen
git diff

# Änderungen stagen
git add .

# Commit mit konventionellem Message
git commit -m "type: Beschreibung"

# Push zu Remote
git push origin main
```

**Commit-Typen:**
- `feat:` - Neues Feature/Kapitel
- `fix:` - Bugfix
- `content:` - Inhaltliche Änderung
- `style:` - Design-Anpassung
- `refactor:` - Code-Umstrukturierung
- `docs:` - Dokumentation

---

## 🧪 Testing & Qualitätssicherung

### Test-Checkliste vor Deployment

#### Funktionalität
- [ ] Alle Kapitel über Navigation erreichbar
- [ ] Vor/Zurück-Navigation funktioniert
- [ ] Fortschrittsbalken aktualisiert sich
- [ ] Quiz-Antworten auswählbar
- [ ] Quiz-Auswertung korrekt
- [ ] Feedback-Texte korrekt angezeigt
- [ ] Akkordeons öffnen/schließen
- [ ] Reset-Funktion funktioniert

#### Content
- [ ] Keine Rechtschreibfehler
- [ ] Alle Fachbegriffe korrekt
- [ ] Beispiele nachvollziehbar
- [ ] Tabellen vollständig
- [ ] Links funktionieren (falls vorhanden)

#### Design
- [ ] Layout korrekt auf Desktop (>1200px)
- [ ] Layout korrekt auf Tablet (768-1199px)
- [ ] Layout korrekt auf Mobile (375-767px)
- [ ] Alle Farben gemäß Design-System
- [ ] Schriftgrößen responsive
- [ ] Buttons gut klickbar
- [ ] Ausreichende Kontraste

#### Browser-Kompatibilität
- [ ] Chrome (neueste Version)
- [ ] Firefox (neueste Version)
- [ ] Safari (neueste Version)
- [ ] Edge (neueste Version)

#### Performance
- [ ] Ladezeit < 2 Sekunden
- [ ] Keine Verzögerungen bei Navigation
- [ ] Keine JavaScript-Fehler in Console (F12)
- [ ] Smooth Transitions/Animationen

### Debugging-Strategien

**1. Browser DevTools nutzen:**
```javascript
// Console öffnen (F12)
// Fehler suchen im "Console"-Tab

// Quiz-Antworten prüfen
console.log(answers);

// Aktuelles Kapitel prüfen
console.log(currentChapter);

// Feedback-Texte prüfen
console.log(feedbackTexts[1][1]);
```

**2. Häufige Fehlerquellen:**

| Problem | Ursache | Lösung |
|---------|---------|--------|
| Quiz zeigt immer "falsch" | `answers` Objekt falsch | Groß-/Kleinschreibung prüfen |
| Kapitel nicht sichtbar | `display: none` nicht geändert | `showChapter()` debuggen |
| Navigation funktioniert nicht | `onclick` fehlt/falsch | Attribut und Index prüfen |
| Akkordeon klappt nicht | `this` fehlt bei `onclick` | `toggleAccordion(this)` |
| Fortschrittsbalken falsch | `totalChapters` nicht aktualisiert | Wert erhöhen |

**3. Debug-Modus aktivieren:**
```javascript
const DEBUG = true;

function log(...args) {
    if (DEBUG) console.log(...args);
}

// In Funktionen verwenden:
function showChapter(index) {
    log("showChapter:", index);
    // ...
}
```

### Validierung

**HTML-Validierung:**
- Online: https://validator.w3.org/
- Datei hochladen und prüfen

**CSS-Validierung:**
- Online: https://jigsaw.w3.org/css-validator/
- Embedded CSS extrahieren und prüfen

**Accessibility-Check:**
- Keyboard-Navigation testen (Tab-Taste)
- Screen-Reader-kompatibel (ARIA-Labels)
- Farbkontraste ausreichend (WCAG 2.1 Level AA)

---

## 🚀 Deployment & Wartung

### Deployment-Prozess

#### 1. Pre-Deployment
```bash
# Version in Dateinamen
cp ambulantes-tarifsystem-schulung-komplett.html \
   ambulantes-tarifsystem-schulung-v1.0.html

# Test-Checkliste durchgehen
# (siehe Testing-Sektion)
```

#### 2. Intranet-Upload
```
Zielort: /intranet/schulungen/
URL: https://intranet.example.ch/schulungen/ambulantes-tarifsystem-schulung-v1.0.html
```

#### 3. Zugriffsmöglichkeiten

**Option 1: Webserver**
- Apache, Nginx, IIS
- Direkte URL

**Option 2: File-Share**
```
\\server\schulungen\ambulantes-tarifsystem-schulung-v1.0.html
```

**Option 3: E-Mail-Versand**
- Als Anhang (nur bei <2 MB)

**Option 4: Offline/USB**
- Für externe Nutzung

### Versionierung

**Schema:** `MAJOR.MINOR.PATCH`

- **MAJOR (1.0.0)**: Neue Kapitel, große Strukturänderungen
- **MINOR (1.1.0)**: Neue Inhalte, erweiterte Quiz
- **PATCH (1.0.1)**: Bugfixes, Tippfehler

**Changelog pflegen:**
```html
<!--
CHANGELOG

Version 1.1.0 - 2025-11-15
- [Neu] Kapitel 5: Praxisbeispiel Kataraktoperation hinzugefügt
- [Geändert] Quiz Kapitel 3 erweitert (jetzt 5 Fragen)
- [Behoben] Akkordeon in Kapitel 4 funktioniert korrekt

Version 1.0.1 - 2025-10-25
- [Behoben] Tippfehler in Kapitel 3 korrigiert
- [Behoben] Quiz-Feedback Kapitel 7 präzisiert

Version 1.0.0 - 2025-10-21
- Initial Release
-->
```

### Wartungsplan

**Monatlich:**
- Feedback von Nutzern sammeln
- Kleine Verbesserungen umsetzen
- Content auf Aktualität prüfen

**Quartalsweise:**
- Tarif-Änderungen einpflegen
- Browser-Kompatibilität testen
- Neue Features evaluieren

**Jährlich:**
- Komplette Inhaltsprüfung
- Design-Refresh erwägen
- Technologie-Update

### Backup-Strategie

**Git-Repository (täglich):**
```bash
git commit -m "Beschreibung"
git push origin main
```

**Lokale Backups (vor Major-Updates):**
```bash
mkdir -p backups
cp ambulantes-tarifsystem-schulung-komplett.html \
   backups/backup-$(date +%Y%m%d).html
```

---

## 📞 Support & Ressourcen

### Dokumentation
- [GUIDELINES.md](GUIDELINES.md) - Diese Datei
- [PROMPT-Schulungsunterlage-Vorgaben.md](PROMPT-Schulungsunterlage-Vorgaben.md) - KI-Prompts
- [README.md](README.md) - Projekt-Übersicht

### Externe Ressourcen
- **HTML/CSS/JS:** [MDN Web Docs](https://developer.mozilla.org)
- **Browser-Kompatibilität:** [Can I Use](https://caniuse.com)
- **Validator:** [W3C](https://validator.w3.org)

### Fachliche Quellen
- Offizielle TARDOC-Dokumentation
- LKAAT-Katalog (Ärztekasse/FMH)
- Ambulante Pauschalen-Handbuch
- SwissDRG-Dokumentation

---

## 📝 Anhang

### Schnellreferenz: Code-Snippets

**Neue Info-Box:**
```html
<div class="info-box">
    <h4>📋 Titel</h4>
    <p>Inhalt...</p>
</div>
```

**Neue Warning-Box:**
```html
<div class="warning-box">
    <h4>⚠ Wichtig</h4>
    <p>Warnung...</p>
</div>
```

**Neue Success-Box:**
```html
<div class="success-box">
    <h4>✓ Erfolg</h4>
    <p>Positive Nachricht...</p>
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

**Neues Akkordeon:**
```html
<div class="accordion">
    <div class="accordion-item">
        <div class="accordion-header" onclick="toggleAccordion(this)">
            <strong>Titel</strong>
            <span class="accordion-icon">▼</span>
        </div>
        <div class="accordion-content">
            <p>Inhalt...</p>
        </div>
    </div>
</div>
```

### Typography Quick-Reference

```css
/* Überschriften */
h1 { font-size: 60px; line-height: 1.2em; }  /* XL */
h2 { font-size: 36px; line-height: 1.2em; }  /* XL */
h3 { font-size: 24px; line-height: 1.2em; }  /* XL */

/* Links */
a {
    color: #2A64B0;
    text-decoration: underline;
}
a:hover {
    color: #282828;
}

/* Überschriften-Links */
h1 a, h2 a, h3 a {
    color: inherit;
}
h1 a:hover, h2 a:hover, h3 a:hover {
    color: #2A64B0;
}
```

### Git-Befehle Cheat Sheet

```bash
# Status
git status

# Änderungen anzeigen
git diff

# Stagen
git add .

# Commit
git commit -m "type: Beschreibung"

# Push
git push origin main

# Log
git log --oneline -10

# Zurücksetzen
git checkout HEAD -- datei.html
```

---

**Version:** 2.0
**Erstellt:** 2025-10-21
**Nächste Review:** 2026-01-21

---

*Dieses Dokument konsolidiert alle Vorgaben für Design, Entwicklung und Inhalt. Bei Änderungen bitte Versionsnummer erhöhen und Changelog aktualisieren.*
