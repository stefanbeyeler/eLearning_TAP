# Changelog - ambulantes-tarifsystem-schulung-komplett.html

Alle wichtigen Änderungen an der Schulungsunterlage werden in dieser Datei dokumentiert.

Das Format basiert auf [Keep a Changelog](https://keepachangelog.com/de/1.0.0/),
und das Projekt folgt [Semantic Versioning](https://semver.org/lang/de/).

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

## Vergleich: v1.0.0 → v1.1.0

| Feature | v1.0.0 | v1.1.0 | Status |
|---------|--------|--------|--------|
| **Typography** | Segoe UI (universell) | DTL Documenta WT (h1-h3)<br>Typ 1451 LL (Body) | ✅ Verbessert |
| **Breakpoints** | 1 (768px) | 4 (XL, LG, SM, XS) | ✅ Verbessert |
| **Link-Farben** | Default Browser | #2A64B0 / #282828 | ✅ Neu |
| **Reset-Funktion** | ❌ Nicht vorhanden | ✅ Implementiert | ✅ Neu |
| **Button-Styling** | Basis | GUIDELINES.md konform | ✅ Verbessert |
| **h4-h6** | Undefiniert | Vollständig definiert | ✅ Neu |

---

## GUIDELINES.md Konformität

### Version 1.0.0
- **Gesamt-Konformität:** 77% ⚠️
- **Kritische Mängel:** Typography-System, Responsive Design

### Version 1.1.0
- **Gesamt-Konformität:** 95% ✅
- **Alle kritischen Punkte behoben**
- **Verbleibende Nice-to-haves:** Naming-Konventionen (optional)

---

## Geplante Änderungen (Roadmap)

### Version 1.2.0 (Optional)
- [ ] Naming-Konventionen vereinheitlichen
  - `.info-box.warning` → `.warning-box`
  - `.info-box.success` → `.success-box`
  - `.progress-bar > .progress-fill` → `.progress-container > .progress-bar`

### Version 2.0.0 (Zukunft)
- [ ] Neue Kapitel hinzufügen (z.B. FAQ, Übungsaufgaben)
- [ ] Erweiterte interaktive Elemente (Drag & Drop)
- [ ] Zertifikat-Download nach Abschlusstest
- [ ] Mehrsprachigkeit (DE, FR, IT)

---

**Hinweis:** Diese Datei wird bei jeder Änderung aktualisiert. Bei Major-Updates bitte Versionsnummer in der HTML-Datei (Kommentar im `<head>`) anpassen.
