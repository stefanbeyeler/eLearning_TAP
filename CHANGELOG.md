# Changelog - eLearning TAP

Alle wichtigen Änderungen am eLearning TAP Projekt werden in dieser Datei dokumentiert.

Das Format basiert auf [Keep a Changelog](https://keepachangelog.com/de/1.0.0/),
und das Projekt folgt [Semantic Versioning](https://semver.org/lang/de/).

---

## [1.3.0] - 2025-10-26

### ✨ Hinzugefügt

#### Metadaten-Unterstützung
- **Anpassbare Titel und Untertitel:**
  - `ELEARNING_TITEL:` in content/content.md definierbar
  - `ELEARNING_UNTERTITEL:` in content/content.md definierbar
  - Automatische Verwendung in HTML `<title>`, `<h1>` und Untertitel
  - Standardwerte, falls nicht definiert

- **Build-Script Erweiterungen:**
  - `parse_metadata()` Funktion in build_html.py
  - Unterstützt normale und escaped Unterstriche
  - Stoppt bei `---` Separator (verhindert Überschreibung durch Dokumentations-Beispiele)
  - Console-Ausgabe zeigt erkannte Metadaten

### 📝 Dokumentation
- README.md aktualisiert mit Metadaten-Informationen
- scripts/README.md erweitert um Metadaten-Parsing
- CONTENT_WORKFLOW.md v1.1 mit Metadaten-Konfiguration
- content/content.md mit Metadaten-Dokumentation und Beispielen

### 🔄 Geändert
- `generate_html()` benötigt jetzt `metadata` Parameter
- HTML-Template verwendet Platzhalter `{{TITLE}}` und `{{SUBTITLE}}`
- Projekt-Version auf 1.3 erhöht

---

## [1.2.0] - 2025-10-25

### ✨ Hinzugefügt
- Content-Workflow eingeführt (content.md + CONTENT_WORKFLOW.md)
- Markdown-basierte Content-Verwaltung
- Automatische HTML-Konvertierung durch build_html.py
- Projekt-Struktur erweitert und dokumentiert

### 📝 Dokumentation
- CONTENT_WORKFLOW.md erstellt
- README.md, DEVELOPMENT.md, GUIDELINES.md aktualisiert

---

## [1.1.0] - 2025-10-21

### ✨ Hinzugefügt

#### Typography-System (GUIDELINES.md konform)
- **Schriftarten implementiert:**
  - DTL Documenta WT Bold für h1, h2, h3
  - Typ 1451 LL für Body, p, h4, h5, h6, li, td, th
  - Fallback-Schriften beibehalten

- **Responsive Heading-Größen (4 Breakpoints):**
  - **XL (>1440px):** h1: 60px, h2: 36px, h3: 24px
  - **LG (1025-1440px):** h1: 48px, h2: 28px, h3: 24px
  - **SM (431-1024px):** h1: 36px, h2: 24px, h3: 21px
  - **XS (<430px):** h1: 28px, h2: 21px, h3: 21px

- **h4, h5, h6 Definitionen:**
  - h4: 18px, line-height: 1.4em, letter-spacing: 2px
  - h5: 20px, line-height: 1.5em
  - h6: 14px, line-height: 1.3em, letter-spacing: 2px

#### Link-Styling
- **Standard-Links:**
  - Farbe: #2A64B0 (Blau)
  - Hover: #282828 (Dunkelgrau)
  - Text-decoration: underline
  - Transition: 0.3s ease

- **Überschriften-Links (h1-h3):**
  - Farbe: inherit (erbt von Überschrift)
  - Hover: #2A64B0
  - Text-decoration: underline beibehalten

#### JavaScript-Funktionen
- **Reset-Funktion (`resetTraining()`):**
  - Deselektiert alle Radio-Buttons
  - Blendet alle Quiz-Feedbacks aus
  - Setzt alle Quiz-Ergebnisse zurück
  - Navigiert zu Kapitel 1
  - Zeigt Bestätigungsdialog vor Reset
  - Zeigt Erfolgsmeldung nach Reset

- **Reset-Button im Header:**
  - Grauer Button (🔄 Schulung zurücksetzen)
  - Immer sichtbar für einfachen Zugriff

### 🔄 Geändert

#### Button-Styling (GUIDELINES.md konform)
- **Navigation-Buttons (.nav-btn):**
  - Padding: 10px 20px → **12px 24px**
  - Border-radius: 5px → **8px**
  - Font-weight: **600** hinzugefügt
  - Hover-Effekt: translateY(-2px) beibehalten

#### Responsive Design
- **Erweiterte Breakpoints:**
  - Von 1 Breakpoint (768px) auf 4 Breakpoints erweitert
  - Bessere Darstellung auf XL-Screens (>1440px)
  - Optimierte Typography für mittlere Viewports (431-1024px)
  - Verbesserte Mobile-Ansicht (<430px)

### 📝 Dokumentation
- AUDIT_REPORT.md erstellt
- GUIDELINES.md konsolidiert (v2.0)
- README.md aktualisiert

---

## [1.0.0] - 2025-10-21

### ✨ Initial Release

#### Kapitel-Struktur
- 8 Kapitel implementiert:
  1. Einführung
  2. Ambulante Behandlung
  3. LKAAT
  4. TARDOC
  5. Ambulante Pauschalen
  6. Vergleich
  7. Praxisanwendung
  8. Abschlusstest

#### Funktionen
- Kapitel-Navigation mit Progress-Bar
- Quiz-System mit Feedback
- Akkordeon-Komponenten
- Info-Boxen (Standard, Warning, Success)
- Responsive Design (Basis)

#### Technische Features
- Single-File HTML-Anwendung
- Embedded CSS und JavaScript
- Keine externen Abhängigkeiten
- Base64-encoded Bilder
- Cross-Browser kompatibel

---

## Vergleich: v1.0.0 → v1.3.0

| Feature | v1.0.0 | v1.3.0 | Status |
|---------|--------|--------|--------|
| **Typography** | Segoe UI (universell) | DTL Documenta WT (h1-h3)<br>Typ 1451 LL (Body) | ✅ Verbessert |
| **Breakpoints** | 1 (768px) | 4 (XL, LG, SM, XS) | ✅ Verbessert |
| **Link-Farben** | Default Browser | #2A64B0 / #282828 | ✅ Neu |
| **Reset-Funktion** | ❌ Nicht vorhanden | ✅ Implementiert | ✅ Neu |
| **Button-Styling** | Basis | GUIDELINES.md konform | ✅ Verbessert |
| **h4-h6** | Undefiniert | Vollständig definiert | ✅ Neu |
| **Content-Management** | Direktes HTML | Markdown-basiert (content.md) | ✅ Neu |
| **Metadaten** | Hardcodiert | Konfigurierbar via content.md | ✅ Neu |
| **Build-Process** | Manuell | Automatisiert (build_html.py) | ✅ Neu |

---

## GUIDELINES.md Konformität

### Version 1.0.0
- **Gesamt-Konformität:** 77% ⚠️
- **Kritische Mängel:** Typography-System, Responsive Design

### Version 1.1.0
- **Gesamt-Konformität:** 95% ✅
- **Alle kritischen Punkte behoben**
- **Verbleibende Nice-to-haves:** Naming-Konventionen (optional)

### Version 1.2.0 - 1.3.0
- **Content-Management:** Vollständig auf Markdown umgestellt
- **Metadaten:** Flexibles Konfigurationssystem
- **Dokumentation:** Umfassend aktualisiert

---

## Geplante Änderungen (Roadmap)

### Version 1.4.0 (Optional)
- [ ] Naming-Konventionen vereinheitlichen
  - `.info-box.warning` → `.warning-box`
  - `.info-box.success` → `.success-box`
  - `.progress-bar > .progress-fill` → `.progress-container > .progress-bar`
- [ ] Weitere Metadaten (Autor, Version, Datum in content.md)
- [ ] Automatische Generierung von Kapitel-Buttons aus Metadaten

### Version 2.0.0 (Zukunft)
- [ ] Neue Kapitel hinzufügen (z.B. FAQ, Übungsaufgaben)
- [ ] Erweiterte interaktive Elemente (Drag & Drop)
- [ ] Zertifikat-Download nach Abschlusstest
- [ ] Mehrsprachigkeit (DE, FR, IT)
- [ ] Fortschritts-Tracking (LocalStorage)

---

**Hinweis:** Diese Datei wird bei jeder Änderung aktualisiert. Bei Major-Updates bitte Versionsnummer in der HTML-Datei (Kommentar im `<head>`) anpassen.
