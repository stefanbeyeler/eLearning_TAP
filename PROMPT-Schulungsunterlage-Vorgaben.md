# Prompt-Vorgaben: Interaktive Schulungsunterlagen für das Ambulante Tarifsystem

## 📋 Zweck und Zielsetzung

Erstelle eine vollständige, interaktive HTML-Schulungsunterlage zum Thema "Ambulantes Gesamt-Tarifsystem - Basiswissen für Anwender:innen", die im Intranet aufgeschaltet werden kann.

### Hauptziele:
- Vermittlung von Basiswissen zum ambulanten Tarifsystem (LKAAT, TARDOC, Ambulante Pauschalen)
- Interaktive Lernelemente mit sofortigem Feedback
- Professionelles, ansprechendes Design
- Vollständig selbstständige HTML-Datei (keine externen Abhängigkeiten)
- Mobile-responsive Darstellung
- Intuitive Navigation zwischen Kapiteln
- Integrierte Wissensüberprüfung nach jedem Kapitel

---

## 🏗️ Technische Grundstruktur

### Dateiformat:
- **Single-Page HTML-Anwendung** mit embedded CSS und JavaScript
- Alle Ressourcen inline (keine externen Dateien)
- UTF-8 Encoding
- Kompatibel mit modernen Browsern (Chrome, Firefox, Safari, Edge)

### Struktur-Template:

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Schulungstitel</title>
    <style>
        /* Alle CSS-Styles hier */
    </style>
</head>
<body>
    <div class="container">
        <header>
            <!-- Titel, Untertitel, Fortschrittsbalken -->
        </header>
        
        <nav>
            <!-- Kapitel-Navigation -->
        </nav>
        
        <div class="content">
            <!-- Kapitel-Inhalte -->
        </div>
    </div>
    
    <script>
        /* Alle JavaScript-Funktionen hier */
    </script>
</body>
</html>
```

---

## 🎨 Design-Vorgaben

### Farbschema:
- **Primärfarbe**: `#667eea` (Blau-Violett)
- **Sekundärfarbe**: `#764ba2` (Violett)
- **Hintergrund**: Gradient von `#667eea` nach `#764ba2`
- **Content-Bereiche**: Weiß (`#ffffff`)
- **Text**: Dunkelgrau (`#333333`)
- **Erfolg**: Grün (`#28a745`)
- **Warnung**: Gelb (`#ffc107`)
- **Info**: Hellblau (`#e8f4f8`)

### Typografie:
- **Font-Family**: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif
- **Line-Height**: 1.6
- **H1**: 2.5em
- **H2**: 2em
- **H3**: 1.5em
- **Body**: 1em

### Layout-Komponenten:

#### Container
```css
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}
```

#### Header
- Weiß mit Schatten
- Zentrierter Text
- Border-radius: 15px
- Enthält: Titel, Untertitel, Fortschrittsbalken

#### Navigation
- Horizontale Button-Leiste
- Responsive (Wrap bei kleinen Screens)
- Active-State hervorgehoben
- Hover-Effekte

#### Content-Boxen (Info-Boxen)
- **Standard** (blau): Informationen
- **Warning** (gelb): Warnungen/Wichtige Hinweise
- **Success** (grün): Erfolge/Bestätigungen
- Border-left: 5px solid (entsprechende Farbe)

---

## 📚 Kapitel-Struktur

### Aktuelle Kapitel-Übersicht:

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

### Standard-Kapitel-Template:

```html
<div class="chapter" id="chapter{N}">
    <h2>Kapitel {N+1}: {Titel}</h2>
    
    <!-- Einleitung -->
    <h3>Unterkapitel-Titel</h3>
    <p>Einleitungstext...</p>
    
    <!-- Info-Boxen -->
    <div class="info-box">
        <h4>📋 Titel der Box</h4>
        <ul class="list-styled">
            <li>Punkt 1</li>
            <li>Punkt 2</li>
        </ul>
    </div>
    
    <!-- Akkordeon für erweiterte Inhalte -->
    <div class="accordion">
        <div class="accordion-item">
            <div class="accordion-header" onclick="toggleAccordion(this)">
                <strong>Titel</strong>
            </div>
            <div class="accordion-content">
                <p>Inhalt...</p>
            </div>
        </div>
    </div>
    
    <!-- Tabellen -->
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
    
    <!-- Quiz-Sektion -->
    <div class="quiz-section">
        <h3>Verständnisfragen Kapitel {N+1}</h3>
        
        <div class="quiz-question" data-chapter="{N+1}" data-question="1">
            <h4>Frage 1: Fragetext?</h4>
            <div class="quiz-options">
                <label class="quiz-option">
                    <input type="radio" name="q{N+1}_1" value="a">
                    Antwort A
                </label>
                <!-- weitere Optionen -->
            </div>
            <div class="quiz-feedback"></div>
        </div>
        
        <button class="submit-quiz" onclick="checkChapterQuiz({N+1})">
            Antworten überprüfen
        </button>
        <div class="quiz-result" id="result-chapter{N+1}"></div>
    </div>
    
    <!-- Navigation -->
    <div class="navigation-footer">
        <button class="nav-footer-btn" onclick="showChapter({N-1})">◄ Vorheriges</button>
        <button class="nav-footer-btn" onclick="showChapter({N+1})">Nächstes ►</button>
    </div>
</div>
```

---

## 📝 Inhaltliche Vorgaben pro Kapitel

### Kapitel 1: Einführung
**Lernziele:**
- Überblick über das Gesamt-Tarifsystem geben
- Die drei Komponenten (LKAAT, TARDOC, Pauschalen) vorstellen
- Notwendigkeit und Vorteile erklären

**Inhalte:**
1. Was ist das ambulante Gesamt-Tarifsystem?
2. Komponenten des Systems
3. Warum verschiedene Komponenten?
4. Lernziele des Moduls

**Quiz:** 2 Fragen (Multiple Choice)

---

### Kapitel 2: Ambulante Behandlung
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

### Kapitel 3: LKAAT
**Lernziele:**
- Funktion des LKAAT verstehen
- Leistungstypen unterscheiden können
- Triggerpositionen erkennen

**Inhalte:**
1. Was ist der LKAAT?
2. Struktur und Aufbau (Tabelle mit Typen E, EZ, P, PZ)
3. Entscheidung TARDOC vs. Pauschale (Akkordeon mit 3 Schritten)
4. LKN-Nummern verstehen (8-stellig vs 9-stellig)
5. Triggerpositionen - Das Herzstück des Systems
6. Praktisches Beispiel (Fallbeispiel: Zwei Behandlungen)
7. Tools für die Arbeit mit dem LKAAT
8. Häufige Fehler beim LKAAT

**Quiz:** 4 Fragen

---

### Kapitel 4: TARDOC
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

### Kapitel 5: Ambulante Pauschalen
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

### Kapitel 6: Vergleich
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

### Kapitel 7: Praxisanwendung
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

### Abschlusstest
**Format:** 12 Multiple-Choice-Fragen aus allen Kapiteln
**Bestehensgrenze:** 10 von 12 richtigen Antworten (83%)
**Feedback:** Detailliertes Ergebnis mit Bestanden/Nicht bestanden

---

## ⚙️ Interaktive Funktionen

### JavaScript-Funktionen (erforderlich):

```javascript
// Globale Variablen
let currentChapter = 0;
const totalChapters = 8;

// Funktionen
function showChapter(index) {
    // Kapitel anzeigen, Navigation updaten, Progress updaten
}

function updateProgress() {
    // Fortschrittsbalken aktualisieren
}

function toggleAccordion(header) {
    // Akkordeon auf-/zuklappen
}

function checkChapterQuiz(chapter) {
    // Quiz auswerten, Feedback anzeigen
}

function checkFinalQuiz() {
    // Abschlusstest auswerten
}

function resetTraining() {
    // Schulung neu starten
}
```

### Quiz-System:

**Antworten-Objekt:**
```javascript
const answers = {
    1: { 1: 'c', 2: 'c' },
    2: { 1: 'b', 2: 'b', 3: 'b', 4: 'b' },
    // ... für alle Kapitel
    final: { 1: 'b', 2: 'b', /* ... */ 12: 'b' }
};
```

**Feedback-Objekt:**
```javascript
const feedbackTexts = {
    1: {
        1: {
            correct: "Richtig! Erklärung...",
            incorrect: "Falsch. Korrektur..."
        },
        // ... für alle Fragen
    },
    // ... für alle Kapitel
};
```

### Fortschrittsbalken:
- Zeigt aktuellen Fortschritt als Prozentsatz
- Berechnung: `(currentChapter + 1) / totalChapters * 100`
- Visuelles Feedback durch farbigen Balken

### Akkordeon-Elemente:
- Click auf Header öffnet/schließt Content
- Visual Indicator (Pfeil dreht sich)
- Smooth Transition

---

## 🎯 Quiz-Anforderungen

### Pro Kapitel-Quiz:
- **Anzahl Fragen:** 2-4 Fragen (je nach Komplexität)
- **Format:** Multiple Choice (4 Optionen)
- **Feedback:** Sofort nach Klick auf "Antworten überprüfen"
- **Bewertung:** Anzeige von Anzahl richtig/gesamt und Prozent
- **Empfehlung:** Bei <66% Kapitel wiederholen

### Abschlusstest:
- **Anzahl Fragen:** 12 Fragen
- **Bestehensgrenze:** 10 von 12 (83%)
- **Feedback:** 
  - Bestanden: Grüne Box mit Glückwunsch
  - Nicht bestanden: Rote Box mit Empfehlung zur Wiederholung

### Quiz-Feedback-Gestaltung:
```html
<!-- Richtig -->
<div class="quiz-feedback correct">
    ✓ Richtig! Erklärung warum die Antwort korrekt ist.
</div>

<!-- Falsch -->
<div class="quiz-feedback incorrect">
    ✗ Falsch. Erklärung der richtigen Antwort.
</div>
```

---

## 📱 Responsive Design

### Breakpoints:
```css
@media (max-width: 768px) {
    h1 { font-size: 1.8em; }
    .content { padding: 20px; }
    .nav-buttons { flex-direction: column; }
}
```

### Mobile Optimierungen:
- Kleinere Schriftgrößen
- Gestapelte statt horizontale Navigation
- Touch-optimierte Button-Größen
- Reduzierte Padding-Werte

---

## 🔄 Erweiterungsmöglichkeiten

### Neue Kapitel hinzufügen:

**Schritt 1:** Navigation erweitern
```html
<button class="nav-btn" onclick="showChapter({N})">
    Kapitel {N+1}: {Titel}
</button>
```

**Schritt 2:** Kapitel-HTML erstellen (siehe Template oben)

**Schritt 3:** JavaScript anpassen
```javascript
const totalChapters = {neue_anzahl};

// Quiz-Antworten hinzufügen
const answers = {
    // ...
    {N}: { 1: 'a', 2: 'b', /* ... */ },
};

// Feedback-Texte hinzufügen
const feedbackTexts = {
    // ...
    {N}: {
        1: {
            correct: "...",
            incorrect: "..."
        },
    },
};
```

### Neue interaktive Elemente:

**Klickbare Tabs:**
```html
<div class="tabs">
    <div class="tab-header">
        <button onclick="showTab(1)">Tab 1</button>
        <button onclick="showTab(2)">Tab 2</button>
    </div>
    <div class="tab-content" id="tab1">Inhalt 1</div>
    <div class="tab-content" id="tab2">Inhalt 2</div>
</div>
```

**Tooltips:**
```html
<span class="tooltip">
    Hover-Text
    <span class="tooltip-text">Erklärung</span>
</span>
```

**Drag & Drop Übungen:**
```html
<div class="drag-drop-exercise">
    <div class="draggable" draggable="true">Element</div>
    <div class="drop-zone">Ziel</div>
</div>
```

### Weitere Content-Typen:

**Videos (Base64 embedded):**
```html
<video controls>
    <source src="data:video/mp4;base64,{BASE64_DATA}" type="video/mp4">
</video>
```

**Bilder (Base64 embedded):**
```html
<img src="data:image/png;base64,{BASE64_DATA}" alt="Beschreibung">
```

**Interaktive Diagramme:**
- Verwendung von Canvas/SVG
- JavaScript zur Darstellung
- Keine externen Bibliotheken (alles inline)

---

## 📋 Checkliste für neue Kapitel

- [ ] Lernziele definiert
- [ ] Inhaltsstruktur erstellt (H2, H3-Hierarchie)
- [ ] Info-Boxen eingefügt (min. 1-2 pro Kapitel)
- [ ] Akkordeon für erweiterte Inhalte (optional)
- [ ] Tabellen für Vergleiche (wenn sinnvoll)
- [ ] Praktische Beispiele/Fallbeispiele (min. 1)
- [ ] Quiz-Fragen erstellt (2-4 Fragen)
- [ ] Quiz-Antworten in JavaScript definiert
- [ ] Feedback-Texte für richtig/falsch erstellt
- [ ] Navigation (Vor/Zurück) angepasst
- [ ] Navigation-Button in Header hinzugefügt
- [ ] `totalChapters` erhöht
- [ ] Mobile-Ansicht getestet

---

## 🎨 Style-Guide für Content-Elemente

### Überschriften:
- **H2**: Kapitel-Titel (blau, underline)
- **H3**: Hauptthemen innerhalb Kapitel (violett)
- **H4**: Nur in Info-Boxen oder Quiz

### Listen:
- Verwende `<ul class="list-styled">` für besseres Styling
- Jeder Listenpunkt sollte aussagekräftig sein
- Bei längeren Listen: Akkordeon verwenden

### Hervorhebungen:
- **Wichtige Begriffe**: `<span class="highlight">`
- **Fachbegriffe beim ersten Auftreten**: Fett markieren
- **Warnungen**: Warning Info-Box
- **Erfolge**: Success Info-Box

### Code-Beispiele:
```html
<div class="code-example">
    AA.00.0010 - Ärztliche Konsultation, erste 5 Min.
</div>
```

---

## 💾 Exportformat-Anforderungen

### Dateiname:
`{thema}-schulung-{version}.html`

Beispiel: `ambulantes-tarifsystem-schulung-v2.html`

### Dateigröße:
- Ziel: < 500 KB (ohne eingebettete Medien)
- Mit Bildern: < 2 MB
- Bei Überschreitung: Bilder komprimieren

### Validierung:
- HTML5-konform
- CSS3-konform
- JavaScript ES6+ (mit Fallbacks für ältere Browser)
- Keine Konsolenfehler
- Funktionierende Links (keine broken links)

---

## 🚀 Deployment-Hinweise

### Intranet-Anforderungen:
- Keine externen Ressourcen (CDN, externe Scripts)
- Keine Server-seitige Funktionalität erforderlich
- Funktioniert direkt beim Öffnen der HTML-Datei
- Cross-Browser kompatibel

### Testing-Checkliste:
- [ ] Alle Kapitel aufrufbar
- [ ] Navigation funktioniert vorwärts/rückwärts
- [ ] Quiz-Auswertung korrekt
- [ ] Fortschrittsbalken aktualisiert sich
- [ ] Akkordeons öffnen/schließen
- [ ] Responsive auf Tablet (768px)
- [ ] Responsive auf Mobile (375px)
- [ ] Keine JavaScript-Errors in Console
- [ ] Alle Bilder werden angezeigt
- [ ] Druckansicht sinnvoll

---

## 📊 Metriken und Erfolg

### Lernziele-Tracking:
Nach Abschluss sollten Lernende:
- ✅ Die Komponenten des Tarifsystems benennen können
- ✅ LKAAT-Nummern interpretieren können
- ✅ Triggerpositionen erkennen können
- ✅ Das richtige System (TARDOC/Pauschale) wählen können
- ✅ Häufige Fehler vermeiden können

### Erfolgsmetriken:
- **Bestehensquote Abschlusstest**: Ziel >80%
- **Durchschnittliche Bearbeitungszeit**: 45-60 Minuten
- **Quiz-Erfolgsrate pro Kapitel**: Ziel >70%

---

## 🔧 Wartung und Updates

### Versionierung:
- **Major Update** (v2.0): Neue Kapitel, große Strukturänderungen
- **Minor Update** (v1.1): Inhaltliche Ergänzungen, neue Quiz-Fragen
- **Patch** (v1.0.1): Bugfixes, Typos, kleine Anpassungen

### Changelog-Template:
```markdown
## Version X.Y.Z - YYYY-MM-DD

### Neu
- [Feature] Neues Kapitel X hinzugefügt
- [Content] Erweiterte Beispiele in Kapitel Y

### Geändert
- [Content] Aktualisierte Tabelle in Kapitel Z
- [Design] Verbesserte Mobile-Ansicht

### Behoben
- [Bug] Quiz-Auswertung Kapitel A korrigiert
- [Typo] Rechtschreibfehler in Kapitel B
```

---

## 📚 Ressourcen und Referenzen

### Inhaltliche Quellen:
- Offizielle TARDOC-Dokumentation
- LKAAT-Katalog (Ärztekasse/FMH)
- Ambulante Pauschalen-Handbuch
- SwissDRG-Dokumentation (für Vergleiche)

### Design-Inspirationen:
- Material Design Guidelines
- Bootstrap-Komponenten (Akkordeon, Buttons)
- Moderne E-Learning-Plattformen

### JavaScript-Patterns:
- Single Page Application (SPA)
- Progressive Enhancement
- Mobile First Approach

---

## 🎓 Best Practices

### Content:
1. **Klare Sprache**: Fachbegriffe erklären
2. **Struktur**: Vom Allgemeinen zum Speziellen
3. **Beispiele**: Mindestens ein Praxisbeispiel pro Kapitel
4. **Wiederholung**: Kernkonzepte mehrfach aufgreifen
5. **Visualisierung**: Tabellen und Boxen zur Übersichtlichkeit

### Didaktik:
1. **Lernziele** klar kommunizieren
2. **Aktivierung**: Quiz und interaktive Elemente
3. **Feedback**: Sofortiges, konstruktives Feedback
4. **Progression**: Aufbauende Kapitel-Struktur
5. **Zusammenfassung**: Am Ende jedes Kapitels

### Technik:
1. **Performance**: Minimale Ladezeit (<2s)
2. **Accessibility**: ARIA-Labels, Keyboard-Navigation
3. **Fehlerbehandlung**: Graceful Degradation
4. **Kompatibilität**: Cross-Browser Testing
5. **Sicherheit**: Keine user inputs, reine Client-Side App

---

## 📝 Template für neue Kapitel (Quick Start)

```markdown
### Kapitel {N}: {Titel}

**Lernziele:**
- Ziel 1
- Ziel 2
- Ziel 3

**Inhaltsstruktur:**
1. Einleitung: Was ist {Thema}?
2. Hauptteil:
   - Punkt A (mit Info-Box)
   - Punkt B (mit Tabelle/Akkordeon)
   - Punkt C
3. Praktisches Beispiel (Fallbeispiel)
4. Häufige Fehler / Best Practices
5. Zusammenfassung (optional)

**Quiz:**
- Frage 1: [Schwierigkeit: Leicht]
- Frage 2: [Schwierigkeit: Mittel]
- Frage 3: [Schwierigkeit: Schwer]
- (Optional) Frage 4

**Geschätzte Bearbeitungszeit:** X Minuten
```

---

## 🎯 Nächste Schritte für Erweiterungen

### Priorität 1 (Quick Wins):
- [ ] Zusätzliche Fallbeispiele in bestehenden Kapiteln
- [ ] Erweiterte Quiz-Fragen für Abschlusstest
- [ ] Glossar mit Fachbegriffen (neues Kapitel oder Sidebar)

### Priorität 2 (Mittel):
- [ ] Kapitel 8: Häufig gestellte Fragen (FAQ)
- [ ] Kapitel 9: Übungsaufgaben mit Musterlösungen
- [ ] Downloadbare Checklisten (als Base64-PDF)

### Priorität 3 (Langfristig):
- [ ] Interaktive Codierungs-Übungen (Drag & Drop)
- [ ] Video-Tutorials (embedded als Base64)
- [ ] Zertifikat nach erfolgreichem Abschluss (PDF-Generator)
- [ ] Mehrsprachigkeit (DE, FR, IT)

---

## 📧 Kontakt und Support

Bei Fragen oder Problemen zu dieser Prompt-Datei:
- Dokumentation durchlesen
- Bestehendes Kapitel als Vorlage verwenden
- Schrittweise vorgehen (erst HTML, dann Styling, dann JavaScript)

---

**Letzte Aktualisierung:** 2025-10-21  
**Version Prompt-File:** 1.0  
**Kompatibel mit:** Schulungsunterlage ambulantes-tarifsystem-schulung-komplett.html

---

*Diese Prompt-Datei kann beliebig erweitert und angepasst werden. Bei größeren Änderungen bitte Versionsnummer erhöhen.*
