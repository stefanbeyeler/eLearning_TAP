# eLearning TAP

Interaktive HTML-Schulungsunterlagen für das ambulante Tarifsystem der Schweiz (TARDOC, LKAAT, Ambulante Pauschalen)

## 📋 Projekt-Übersicht

Dieses Projekt enthält Single-File HTML-Schulungsunterlagen für medizinisches Personal, Verwaltungsmitarbeitende und Codierer/innen in Schweizer Spitälern.

### Hauptkomponenten
- **LKAAT** - Leistungskatalog ambulanter Behandlungen und Abklärungen
- **ICD-10-GM** - Diagnosecodierung (Internationale Klassifikation der Krankheiten)
- **TARDOC** - Einzelleistungstarif für ambulante ärztliche Behandlungen
- **Ambulante Pauschalen** - Pauschaliertes Abrechnungssystem

## 📁 Projekt-Struktur

```
eLearning_TAP/
├── README.md                                      # Diese Datei
├── GUIDELINES.md                                  # ⭐ Haupt-Vorgabedatei (Design, Entwicklung, Content)
├── DEVELOPMENT.md                                 # Entwicklungsdokumentation (technisch)
├── CONTENT_WORKFLOW.md                            # ⭐ NEU: Content-Workflow (MD → HTML)
├── content.md                                     # ⭐ NEU: Content-Quelle (Markdown, editierbar)
├── eLearning.html                                 # Hauptschulungsunterlage (generiert aus content.md)
├── ambulantes-tarifsystem-schulung-komplett.html # Legacy-Version (deprecated)
├── PROMPT-Schulungsunterlage-Vorgaben.md         # KI-Prompt-Vorgaben (veraltet, siehe GUIDELINES.md)
├── specification_documents/                       # Offizielle OAAT-Tarifdokumente
│   ├── 250430_AnhangC_Richtlinien_fuer_die_ambulante_Leistungserfassung.pdf
│   ├── 250430_AnhangH_Rechnungsstellung.pdf
│   ├── 20250214_FAQ_Gesamtsystem_final.pdf
│   └── *.pdf (weitere Vorgabedokumente)
└── Vorgaben/                                      # Design-Referenzmaterialien
    ├── Typography-Fonts.pdf
    ├── Typography-Headings.pdf
    ├── Typography-Hyperlinks.pdf
    └── *.pdf (weitere Vorgabedokumente)
```

## 🚀 Quick Start

### Für Content-Ersteller (⭐ Empfohlen)

**Neuer vereinfachter Workflow:**

1. **Inhalte bearbeiten:**
   - Öffne [content/content.md](content/content.md) in einem Texteditor
   - Bearbeite Texte, Info-Boxen, Quiz-Fragen in Markdown
   - Optional: Passe Titel und Untertitel mit `ELEARNING_TITEL:` und `ELEARNING_UNTERTITEL:` an
   - Speichern

2. **HTML aktualisieren:**
   - Beauftrage Claude: "Kapitel X in @content/content.md wurde geändert, bitte aktualisiere @eLearning.html"
   - Oder führe das Build-Script aus: `python3 scripts/build_html.py`
   - Markdown wird automatisch zu HTML konvertiert

3. **Testing:**
   - Öffne [eLearning.html](eLearning.html) im Browser

**Detaillierte Anleitung:** [CONTENT_WORKFLOW.md](CONTENT_WORKFLOW.md)

**Vorteile:**
- ✅ Einfache Markdown-Syntax (kein HTML nötig)
- ✅ Schnelle Content-Updates
- ✅ Automatische HTML-Konvertierung
- ✅ Konsistente Formatierung
- ✅ Anpassbare Titel und Untertitel via Metadaten

### Für Entwickler (Technische Änderungen)

1. **Design-Anpassungen:**
   - Siehe [GUIDELINES.md](GUIDELINES.md) → "Typography-System" und "Design-System"
   - Alle Farben, Schriftarten und Komponenten sind dort dokumentiert
   - Direkte Bearbeitung von [eLearning.html](eLearning.html)

2. **Neue Features entwickeln:**
   - Folge dem Abschnitt "Entwicklungsworkflow" in [DEVELOPMENT.md](DEVELOPMENT.md)
   - Bearbeite HTML, CSS oder JavaScript in [eLearning.html](eLearning.html)

3. **Testing:**
   - Verwende die Test-Checkliste in [GUIDELINES.md](GUIDELINES.md)
   - Öffne HTML-Datei direkt im Browser

## 📖 Dokumentation

### Haupt-Dokumentation
- **[CONTENT_WORKFLOW.md](CONTENT_WORKFLOW.md)** - ⭐ NEU: Content-Workflow (MD → HTML)
  - Anleitung zur Bearbeitung von [content.md](content.md)
  - Wie Claude die HTML-Konvertierung durchführt
  - Struktur-Konventionen und Markdown-Syntax
  - Praktische Beispiele und Troubleshooting

- **[GUIDELINES.md](GUIDELINES.md)** - Konsolidierte Vorgaben für Design, Entwicklung und Inhalt
  - Typography-System (Schriftarten, Größen, Hierarchie)
  - Design-System (Farben, Layout, Komponenten)
  - Technische Architektur
  - Content-Struktur und Kapitel-Vorgaben
  - Interaktive Komponenten (Quiz, Akkordeon, Navigation)
  - Entwicklungsworkflow
  - Testing & Deployment

- **[DEVELOPMENT.md](DEVELOPMENT.md)** - Technische Entwicklungsdokumentation
  - Entwicklungsworkflow (Content vs. Direkter HTML-Workflow)
  - Coding Standards
  - Testing & Qualitätssicherung
  - Deployment & Wartung
  - Troubleshooting

### Ergänzende Dokumentation
- [content/content.md](content/content.md) - Content-Quelle (Markdown, manuell editierbar)
  - Unterstützt Metadaten für Titel/Untertitel (`ELEARNING_TITEL:`, `ELEARNING_UNTERTITEL:`)
- [scripts/README.md](scripts/README.md) - Dokumentation der Build-Scripts
- [PROMPT-Schulungsunterlage-Vorgaben.md](PROMPT-Schulungsunterlage-Vorgaben.md) - KI-Prompt-Vorgaben (veraltet)

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
open eLearning.html

# Test-Checkliste durchgehen (siehe GUIDELINES.md)
```

## 🚀 Deployment

```bash
# Version erstellen
cp eLearning.html \
   eLearning-v1.1.html

# Upload zu Intranet-Server
# Details: GUIDELINES.md → "Deployment & Wartung"
```

## 📞 Support

- Bei Fragen zur Entwicklung: [GUIDELINES.md](GUIDELINES.md)
- Bei technischen Problemen: [GUIDELINES.md](GUIDELINES.md) → "Testing & Qualitätssicherung"
- Für Content-Updates: [GUIDELINES.md](GUIDELINES.md) → "Content-Struktur"

## 📝 Version

- **Aktuelle Version:** 1.3
- **Letzte Aktualisierung:** 2025-10-26
- **Versionierung:** MAJOR.MINOR.PATCH

### Changelog

**Version 1.3 (2025-10-26):**
- ✅ **NEU:** Metadaten-Unterstützung in content/content.md
- ✅ **NEU:** Anpassbare Titel und Untertitel via `ELEARNING_TITEL:` und `ELEARNING_UNTERTITEL:`
- ✅ Build-Script (build_html.py) erweitert für Metadaten-Parsing
- ✅ Dokumentation aktualisiert (README, scripts/README, CONTENT_WORKFLOW)

**Version 1.2 (2025-10-25):**
- ✅ **NEU:** Content-Workflow eingeführt (content.md + CONTENT_WORKFLOW.md)
- ✅ **NEU:** Markdown-basierte Content-Verwaltung
- ✅ Automatische HTML-Konvertierung durch Claude
- ✅ Projekt-Struktur erweitert und dokumentiert
- ✅ README.md, DEVELOPMENT.md, GUIDELINES.md aktualisiert

**Version 1.1 (2025-10-25):**
- ✅ Kapitel 4 "Diagnosen als ICD-10 Code" vollständig entwickelt
- ✅ Basiert auf offiziellen OAAT-Dokumenten (Anhang C, H, FAQ)
- ✅ 4 neue Quiz-Fragen zu ICD-10-GM Codierung
- ✅ Gesamtzahl der Kapitel: 9 (8 Inhaltskapitel + Abschlusstest)

**Version 1.0 (2025-10-21):**
- ✅ Initiale Version mit 3 vollständigen Kapiteln
- ✅ LKAAT, Ambulante Behandlung, Ambulante Pauschalen

## 📄 Lizenz

Interne Verwendung - Schweizer Spitäler
