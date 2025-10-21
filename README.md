# eLearning TAP

Interaktive HTML-Schulungsunterlagen für das ambulante Tarifsystem der Schweiz (TARDOC, LKAAT, Ambulante Pauschalen)

## 📋 Projekt-Übersicht

Dieses Projekt enthält Single-File HTML-Schulungsunterlagen für medizinisches Personal, Verwaltungsmitarbeitende und Codierer/innen in Schweizer Spitälern.

### Hauptkomponenten
- **LKAAT** - Leistungskatalog ambulanter Behandlungen und Abklärungen
- **TARDOC** - Einzelleistungstarif für ambulante ärztliche Behandlungen
- **Ambulante Pauschalen** - Pauschaliertes Abrechnungssystem

## 📁 Projekt-Struktur

```
eLearning_TAP/
├── README.md                                      # Diese Datei
├── GUIDELINES.md                                  # ⭐ Haupt-Vorgabedatei (Design, Entwicklung, Content)
├── DEVELOPMENT.md                                 # Entwicklungsdokumentation (veraltet, siehe GUIDELINES.md)
├── PROMPT-Schulungsunterlage-Vorgaben.md         # KI-Prompt-Vorgaben (veraltet, siehe GUIDELINES.md)
├── ambulantes-tarifsystem-schulung-komplett.html # Hauptschulungsunterlage
└── Vorgaben/                                      # Referenzmaterialien
    ├── Typography-Fonts.pdf
    ├── Typography-Headings.pdf
    ├── Typography-Hyperlinks.pdf
    └── *.pdf (weitere Vorgabedokumente)
```

## 🚀 Quick Start

### Für Entwickler

1. **Neue Inhalte hinzufügen:**
   - Öffne [GUIDELINES.md](GUIDELINES.md)
   - Folge dem Abschnitt "Entwicklungsworkflow"
   - Bearbeite `ambulantes-tarifsystem-schulung-komplett.html`

2. **Design-Anpassungen:**
   - Siehe [GUIDELINES.md](GUIDELINES.md) → "Typography-System" und "Design-System"
   - Alle Farben, Schriftarten und Komponenten sind dort dokumentiert

3. **Testing:**
   - Verwende die Test-Checkliste in [GUIDELINES.md](GUIDELINES.md)
   - Öffne HTML-Datei direkt im Browser

### Für Content-Ersteller

- Alle inhaltlichen Vorgaben und Kapitel-Strukturen: [GUIDELINES.md](GUIDELINES.md) → "Content-Struktur"
- Quiz-Erstellung: [GUIDELINES.md](GUIDELINES.md) → "Interaktive Komponenten"

## 📖 Dokumentation

### Haupt-Dokumentation
- **[GUIDELINES.md](GUIDELINES.md)** - Konsolidierte Vorgaben für Design, Entwicklung und Inhalt
  - Typography-System (Schriftarten, Größen, Hierarchie)
  - Design-System (Farben, Layout, Komponenten)
  - Technische Architektur
  - Content-Struktur und Kapitel-Vorgaben
  - Interaktive Komponenten (Quiz, Akkordeon, Navigation)
  - Entwicklungsworkflow
  - Testing & Deployment

### Ergänzende Dokumentation (veraltet - siehe GUIDELINES.md)
- [DEVELOPMENT.md](DEVELOPMENT.md) - Entwicklungsdokumentation
- [PROMPT-Schulungsunterlage-Vorgaben.md](PROMPT-Schulungsunterlage-Vorgaben.md) - KI-Prompt-Vorgaben

## 🎨 Design-System

**Schriftarten:**
- Überschriften (h1-h3): DTL Documenta WT Bold
- Body & h4-h6: Typ 1451 LL

**Farben:**
- Primär: #667eea (Blau-Violett)
- Sekundär: #764ba2 (Violett)
- Links: #2A64B0 (Blau)
- Links Hover: #282828 (Dunkelgrau)

Details: [GUIDELINES.md](GUIDELINES.md) → "Typography-System" und "Design-System"

## 🛠 Technologie

- **Format:** Single-File HTML5
- **CSS:** Embedded (keine externen Stylesheets)
- **JavaScript:** Embedded (ES6+, keine externen Libraries)
- **Deployment:** Funktioniert offline, im Intranet, keine Build-Tools nötig

## 🧪 Testing

Vor Deployment:
```bash
# HTML-Datei im Browser öffnen
open ambulantes-tarifsystem-schulung-komplett.html

# Test-Checkliste durchgehen (siehe GUIDELINES.md)
```

## 🚀 Deployment

```bash
# Version erstellen
cp ambulantes-tarifsystem-schulung-komplett.html \
   ambulantes-tarifsystem-schulung-v1.0.html

# Upload zu Intranet-Server
# Details: GUIDELINES.md → "Deployment & Wartung"
```

## 📞 Support

- Bei Fragen zur Entwicklung: [GUIDELINES.md](GUIDELINES.md)
- Bei technischen Problemen: [GUIDELINES.md](GUIDELINES.md) → "Testing & Qualitätssicherung"
- Für Content-Updates: [GUIDELINES.md](GUIDELINES.md) → "Content-Struktur"

## 📝 Version

- **Aktuelle Version:** 1.0
- **Letzte Aktualisierung:** 2025-10-21
- **Versionierung:** MAJOR.MINOR.PATCH

## 📄 Lizenz

Interne Verwendung - Schweizer Spitäler
