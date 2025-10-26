# eLearning - Content Source

**Version:** 1.3  
**Letzte Aktualisierung:** 2025-10-26  
**Zweck:** Diese Datei dient als zentrale Content-Quelle für eLearning.html

ELEARNING\_TITEL: Ambulantes Gesamt-Tarifsystem  
ELEARNING\_UNTERTITEL: Basiswissen für Anwender:innen

---

## Hinweise zur Nutzung

Diese Markdown-Datei enthält alle Inhalte der eLearning-Schulung in strukturierter Form. Du kannst diese Datei manuell bearbeiten, um Inhalte zu erweitern oder anzupassen. Claude kann dann die `eLearning.html` Datei basierend auf deinen Änderungen aktualisieren.

### Metadaten-Konfiguration:

Du kannst den Titel und Untertitel des eLearnings anpassen, indem du folgende Zeilen am Anfang der Datei hinzufügst:

```
ELEARNING_TITEL: Dein Titel hier
ELEARNING_UNTERTITEL: Dein Untertitel hier
```

**Beispiel:**

```
ELEARNING_TITEL: Ambulantes Gesamt-Tarifsystem
ELEARNING_UNTERTITEL: Basiswissen für Anwender:innen
```

Falls diese Zeilen nicht definiert sind, werden die oben genannten Standardwerte verwendet.

### Struktur-Konventionen:

*   **INFO-BOX**: Wird zu `<div class="info-box">` konvertiert
*   **INFO-BOX WARNUNG**: Wird zu `<div class="info-box warning">` konvertiert
*   **INFO-BOX SUCCESS**: Wird zu `<div class="info-box success">` konvertiert
*   **ACCORDION**: Wird zu `<div class="accordion">` konvertiert
*   **TABELLE**: Markdown-Tabellen werden zu HTML `<table>` konvertiert
*   **BILD**: Bilder mit optionaler Bildunterschrift einfügen
*   **QUIZ**: Quiz-Fragen mit Antwortoptionen (✓ markiert die korrekte Antwort)

### Bilder einfügen:

```
**BILD: pfad/bild.jpg**
Optional: Bildunterschrift hier einfügen

**BILD: images/beispiel.png**
Diese Bildunterschrift erscheint unter dem Bild in kursiv.
```

**Hinweise:**

*   Relative Pfade vom Standort der HTML-Datei
*   Unterstützte Formate: JPG, PNG, GIF, SVG, WebP
*   Bilder werden zentriert und responsiv dargestellt
*   Bildunterschrift ist optional (nächste Zeile nach BILD:)

---

## Vorwort

BUTTON: Vorwort  
TITEL: Vorwort

### Willkommen zur eLearning-Schulung

Herzlich willkommen zu dieser umfassenden Schulung zum ambulanten Gesamt-Tarifsystem der Schweiz. Diese Schulung wurde entwickelt, um dir ein fundiertes Verständnis der komplexen Strukturen und Prozesse des neuen ambulanten Tarifsystems zu vermitteln, welches per 1. Januar 2026 eingeführt wird.

**BILD: pictures/stairs.webp**  
Einzelleistung (TARDOC) oder ambulante Pauschale?

**INFO-BOX: Zielgruppe dieser Schulung**

*   Medizinisches Fachpersonal
*   Zentrums- und Klinikmanager:innen
*   Mitarbeitende im Leistungsmanagement, der Abrechnung und der Kodierung
*   Alle, die mit der ambulanten Leistungserfassung und -abrechnung befasst sind

### Aufbau und Struktur

Diese Schulung ist in 10 Kapitel gegliedert, die aufeinander aufbauen und dich Schritt für Schritt durch das Tarifsystem führen:

**Grundlagen (Kapitel 1-3)**

Du lernst zunächst die Komponenten des Systems kennen, verstest was ambulante Behandlungen sind und wie der LKAAT als zentrales Erfassungsinstrument funktioniert.

**Diagnosen und Abrechnungssysteme (Kapitel 4-6)**

Hier vertiefst du dein Wissen über die Diagnosecodierung mit ICD-10-GM, den TARDOC-Einzelleistungstarif und die Ambulanten Pauschalen.

**Vergleich und Praxis (Kapitel 7-8)**

Du lernst die Unterschiede zwischen TARDOC und Pauschalen kennen und erhälst praxisnahe Anleitungen für den Arbeitsalltag.

**Abschlusstest (Kapitel 9)**

Ein umfassender Test überprüft dein erworbenes Wissen über alle Kapitel hinweg.

**FAQ - Häufig gestellte Fragen**

Antworten auf die wichtigsten Fragen zu LKAAT, TARDOC, Ambulanten Pauschalen, ICD-10-GM, Praxisanwendung und Übergangsregelungen findest du hier.

### Wie du diese Schulung nutzen kannst

**INFO-BOX SUCCESS: Lernempfehlungen**

*   Arbeite die Kapitel nacheinander durch
*   Nutze die INFO-Boxen für wichtige Hinweise
*   Öffne die Accordion-Bereiche für zusätzliche Details
*   Bearbeite die Quiz-Fragen am Ende jedes Kapitels
*   Mache dir Notizen zu Unklarheiten
*   Nimm dir Zeit für den Abschlusstest

### Interaktive Elemente

In dieser Schulung findest du verschiedene didaktische Elemente:

**INFO-BOX: Verwendete Elemente**

*   **INFO-BOX:** Wichtige Informationen und Zusammenfassungen
*   **INFO-BOX WARNUNG:** Hinweise auf häufige Fehler und kritische Punkte
*   **INFO-BOX SUCCESS:** Best Practices und Erfolgstipps
*   **ACCORDION:** Zusätzliche Details, die du bei Bedarf ausklappen kannst
*   **TABELLE:** Übersichtliche Gegenüberstellungen
*   **QUIZ:** Wissensfragen zur Selbstkontrolle

### Zeitaufwand und Lernziele

Die gesamte Schulung dauert je nach Vorkenntnissen und Lerntempo etwa **eine Stunde**. Du kannst die Schulung jederzeit unterbrechen und später fortsetzen. Dein Fortschritt wird automatisch festgehalten solange du die Seite nicht schliesst oder aktualisierst.

**INFO-BOX: Geschätzter Zeitaufwand pro Kapitel**

*   Vorwort: 5 Minuten
*   Kapitel 1 (Einführung in das ambulante Gesamt-Tarifsystem): 5 Minuten
*   Kapitel 2 (Dignitäten und Besitzstände): 5 Minuten
*   Kapitel 3 (Diagnosen als ICD-10 Code): 5 Minuten
*   Kapitel 4 (LKAAT - Der Leistungskatalog): 10-15 Minuten
*   Kapitel 5 (Ambulante Behandlung): 10-15 Minuten
*   Kapitel 6 (TARDOC - Der Einzelleistungstarif): 5-10 Minuten
*   Kapitel 7 (Ambulante Pauschalen): 5-10 Minuten
*   Kapitel 8 (TARDOC vs. ambulante Pauschalen): 5-10 Minuten
*   Kapitel 9 (Praxisanwendung und Best Practices): 10-15 Minuten
*   Abschlusstest: 10-15 Minuten
*   FAQ: individuell

### Lernziele der Gesamtschulung

Nach erfolgreichem Abschluss dieser Schulung bist du in der Lage:

*   Die Struktur und Komponenten des ambulanten Gesamt-Tarifsystems zu erklären
*   Ambulante von stationären Behandlungen abzugrenzen
*   Den LKAAT zur korrekten Leistungserfassung zu nutzen
*   Diagnosen korrekt nach ICD-10-GM zu codieren
*   TARDOC-Leistungen zu identifizieren und abzurechnen
*   Ambulante Pauschalen zu erkennen und anzuwenden
*   Das richtige Abrechnungssystem für verschiedene Behandlungssituationen auszuwählen
*   Häufige Fehlerquellen zu vermeiden und Best Practices anzuwenden

### Technische Voraussetzungen

**INFO-BOX: Was du benötigst**

*   Einen modernen Webbrowser (Chrome, Firefox, Safari, Edge)
*   Eine stabile Internetverbindung
*   Etwa 1 Stunde ungestörte Lernzeit
*   Optional: Notizblock für eigene Anmerkungen

### Support und Fragen

Bei Fragen oder technischen Problemen wende dich bitte an deine Schulungsverantwortlichen oder nutze die bereitgestellten Support-Kanäle.

**INFO-BOX SUCCESS: Bereit zu starten?**

Klicke auf "Weiter", um mit Kapitel 1 zu beginnen. Wir wünschen dir viel Erfolg beim Lernen!

---

## KAPITEL 1: Einführung in das ambulante Gesamt-Tarifsystem

BUTTON: Kapitel 1: Einführung  
TITEL: Kapitel 1: Einführung in das ambulante Gesamt-Tarifsystem

### Was ist das ambulante Gesamt-Tarifsystem?

Das ambulante Gesamt-Tarifsystem in der Schweiz regelt die Vergütung von ambulanten medizinischen Leistungen. Es besteht aus mehreren Komponenten, die sich ergänzen und gemeinsam ein umfassendes Abrechnungssystem bilden.

**INFO-BOX: Die Komponenten des Systems**

*   **LKAAT:** Leistungskatalog zur Erfassung aller Leistungen
*   **TARDOC:** Einzelleistungstarif für die detaillierte Abrechnung
*   **Ambulante Pauschalen:** Pauschaltarif für komplexe Behandlungen

### Warum verschiedene Komponenten?

Die Kombination aus Leistungserfassung und unterschiedlichen Abrechnungssystemen ermöglicht eine bedarfsgerechte Vergütung.

**ACCORDION:**

**Flexibilität in der Abrechnung**

Je nach Art der Behandlung kann das passende Abrechnungssystem gewählt werden. Einfache Konsultationen werden über TARDOC einzeln abgerechnet, während komplexe Behandlungen pauschal vergütet werden können.

**Wirtschaftlichkeit und Transparenz**

Pauschalen schaffen Planungssicherheit für Leistungserbringer und Kostenträger, während TARDOC eine detaillierte und transparente Abrechnung ermöglicht.

**Anpassung an internationale Standards**

Das System orientiert sich an bewährten internationalen Modellen und ermöglicht eine bessere Vergleichbarkeit der Gesundheitskosten.

**INFO-BOX WARNUNG: Wichtig zu wissen**

Als Anwender:in musst du verstehen, wann welches System anzuwenden ist. Eine falsche Zuordnung kann zu Abrechnungsfehlern und finanziellen Nachteilen führen.

### Lernziele dieses Moduls

Nach Abschluss dieser Schulung kannst du:

*   Die Komponenten des Tarifsystems unterscheiden und ihre Funktionen benennen
*   Den LKAAT für die Leistungserfassung nutzen
*   Die Struktur von TARDOC erklären und Leistungen korrekt codieren
*   Ambulante Pauschalen identifizieren und zuordnen
*   Das richtige System für verschiedene Behandlungssituationen auswählen
*   Häufige Fehlerquellen in der Praxis vermeiden

### QUIZ

**Frage 1: Aus wie vielen Hauptkomponenten besteht das ambulante Gesamt-Tarifsystem?**

*   a) Eine Komponente
*   b) Zwei Komponenten
*   c) Drei Komponenten (LKAAT, TARDOC, Ambulante Pauschalen) ✓
*   d) Vier Komponenten

**Frage 2: Welche Komponente dient zur Leistungserfassung?**

*   a) Ambulante Pauschalen
*   b) TARDOC
*   c) LKAAT ✓
*   d) TARMED

---

## KAPITEL 2: Dignitäten und Besitzstände

BUTTON: Kapitel 2: Dignitäten  
TITEL: Kapitel 2: Dignitäten und Besitzstände

### 2.1 Was sind Dignitäten?

**Dignitäten** bezeichnen im Schweizer Gesundheitswesen die qualitative Berechtigung von Ärztinnen und Ärzten, bestimmte medizinische Leistungen abzurechnen. Sie stellen ein zentrales Steuerungsinstrument im ambulanten Tarifsystem dar und gewährleisten, dass nur entsprechend qualifizierte Leistungserbringer bestimmte Tarifpositionen verrechnen können.

**INFO-BOX: Definition Dignitäten**

*   **Qualitative Dignitäten** berechtigen zur Verrechnung spezifischer Tarifpositionen
*   Basieren auf nachgewiesenen Weiterbildungstiteln und Qualifikationen
*   Werden in der MEDREG-Datenbank zentral verwaltet
*   Sind unabdingbare Voraussetzung für die Leistungsabrechnung
*   Gewährleisten die Qualitätssicherung im Gesundheitswesen

### 2.2 Funktion der Dignitäten im Tarifsystem

Dignitäten erfüllen mehrere wichtige Funktionen:

1.  **Qualitätssicherung**: Nur entsprechend ausgebildete Fachpersonen dürfen spezifische Leistungen erbringen
2.  **Tarifsteuerung**: Verhinderung der Abrechnung von Leistungen ohne entsprechende Qualifikation
3.  **Transparenz**: Klare Zuordnung zwischen Qualifikation und abrechnungsfähigen Leistungen
4.  **Patientensicherheit**: Gewährleistung der fachgerechten medizinischen Versorgung

**INFO-BOX: Wichtig**

Die Dignitäten sind im Anhang F der Allgemeinen Bestimmungen Ambulante Pauschalen (ABAP) sowie in Anhang I des LKAAT detailliert geregelt. Jede Tarifposition im LKAAT definiert, welche Dignität für deren Verrechnung erforderlich ist.

### 2.3 Arten von qualitativen Dignitäten

Das Schweizer Tarifsystem unterscheidet drei Hauptkategorien von Dignitäten:

**ACCORDION: 2.3.1 Inhaberinnen und Inhaber von Weiterbildungstiteln**

Diese Kategorie umfasst Ärztinnen und Ärzte mit folgenden anerkannten Titeln:

**a) Facharzttitel**

*   Von der Medizinalberufekommission (MEBEKO) anerkannte Facharztausbildungen
*   Beispiele: Facharzt für Allgemeine Innere Medizin, Facharzt für Chirurgie, Facharzt für Pädiatrie
*   Berechtigen zur Abrechnung aller Leistungen des entsprechenden Fachgebiets

**b) Schwerpunkte**

*   Spezialisierungen innerhalb eines Facharzttitels
*   Beispiele: Schwerpunkt Neuropädiatrie, Schwerpunkt Kinderkardiologie
*   Erweitern die Abrechnungsberechtigung innerhalb des Fachgebiets

**c) Fähigkeitsausweise**

*   Zusatzqualifikationen für spezifische Behandlungsmethoden oder Techniken
*   Beispiele: Manualmedizin SAMM, Akupunktur ASA, Sportmedizin SGSM
*   Berechtigen zur Abrechnung der entsprechenden Spezialleistungen

**d) Interdisziplinäre Schwerpunkte**

*   Fachübergreifende Spezialisierungen
*   Beispiel: Schwerpunkt Geriatrie
*   Können von Ärzten verschiedener Fachrichtungen erworben werden

**Wichtig**: Alle diese Titel müssen im Weiterbildungstitelregister MEDREG eingetragen sein, damit die entsprechende Dignität für die Tarifabrechnung gültig ist.

**ACCORDION: 2.3.2 Ärztinnen und Ärzte in Weiterbildung**

Diese Kategorie regelt die Abrechnungsberechtigung während der fachärztlichen Ausbildung:

**Voraussetzungen für Ärzte in Weiterbildung:**

*   Gültiges eidgenössisches Arztdiplom
*   Anstellung in einer anerkannten Weiterbildungsstätte
*   Supervision durch einen Weiterbildner mit entsprechendem Facharzttitel
*   Eintragung der Weiterbildungssituation in MEDREG

**Abrechnungsberechtigung:**

*   Grundsätzlich können Leistungen unter Supervision abgerechnet werden
*   Die Dignität wird über die Weiterbildungsstätte und den supervisionierenden Facharzt gewährleistet
*   Einschränkungen können je nach Tarifposition und Weiterbildungsjahr bestehen

**Verantwortlichkeit:**

*   Die fachliche Verantwortung liegt beim supervisionierenden Facharzt
*   Die Weiterbildungsstätte trägt die organisatorische Verantwortung
*   Dokumentationspflicht der Supervision

**ACCORDION: 2.3.3 Inhaberinnen und Inhaber von Besitzständen**

Besitzstände sind Übergangsregelungen für Ärzte, die zum Zeitpunkt der Tarifeinführung bestimmte Leistungen bereits erbracht haben, ohne über den formal erforderlichen Weiterbildungstitel zu verfügen.

**Grundprinzip des Besitzstands:**

*   Schutz der bisher ausgeübten ärztlichen Tätigkeit
*   Vermeidung von abrupten Einschränkungen der Behandlungsmöglichkeiten
*   Zeitlich befristete Übergangslösung
*   Gilt nur für bereits vor Tarifeinführung erbrachte Leistungen

**Arten von Besitzständen:**

1.  **Vollständiger Besitzstand**: Berechtigung zur vollumfänglichen Leistungsabrechnung wie bei Titelinhabern
2.  **Eingeschränkter Besitzstand**: Berechtigung nur für spezifische Teilleistungen
3.  **Befristeter Besitzstand**: Zeitlich limitierte Übergangsregelung mit festem Ablaufdatum

**Wichtig**: Besitzstände werden im Abschnitt 2.4 detailliert behandelt.

### 2.4 Besitzstände im Detail

#### 2.4.1 Definition und Rechtsgrundlage

Ein **Besitzstand** ist eine qualitative Dignität, die Ärztinnen und Ärzten ohne formalen Weiterbildungstitel die Abrechnung bestimmter Leistungen ermöglicht, sofern sie diese Leistungen bereits vor Inkrafttreten der neuen Tarifstruktur nachweislich erbracht haben.

**INFO-BOX WARNUNG: Rechtliche Grundlagen**

*   Besitzstände sind im Anhang F der ABAP sowie im OAAT geregelt
*   Sie gelten als Übergangsrecht und unterliegen strengen Nachweispflichten
*   Falsche Deklaration kann zu Rückforderungen und rechtlichen Konsequenzen führen
*   Die Beweislast liegt beim Leistungserbringer

#### 2.4.2 Deklaration von Besitzständen

**Deklarationsprozess:**

**Fristgerechte Anmeldung**

*   Deklaration innerhalb der vorgegebenen Frist nach Tarifeinführung
*   Schriftliche Einreichung mit vollständiger Dokumentation
*   Nutzung der offiziellen Deklarationsformulare

**Erforderliche Nachweise**

*   Nachweis der tatsächlich erbrachten Leistungen (z.B. Abrechnungsstatistiken)
*   Zeitraum: Mindestens 2 Jahre vor Tarifeinführung
*   Dokumentation der fachlichen Qualifikation (Kurse, Fortbildungen)
*   Bestätigung der Praxistätigkeit

**Prüfung durch die zuständige Stelle**

*   Formelle Prüfung der Vollständigkeit
*   Inhaltliche Validierung der Nachweise
*   Entscheid über Anerkennung oder Ablehnung

**INFO-BOX: Deklarationsfristen**

*   Deklarationsfristen sind verbindlich und können in der Regel nicht verlängert werden
*   Versäumte Fristen führen zum Verlust des Besitzstandsanspruchs
*   Rechtzeitige Vorbereitung der Dokumentation ist essentiell
*   Bei Unklarheiten: Frühzeitige Kontaktaufnahme mit der zuständigen Stelle

#### 2.4.3 Validierung von Besitzständen

Nach erfolgreicher Deklaration erfolgt eine Validierung des Besitzstands:

**Validierungskriterien:**

**Quantitativer Nachweis**

*   Mindestanzahl erbrachter Leistungen im Referenzzeitraum
*   Kontinuität der Leistungserbringung
*   Relevantes Leistungsvolumen

**Qualitativer Nachweis**

*   Dokumentation der fachlichen Kompetenz
*   Nachweis von Fortbildungen und Kursen
*   Gegebenenfalls Fallbeispiele oder Referenzen

**Zeitlicher Nachweis**

*   Belegbare Leistungserbringung im festgelegten Referenzzeitraum
*   Lückenlose Dokumentation

**Ergebnis der Validierung:**

*   **Volle Anerkennung**: Besitzstand wird uneingeschränkt gewährt
*   **Teilweise Anerkennung**: Besitzstand wird mit Einschränkungen gewährt
*   **Ablehnung**: Besitzstand wird nicht anerkannt (Widerspruchsmöglichkeit)

**Eintragung in MEDREG:**

Nach erfolgreicher Validierung wird der Besitzstand im MEDREG-Register eingetragen und ist damit für die Tarifabrechnung wirksam.

#### 2.4.4 Revalidierung von Besitzständen

Viele Besitzstände sind nicht unbefristet gültig und erfordern eine **Revalidierung**:

**Revalidierungspflicht:**

*   Periodische Überprüfung der Fortbildungsaktivitäten
*   Nachweis der kontinuierlichen Leistungserbringung
*   Aktualisierung der Dokumentation

**Revalidierungsfristen:**

*   In der Regel alle 3-5 Jahre (je nach spezifischer Regelung)
*   Rechtzeitige Benachrichtigung durch die zuständige Stelle
*   Fristversäumnis führt zum Erlöschen des Besitzstands

**Revalidierungsanforderungen:**

**Fortbildungsnachweis**

*   Teilnahme an fachspezifischen Fortbildungen
*   Mindestanzahl an Fortbildungsstunden
*   Anerkennung durch entsprechende Fachgesellschaften

**Praxisnachweis**

*   Kontinuierliche Ausübung der betreffenden Leistungen
*   Dokumentation des Leistungsvolumens
*   Qualitätsnachweise

**Aktualität der Kenntnisse**

*   Nachweis der Kenntnis aktueller Leitlinien
*   Eventuell praktische Prüfungen oder Audits

**INFO-BOX SUCCESS: Praxistipp Revalidierung**

Führen Sie ein systematisches Fortbildungsportfolio:

*   Dokumentieren Sie alle besuchten Fortbildungen fortlaufend
*   Sammeln Sie Teilnahmebestätigungen und Zertifikate
*   Erstellen Sie jährliche Statistiken Ihrer Leistungserbringung
*   Bereiten Sie die Revalidierung frühzeitig vor (6 Monate im Voraus)

#### 2.4.5 Auslaufen von Besitzständen

Besitzstände sind grundsätzlich Übergangsregelungen und können auslaufen:

**Gründe für das Erlöschen eines Besitzstands:**

**Zeitliche Befristung**

*   Festgelegtes Ablaufdatum erreicht
*   Keine weitere Verlängerung möglich
*   Übergang zu regulären Weiterbildungstiteln erforderlich

**Nicht erfolgte Revalidierung**

*   Versäumte Revalidierungsfristen
*   Unzureichende Fortbildungsnachweise
*   Einstellung der Leistungserbringung

**Erwerb des regulären Titels**

*   Besitzstand wird durch Facharzttitel ersetzt
*   Automatische Umstellung in MEDREG

**Übergangsregelungen beim Auslaufen:**

*   In der Regel Vorankündigungsfrist von mindestens 1 Jahr
*   Möglichkeit zum Erwerb des regulären Weiterbildungstitels
*   Eventuell vereinfachte Anerkennungsverfahren

### 2.5 Verwaltung der Dignitäten in MEDREG

Die **MEDREG-Datenbank** ist das zentrale Register für alle medizinischen Berufe in der Schweiz und verwaltet auch die Dignitäten:

#### 2.5.1 MEDREG als zentrale Datenbank

**Funktionen von MEDREG:**

*   Registrierung aller Ärztinnen und Ärzte mit Berufsausübungsbewilligung
*   Verwaltung aller Weiterbildungstitel, Schwerpunkte und Fähigkeitsausweise
*   Dokumentation der Besitzstände
*   Schnittstelle zu den Tarifierungs- und Abrechnungssystemen
*   Verifizierung der Abrechnungsberechtigungen

#### 2.5.2 Eintragung und Aktualisierung

**Prozess der Eintragung:**

1.  Beantragung durch den Titelinhaber oder die zuständige Institution
2.  Prüfung der Nachweise durch die kantonale Gesundheitsdirektion
3.  Eintragung in MEDREG nach erfolgreicher Prüfung
4.  Automatische Übernahme in die Tarifierungs-/Abrechnungssysteme

**Aktualisierungspflicht:**

*   Meldung aller Änderungen (neue Titel, Besitzstände)
*   Aktualität der Kontaktdaten
*   Meldung bei Beendigung der Berufstätigkeit

#### 2.5.3 Schnittstellen zu Abrechnungssystemen

**INFO-BOX: Technische Integration**

*   MEDREG-Daten werden täglich mit Abrechnungssystemen synchronisiert
*   Automatische Prüfung der Dignitäten bei jeder Leistungsabrechnung
*   Fehlende oder abgelaufene Dignitäten führen zu Abrechnungsfehlern
*   Wichtig: Rechtzeitige Aktualisierung vor Ablaufdaten

### 2.6 Praktische Anwendung

#### Beispiel 1: Facharzttitel

**Szenario**: Dr. med. Anna Müller hat ihre Facharztausbildung in Allgemeiner Innerer Medizin abgeschlossen und möchte eine Praxis eröffnen.

**Vorgehen:**

1.  Beantragung des Facharzttitels bei der MEBEKO
2.  Nach Erhalt des Titels: Eintragung in MEDREG über die kantonale Gesundheitsdirektion
3.  Erhalt der Berufsausübungsbewilligung (BAB)
4.  Automatische Freischaltung aller Tarifpositionen, die die Dignität "Facharzt Allgemeine Innere Medizin" erfordern
5.  Start der Praxistätigkeit mit vollständiger Abrechnungsberechtigung

#### Beispiel 2: Besitzstand

**Szenario**: Dr. med. Peter Schmidt ist seit 15 Jahren als praktischer Arzt tätig und führt regelmässig kleinere chirurgische Eingriffe durch, verfügt aber nicht über einen Facharzttitel Chirurgie.

**Vorgehen:**

1.  Fristgerechte Deklaration des Besitzstands für chirurgische Leistungen
2.  Einreichung der Nachweise:
    *   Abrechnungsstatistiken der letzten 3 Jahre
    *   Dokumentation besuchter chirurgischer Fortbildungen
    *   Beschreibung der regelmässig durchgeführten Eingriffe
3.  Validierung durch die zuständige Stelle
4.  Bei positiver Validierung: Eintragung des Besitzstands in MEDREG
5.  Regelmässige Revalidierung gemäss Vorgaben (z.B. alle 3 Jahre)
6.  Fortlaufende Dokumentation der Fortbildungen und Leistungserbringung

#### Beispiel 3: Arzt in Weiterbildung

**Szenario**: Dr. med. Lisa Weber befindet sich im 3. Jahr ihrer Weiterbildung zur Fachärztin für Pädiatrie in einem Kinderspital.

**Vorgehen:**

1.  Das Kinderspital meldet die Weiterbildungssituation an MEDREG
2.  Dr. Weber wird als "Ärztin in Weiterbildung Pädiatrie" registriert
3.  Die erbrachten Leistungen werden unter der Supervision des Weiterbildners über die Dignität der Weiterbildungsstätte abgerechnet
4.  Nach Abschluss der Weiterbildung: Beantragung des Facharzttitels
5.  Aktualisierung in MEDREG: Wechsel von "in Weiterbildung" zu "Fachärztin Pädiatrie"

### 2.7 Häufige Fehler und wie Sie sie vermeiden

**INFO-BOX WARNUNG: Häufige Fehlerquellen**

**Verspätete Aktualisierung in MEDREG**

*   Problem: Neue Titel werden nicht rechtzeitig eingetragen
*   Folge: Abrechnungen werden abgelehnt
*   Lösung: Titel sofort nach Erhalt bei der Gesundheitsdirektion anmelden

**Verpasste Revalidierungsfristen**

*   Problem: Besitzstände werden nicht rechtzeitig revalidiert
*   Folge: Verlust der Abrechnungsberechtigung
*   Lösung: Revalidierungsfristen im Kalender vormerken, 6 Monate vorher vorbereiten

**Unzureichende Dokumentation**

*   Problem: Nachweise für Besitzstände sind lückenhaft
*   Folge: Ablehnung der Deklaration
*   Lösung: Kontinuierliche Dokumentation aller Leistungen und Fortbildungen

**Abrechnung ohne gültige Dignität**

*   Problem: Leistungen werden ohne entsprechende Berechtigung verrechnet
*   Folge: Rückforderungen, evtl. rechtliche Konsequenzen
*   Lösung: Systematische Prüfung der eigenen Dignitäten vor Leistungserbringung

**Fehlende Kenntnis der Dignitätsanforderungen**

*   Problem: Unklare Zuordnung zwischen Leistung und erforderlicher Dignität
*   Folge: Falsche Abrechnungen
*   Lösung: Regelmässige Konsultation des LKAAT und der Anhänge F/I

### 2.8 Rechtliche Aspekte und Compliance

**Rechtliche Grundlagen:**

*   Bundesgesetz über die universitären Medizinalberufe (MedBG)
*   Verordnung über die beruflichen Qualifikationen medizinischer Fachpersonen (VSMED)
*   Allgemeine Bestimmungen Ambulante Pauschalen (ABAP)
*   Organisation ambulante Arzttarife (OAAT)

**Compliance-Anforderungen:**

**Wahrheitspflicht bei Deklarationen**

*   Alle Angaben müssen wahrheitsgemäss und vollständig sein
*   Falsche Angaben können strafrechtliche Konsequenzen haben

**Dokumentationspflicht**

*   Nachweise müssen während der gesetzlichen Aufbewahrungsfrist verfügbar sein
*   Mindestens 10 Jahre Aufbewahrung

**Meldepflicht bei Änderungen**

*   Alle Änderungen der Dignitätssituation müssen zeitnah gemeldet werden
*   Versäumnis kann zu Sanktionen führen

**INFO-BOX WARNUNG: Konsequenzen bei Verstössen**

*   Rückforderung zu Unrecht bezogener Leistungen
*   Vertragsstrafen durch Versicherer
*   Meldung an die kantonale Aufsichtsbehörde
*   Im Extremfall: Entzug der Berufsausübungsbewilligung
*   Strafrechtliche Verfolgung bei vorsätzlichem Betrug

### 2.9 Zusammenfassung

**Wichtigste Erkenntnisse zu Dignitäten:**

1.  Dignitäten sind qualitative Berechtigungen zur Leistungsabrechnung
2.  Drei Hauptkategorien: Titelinhaber, Ärzte in Weiterbildung, Besitzstandsinhaber
3.  MEDREG ist die zentrale Verwaltungsplattform
4.  Besitzstände sind Übergangsregelungen mit strengen Anforderungen
5.  Revalidierung von Besitzständen ist regelmässig erforderlich
6.  Falsche Deklarationen haben ernsthafte rechtliche Konsequenzen

**INFO-BOX SUCCESS: Best Practices**

*   Führen Sie ein persönliches Dignitätsportfolio
*   Dokumentieren Sie alle Fortbildungen systematisch
*   Prüfen Sie regelmässig Ihre MEDREG-Einträge auf Aktualität
*   Setzen Sie sich frühzeitig mit Revalidierungsfristen auseinander
*   Konsultieren Sie bei Unklarheiten die zuständigen Stellen
*   Bleiben Sie über Änderungen in den Tarifbestimmungen informiert

### QUIZ: Kapitel 2 - Dignitäten und Besitzstände

**Frage 1**: Welche der folgenden Aussagen zu Dignitäten ist korrekt?

*   a) Dignitäten sind optional und dienen nur der Qualitätssicherung
*   b) Dignitäten sind unabdingbare Voraussetzung für die Abrechnung bestimmter Leistungen
*   c) Nur Fachärzte benötigen Dignitäten, praktische Ärzte nicht
*   d) Dignitäten werden direkt von den Fachgesellschaften vergeben ✓

**Frage 2**: Was ist ein Besitzstand im Kontext des Tarifsystems?

*   a) Ein dauerhaft garantiertes Recht zur Leistungsabrechnung
*   b) Eine Übergangslösung für Ärzte ohne formalen Titel, die Leistungen bereits vor Tarifeinführung erbracht haben ✓
*   c) Eine neue Form von Facharzttitel
*   d) Ein Fortbildungszertifikat

**Frage 3**: Welche Datenbank verwaltet die Dignitäten in der Schweiz zentral?

*   a) TARMED
*   b) LKAAT
*   c) MEDREG ✓
*   d) ICD-10-GM

**Frage 4**: Was ist bei der Revalidierung von Besitzständen erforderlich?

*   a) Nur die Zahlung einer Verwaltungsgebühr
*   b) Nachweis von Fortbildungen und kontinuierlicher Leistungserbringung ✓
*   c) Eine neue Prüfung wie beim Facharzttitel
*   d) Nichts, Besitzstände sind unbefristet gültig

**Frage 5**: Welche drei Hauptkategorien von qualitativen Dignitäten gibt es?

*   a) Fachärzte, Allgemeinärzte und Spezialisten
*   b) Titelinhaber, Ärzte in Weiterbildung und Besitzstandsinhaber ✓
*   c) Schweizer Ärzte, EU-Ärzte und Drittstaaten-Ärzte
*   d) Praxisärzte, Spitalärzte und Notfallärzte

---

## KAPITEL 3: Diagnosen als ICD-10 Code

BUTTON: Kapitel 3: Diagnosen ICD-10  
TITEL: Kapitel 3: Diagnosen als ICD-10 Code

### Was ist ICD-10-GM?

Die **ICD-10-GM** (Internationale statistische Klassifikation der Krankheiten und verwandter Gesundheitsprobleme, 10. Revision, German Modification) ist ein weltweit anerkanntes System zur Kodierung von Diagnosen im Gesundheitswesen. Im ambulanten Tarifsystem der Schweiz spielt die korrekte Diagnosecodierung eine zentrale Rolle für die Abrechnung und Dokumentation.

**INFO-BOX: Definition ICD-10-GM**

*   Standardisiertes Klassifikationssystem für medizinische Diagnosen
*   Wird jährlich vom Bundesamt für Statistik (BfS) aktualisiert
*   Verpflichtend für die Abrechnung ambulanter Pauschalen
*   Ermöglicht einheitliche statistische Auswertungen

### Warum ist die Diagnosecodierung wichtig?

**INFO-BOX SUCCESS: Für die Abrechnung**

*   Bestimmt die Eingruppierung in eine Fallgruppe bei Ambulanten Pauschalen
*   Führt zur Zuordnung ins richtige Capitulum (Diagnosegruppe)
*   Beeinflusst die korrekte Vergütung der erbrachten Leistungen

**INFO-BOX: Für die Qualitätssicherung**

*   Ermöglicht statistische Auswertungen
*   Unterstützt das Monitoring von Behandlungsqualität
*   Schafft Transparenz über erbrachte Leistungen

**INFO-BOX: Für die Dokumentation**

*   Sichert die lückenlose Patientendokumentation
*   Gewährleistet Nachvollziehbarkeit der Behandlung
*   Erfüllt gesetzliche Dokumentationspflichten

### Wann wird ICD-10-GM verwendet?

**INFO-BOX WARNUNG: Verpflichtende Verwendung von ICD-10-GM**

*   Bei Sitzungen mit Triggerposition (Ambulante Pauschalen)
*   Bei mehreren Sitzungen am gleichen Tag, wenn mindestens eine Sitzung eine Triggerposition enthält
*   In bestimmten Fachbereichen (siehe Dokumentation zur Datenerhebung der OAAT)

**Alternative: Tessinercode**

*   Bei Sitzungen ohne Triggerposition kann alternativ der Tessinercode verwendet werden
*   Der Tessinercode wird von der OAAT nicht weiterentwickelt
*   Empfehlung: Konsequente Verwendung von ICD-10-GM für alle Sitzungen

### Aufbau eines ICD-10-Codes

**INFO-BOX: Beispiel J45.0**

**Struktur:**

*   **J** = Kapitel (Krankheiten des Atmungssystems, J00-J99)
*   **45** = Kategorie (Asthma bronchiale)
*   **.0** = Unterkategorie (vorwiegend allergisches Asthma)

**Weitere Beispiele:**

*   I10: Essentielle (primäre) Hypertonie
*   M54.5: Kreuzschmerz
*   K35.80: Akute Appendizitis
*   E11.90: Diabetes mellitus Typ 2

**ACCORDION:**

**Ebene 1: Kapitel (Buchstabe + 2 Ziffern)**

*   A00-B99: Bestimmte infektiöse und parasitäre Krankheiten
*   C00-D48: Neubildungen
*   I00-I99: Krankheiten des Kreislaufsystems
*   J00-J99: Krankheiten des Atmungssystems
*   M00-M99: Krankheiten des Muskel-Skelett-Systems

**Ebene 2: Kategorie (3-stellig)**

Beispiel: J45 = Asthma bronchiale

**Ebene 3: Unterkategorie (4-5-stellig)**

Beispiel: J45.0 = Vorwiegend allergisches Asthma

### Richtlinien für die Diagnoseerfassung

**INFO-BOX SUCCESS: Zeitpunkt der Erfassung**

*   Während oder unmittelbar nach der Sitzung
*   Basierend auf dem aktuellen Wissensstand zum Zeitpunkt der Behandlung
*   Ausstehende Untersuchungsresultate (Pathologie, Labor etc.) müssen nicht abgewartet werden

**INFO-BOX: Welche Diagnose erfassen?**

Die Diagnose erfasst denjenigen Zustand, der:

*   Hauptanlass für die Sitzung war
*   Den größten Aufwand an medizinischen Mitteln verursachte (ärztliche & pflegerische Leistungen, Operationen, medizinische Produkte)
*   Der erfolgten Behandlung in Organbezogenheit bzw. Körperregion am nächsten steht

**INFO-BOX WARNUNG: Häufige Fehler vermeiden**

*   Zu unspezifische Symptomcodes statt Organdiagnosen
*   Veraltete Diagnosestände statt aktuellem Wissensstand
*   Mehrere Diagnosen bei einer Sitzung (nur die Hauptdiagnose!)
*   Verwendung nicht-endständiger Codes ohne Begründung

### Besondere Situationen in der Diagnosecodierung

**ACCORDION:**

**Mehrere Leistungen in einer Sitzung**

Werden mehrere Leistungen durchgeführt, wird die Diagnose erfasst, aus welcher der größte Behandlungsaufwand entsteht.

**Fallbeispiel: Hausarztbesuch**

*   **Situation:** Patient kommt zur Medikamenteneinstellung bei Bluthochdruck und lässt zusätzlich ein Muttermal kontrollieren
*   **Hauptaufwand:** Blutdruckmessung 5 Min., Medikamentenanpassung und Beratung 10 Min., Muttermalkontrolle 2 Min.
*   **Zu erfassende Diagnose:** I10 (Essentielle Hypertonie)
*   **Begründung:** Größter Zeitaufwand und medizinischer Aufwand

**Verdachtsdiagnosen**

*   **Szenario 1 - Verdacht bestätigt sich:** Die Diagnose wird entsprechend dem aktuellen Wissensstand erfasst
*   **Szenario 2 - Verdacht wird ausgeschlossen:** Es wird die Diagnose erfasst, welche Anlass für die Sitzung war (die Verdachtsdiagnose)
*   **Beispiel:** Verdacht auf Appendizitis → nach Untersuchung ausgeschlossen → Dennoch Verdachtsdiagnose, da diese Anlass für die Untersuchung war

**Symptomcodes**

*   Diagnosen werden organspezifisch erfasst
*   Symptomcodes werden nur dann erfasst, wenn zum Zeitpunkt der Leistungserbringung keine organbezogene Diagnose zur Verfügung steht
*   **Beispiel:** Besser J45.0 (Allergisches Asthma), Vermeiden R06.0 (Dyspnoe) - nur wenn keine Organdiagnose möglich

**Akut vs. Chronisch**

*   Leidet ein Patient gleichzeitig an der chronischen und akuten Form derselben Krankheit, wird die akute Diagnose erfasst
*   Wenn ein Kombinationscode beide Formen abbildet, wird dieser erfasst
*   **Beispiel COPD mit akuter Verschlechterung:**
    *   Regelung: Akute Form hat Vorrang
    *   Korrekte Wahl: J44.1 (COPD mit akuter Exazerbation) statt J44.9

**Erkrankungen nach medizinischen Maßnahmen**

*   Erkrankungen und Komplikationen nach medizinischen Maßnahmen werden dann erfasst, wenn sie vom behandelnden Arzt/der behandelnden Ärztin als solche beschrieben werden
*   Es wird die Diagnose erfasst, welche den Anlass für die Sitzung in Organbezogenheit, Pathologie und Körperregion am spezifischsten beschreibt

### Diagnosen und Rechnungsstellung

**INFO-BOX: Übermittlung an Versicherer**

**Bei TARDOC-Abrechnung:**

*   Vollständige Diagnose nach Tessinercode (endständig) ODER
*   ICD-10-GM gemäß Anhang C
*   Mindestens der 1. Buchstabe der Diagnose bei Datenschutzgründen

**Bei Ambulanten Pauschalen:**

*   Vollständige Diagnose anhand ICD-10-GM
*   Endständige Lieferung angestrebt
*   Bei Datenschutzgründen: Mindestens 1. Buchstabe + Kapitelzuordnungen (Capitulum)

**INFO-BOX SUCCESS: Datenschutz**

Die Übermittlung erfolgt über gesicherte und verschlüsselte Kanäle. Bei Datenschutzbedenken können verkürzte Codes übermittelt werden, wobei mindestens der erste Buchstabe angegeben werden muss.

### Praktische Übung

**INFO-BOX: Fallbeispiel 1 - Kniearthroskopie**

*   **Situation:** Patient mit Meniskusschaden
*   **Ablauf:** 8:00 Ankunft, 9:00 Operation (45 Min.), 10:00 Aufwachraum (2-3h), 13:00 Entlassung
*   **Korrekte Diagnose:** M23.3 (Sonstige Meniskusschädigungen)
*   **Abrechnung:** Ambulante Pauschale

**INFO-BOX: Fallbeispiel 2 - Kombination chronisch/akut**

*   **Situation:** Patient mit COPD kommt wegen akuter Verschlechterung
*   **Diagnoseoptionen:** J44.0 (COPD mit akuter Infektion) oder J44.1 (COPD mit akuter Exazerbation)
*   **Regelung:** Akute Form hat Vorrang
*   **Korrekte Wahl:** J44.1

### Zusammenfassung und Checkliste

**INFO-BOX SUCCESS: Checkliste Diagnosecodierung**

*   ICD-10-GM Version des aktuellen Jahres verwenden
*   Diagnose während oder unmittelbar nach der Sitzung erfassen
*   Hauptanlass der Behandlung identifizieren
*   Organspezifische Diagnose bevorzugen
*   Bei Triggerposition immer ICD-10-GM verwenden
*   Endständigen Code anstreben
*   Bei Akut/Chronisch: Akute Form wählen
*   Dokumentation lückenlos führen

### QUIZ

**Frage 1: Wofür steht die Abkürzung ICD-10-GM?**

*   a) Internationale Codierung Diagnosen - 10. Generation Medizin
*   b) Internationale statistische Klassifikation der Krankheiten, 10. Revision, German Modification ✓
*   c) International Clinical Diagnosis - 10th Grade Medicine
*   d) Interne Codierung deutscher medizinischer Diagnosen

**Frage 2: Wann MUSS ICD-10-GM zwingend verwendet werden?**

*   a) Bei allen ambulanten Behandlungen
*   b) Nur im stationären Bereich
*   c) Bei Sitzungen mit Triggerposition ✓
*   d) Nur bei chirurgischen Eingriffen

**Frage 3: Welche Diagnose wird bei mehreren Leistungen in einer Sitzung erfasst?**

*   a) Die erste durchgeführte Leistung
*   b) Die Diagnose mit dem höchsten ICD-Code
*   c) Alle Diagnosen werden erfasst
*   d) Die Diagnose mit dem größten Behandlungsaufwand ✓

**Frage 4: Was gilt bei chronischen Erkrankungen mit akuter Exazerbation?**

*   a) Nur die chronische Form wird codiert
*   b) Die akute Form hat Vorrang ✓
*   c) Beide Formen werden separat erfasst
*   d) Es wird ein Mittelwert gebildet

---

## KAPITEL 4: LKAAT - Der Leistungskatalog

BUTTON: Kapitel 4: LKAAT  
TITEL: Kapitel 4: LKAAT - Der Leistungskatalog

### Was ist der LKAAT?

LKAAT steht für "Leistungskatalog ambulante Arzttarife" und ist das zentrale Werkzeug zur Erfassung aller medizinischen Leistungen im ambulanten Gesamt-Tarifsystem. Der LKAAT ist die Schnittstelle zwischen der erbrachten medizinischen Leistung und dem Abrechnungssystem.

**INFO-BOX: Hauptfunktion des LKAAT**

Der LKAAT dient ausschließlich der Leistungserfassung, NICHT der Abrechnung!

*   Enthält alle medizinischen Leistungen, die erfasst werden können
*   Definiert für jede Leistung, ob TARDOC oder Ambulante Pauschalen zur Anwendung kommen
*   Bildet die Grundlage für die spätere Abrechnung

### Struktur und Aufbau des LKAAT

**TABELLE: Leistungstypen im LKAAT**

| Typ | Bedeutung | Beispiel | LKN-Nummer |
| --- | --- | --- | --- |
| E | Einzelleistungstarif-Position | Ärztliche Konsultation, erste 5 Min. | AA.00.0010 (8-stellig) |
| EZ | Zusatzleistung für Einzelleistungs-Position | \+ Ärztliche Konsultation, jede weitere 1 Min. | AA.00.0020 (8-stellig) |
| P | Pauschalen-Position (Triggerposition) | Stripping der Stammvene | C05.GB.0080 (9-stellig) |
| PZ | Zusatzleistung für Pauschalen-Position | Rechtsherzkatheter unter Belastung | C05.KC.Z001 (9-stellig) |

### Wie funktioniert die Entscheidung TARDOC vs. Pauschale?

**ACCORDION:**

**Schritt 1: Leistung erfassen**

Bei jeder ambulanten Behandlung werden alle erbrachten Leistungen im LKAAT erfasst. Jede Leistung hat eine eindeutige LKN-Nummer (Leistungskatalognummer).

**Schritt 2: Typ prüfen**

Das System prüft automatisch den Typ der erfassten Leistung:

*   E oder EZ: Einzelleistungsposition → Abrechnung über TARDOC
*   P oder PZ: Pauschalen-Position (Triggerposition) → Abrechnung über Ambulante Pauschalen

**Schritt 3: Abrechnungssystem wird bestimmt**

Sobald eine Triggerposition (P) erfasst wird, erfolgt die Abrechnung über Ambulante Pauschalen. Wurde keine Triggerposition erfasst, wird über TARDOC abgerechnet.

### LKN-Nummern verstehen

**INFO-BOX SUCCESS: So erkennst du den Unterschied**

**TARDOC-Positionen (8-stellig):**

```
AA.00.0010 - Ärztliche Konsultation, erste 5 Min.
AA.00.0020 - + Ärztliche Konsultation, jede weitere 1 Min.
AA.25.0010 - Bericht an Arzt, pro 1 Min.
```

**Pauschalen-Positionen (9-stellig):**

```
C05.GB.0080 - Stripping der Stammvene
C05.KC.0100 - Implantation eines flussreduzierenden Stents
C05.KC.Z001 - Rechtsherzkatheter unter Belastung (Zusatz)
```

**Merkhilfe:** Die ersten drei Stellen bei Pauschalen-Positionen (z.B. C05) geben an, welchem Capitulum (Kapitel) die Pauschale zugeordnet ist.

### Triggerpositionen - Das Herzstück des Systems

*   **Was löst eine Pauschale aus?** Sobald eine Triggerposition (Typ P) erfasst wird, wird die gesamte Behandlung über Ambulante Pauschalen abgerechnet, nicht mehr über TARDOC
*   **Beispiele für Triggerpositionen:** Chirurgische Eingriffe, Endoskopien mit Intervention, komplexe diagnostische Verfahren
*   **Wichtig:** Eine Behandlung kann entweder über TARDOC ODER über Pauschalen abgerechnet werden, nie beides gemischt (außer definierte Zusatzentgelte)

### Praktisches Beispiel

**INFO-BOX: Fallbeispiel - Zwei Behandlungen am gleichen Tag**

**Situation:** Patient:in kommt zweimal am gleichen Tag

**Behandlung 1 (Vormittag):**

*   Erfasste Leistung: AA.00.0010 (Typ E) - Konsultation
*   → Keine Triggerposition
*   → Abrechnung über TARDOC

**Behandlung 2 (Nachmittag - anderer Grund):**

*   Erfasste Leistung: C05.GB.0080 (Typ P) - Stripping der Stammvene
*   → Triggerposition!
*   → Abrechnung über Ambulante Pauschalen

**Ergebnis:** Da beide Behandlungen unterschiedliche Gründe haben und in verschiedenen Capitulum aufgeführt sind, sind zwei ambulante Behandlungen möglich.

### Tools für die Arbeit mit dem LKAAT

**INFO-BOX: LKAAT plus Browser**

*   Online-Tarifbrowser der Ärztekasse und der FMH
*   Umfangreiche Suchfunktionen
*   Zeigt an, welche LKAAT-Leistungen Pauschalen auslösen
*   Vergleich mit TARMED-Leistungen möglich
*   ICD-10 Zuordnung der Diagnosen zu den Capitulum

**INFO-BOX WARNUNG: Häufige Fehler beim LKAAT**

*   Verwechslung von Leistungserfassung (LKAAT) und Abrechnung (TARDOC/Pauschalen)
*   Übersehen einer Triggerposition → falsche Abrechnung über TARDOC
*   Falsche Annahme, dass 8-stellige Nummern immer TARDOC bedeuten
*   Nichtbeachtung der Capitulum-Zuordnung bei Pauschalen

### QUIZ

**Frage 1: Wofür steht die Abkürzung LKAAT?**

*   a) Leistungskatalog aller ambulanten Tarife
*   b) Leistungskatalog ambulante Arzttarife ✓
*   c) Leistungskosten ambulanter Arzt-Behandlungen
*   d) Leistungsverzeichnis klinischer ambulanter Tarife

**Frage 2: Was bedeutet eine Position mit dem Typ "P" im LKAAT?**

*   a) Private Leistung
*   b) Pauschalen-Position (Triggerposition) ✓
*   c) Präventive Leistung
*   d) Priorisierte Leistung

**Frage 3: Wie viele Stellen hat eine LKN-Nummer für TARDOC-Positionen?**

*   a) 6 Stellen
*   b) 7 Stellen
*   c) 8 Stellen ✓
*   d) 9 Stellen

**Frage 4: Was löst eine Triggerposition aus?**

*   a) Eine doppelte Abrechnung
*   b) Die Abrechnung über Ambulante Pauschalen ✓
*   c) Eine Kostengutsprache
*   d) Eine Warnung im System

---

## KAPITEL 5: Ambulante Behandlung

BUTTON: Kapitel 5: Ambulante Behandlung  
TITEL: Kapitel 5: Ambulante Behandlung

### Was ist eine ambulante Behandlung?

Eine **ambulante Behandlung** ist eine medizinische Leistung, bei der Patient:innen die Gesundheitseinrichtung am selben Tag wieder verlassen können, ohne über Nacht zu bleiben. Der Begriff "ambulant" leitet sich vom lateinischen "ambulare" ab, was "umhergehen" bedeutet.

**INFO-BOX: Kernmerkmale ambulanter Behandlungen**

*   **Keine Übernachtung:** Patient:innen gehen am selben Tag nach Hause
*   **Kurze Behandlungsdauer:** Meist wenige Minuten bis Stunden
*   **Geringere Komplexität:** Behandlungen, die keine intensive Überwachung erfordern
*   **Verschiedene Settings:** Arztpraxis, Ambulatorium, Spitalambulanz

### Abgrenzung: Ambulant vs. Stationär

Die Unterscheidung zwischen ambulant und stationär ist entscheidend für die Abrechnung und die Zuständigkeiten:

**TABELLE: Vergleich Ambulant vs. Stationär**

| Kriterium | Ambulant | Stationär |
| --- | --- | --- |
| Aufenthaltsdauer | Wenige Stunden, keine Übernachtung | Mindestens eine Übernachtung |
| Tarifsystem | TARDOC / Ambulante Pauschalen | SwissDRG |
| Behandlungsort | Praxis, Ambulatorium, Spitalambulanz | Spital mit Bettenbelegung |
| Überwachung | Keine oder kurze Nachbeobachtung | 24-Stunden-Überwachung |
| Komplexität | Einfach bis mittel | Mittel bis hoch |
| Kostenträger-Anteil | OKP zahlt ca. 42.6% | OKP zahlt 55% |
| Kantonsanteil | Ca. 55% (variiert je nach Kanton) | 45% (fixiert durch KVG) |

**INFO-BOX WARNUNG: Wichtige Abgrenzungsfälle**

In der Praxis gibt es Grenzfälle, die eine klare Zuordnung erfordern:

*   **Tagesklinik:** Ambulant, auch wenn mehrere Stunden Aufenthalt
*   **Observation über Nacht:** Gilt bereits als stationär
*   **OP mit Nachbeobachtung:** Ambulant, wenn Entlassung am gleichen Tag
*   **Notfallbehandlung:** Je nach Aufenthaltsdauer ambulant oder stationär

### Typische ambulante Behandlungen

**ACCORDION:**

**Konsultationen und Untersuchungen**

*   Allgemeine ärztliche Konsultationen
*   Fachärztliche Untersuchungen
*   Präventive Check-ups
*   Nachkontrollen
*   Hausbesuche

**Diagnostische Verfahren**

*   Laboruntersuchungen
*   Röntgen, CT, MRI
*   Ultraschall
*   EKG, Belastungstests
*   Endoskopien (diagnostisch)

**Therapeutische Eingriffe**

*   Kleinere chirurgische Eingriffe
*   Endoskopien mit Intervention
*   Kataraktoperationen
*   Arthroskopien
*   Dialysebehandlungen
*   Chemotherapie-Sitzungen
*   Physiotherapie

**Notfallbehandlungen**

*   Versorgung akuter Verletzungen
*   Akute Erkrankungen ohne Hospitalisierung
*   Wundversorgung
*   Reposition von Frakturen

### Vorteile ambulanter Behandlungen

**INFO-BOX SUCCESS: Für Patient:innen**

*   Verbleib im gewohnten Umfeld
*   Geringeres Infektionsrisiko
*   Schnellere Rückkehr in den Alltag
*   Weniger Belastung durch Krankenhausaufenthalt
*   Geringere Selbstbeteiligung

**INFO-BOX SUCCESS: Für das Gesundheitssystem**

*   Kosteneinsparungen (ca. 30-50% günstiger als stationär)
*   Effizientere Ressourcennutzung
*   Entlastung der Spitalbetten
*   Flexiblere Terminplanung

### Trend zur Ambulantisierung

In den letzten Jahren ist ein klarer Trend zur Verlagerung von stationären zu ambulanten Behandlungen zu beobachten:

**INFO-BOX: Entwicklung und Gründe**

*   **Medizinischer Fortschritt:** Minimalinvasive Techniken ermöglichen schonendere Eingriffe
*   **Bessere Anästhesie:** Schnellere Erholung nach Eingriffen
*   **Politischer Wille:** Förderung ambulanter Behandlungen zur Kostensenkung
*   **"Ambulant vor stationär":** Gesetzliche Regelung in vielen Kantonen
*   **Listen mit ambulant durchzuführenden Eingriffen:** Definierte Kataloge je nach Kanton

### Besonderheiten bei der Abrechnung

Die ambulante Behandlung erfordert besondere Aufmerksamkeit bei der Dokumentation und Abrechnung:

*   **Leistungserfassung:** Jede Leistung muss im LKAAT erfasst werden
*   **Systemwahl:** Entscheidung zwischen TARDOC und Pauschalen
*   **Dokumentation:** Lückenlose Dokumentation aller erbrachten Leistungen
*   **Wirtschaftlichkeit:** Beachtung der WZW-Kriterien (wirksam, zweckmäßig, wirtschaftlich)
*   **Kostenträger:** Klärung der Zuständigkeit (Krankenkasse, Unfallversicherung, etc.)

**INFO-BOX WARNUNG: Häufige Fehler bei der Zuordnung**

*   Falsche Einschätzung der Aufenthaltsdauer
*   Unklare Abgrenzung bei Notfällen
*   Nichtbeachtung kantonaler Regelungen
*   Fehlende Kostengutsprache bei elektiven Eingriffen
*   Verwendung des falschen Tarifsystems

### Praktisches Beispiel

**INFO-BOX: Fallbeispiel - Arthroskopie des Kniegelenks**

**Situation:** Patient:in mit Meniskusschaden

**Ablauf ambulant:**

*   8:00 Uhr: Ankunft und Vorbereitung
*   9:00 Uhr: Operation (ca. 45 Minuten)
*   10:00 Uhr: Aufwachraum (2-3 Stunden Überwachung)
*   13:00 Uhr: Kontrolle und Entlassung
*   Abrechnung über Ambulante Pauschale

**Voraussetzungen:**

*   Keine schweren Begleiterkrankungen
*   Betreuung zu Hause gewährleistet
*   Erreichbarkeit bei Komplikationen
*   Patient:in ist mobil und ansprechbar

**Abrechnung:** Ambulante Pauschale + ggf. Zusatzentgelte für Implantate

### QUIZ

**Frage 1: Was ist das Hauptmerkmal einer ambulanten Behandlung?**

*   a) Die Behandlung findet immer in einer Arztpraxis statt
*   b) Patient:innen verlassen die Einrichtung am selben Tag ohne Übernachtung ✓
*   c) Die Behandlung dauert maximal 1 Stunde
*   d) Es werden keine chirurgischen Eingriffe durchgeführt

**Frage 2: Welches Tarifsystem wird für stationäre Behandlungen verwendet?**

*   a) TARDOC
*   b) SwissDRG ✓
*   c) Ambulante Pauschalen
*   d) LKAAT

**Frage 3: Was ist ein Vorteil ambulanter Behandlungen für das Gesundheitssystem?**

*   a) Höhere Einnahmen
*   b) Kosteneinsparungen und effizientere Ressourcennutzung ✓
*   c) Längere Überwachung der Patient:innen
*   d) Mehr Spitalbetten werden benötigt

**Frage 4: Ab wann gilt eine Behandlung als stationär?**

*   a) Nach 6 Stunden Aufenthalt
*   b) Wenn mindestens eine Übernachtung erfolgt ✓
*   c) Wenn ein chirurgischer Eingriff durchgeführt wird
*   d) Wenn die Kosten über CHF 5'000.- liegen

---

## KAPITEL 6: TARDOC - Der Einzelleistungstarif

BUTTON: Kapitel 6: TARDOC  
TITEL: Kapitel 6: TARDOC - Der Einzelleistungstarif

### Was ist TARDOC?

TARDOC steht für "Tarif ambulanter Arztleistungen in Arztpraxis und ambulantem Spitalbereich" und ist der Nachfolger des TARMED-Tarifs. TARDOC ist ein Einzelleistungstarif, der jede erbrachte medizinische Leistung einzeln erfasst und abrechnet.

**INFO-BOX: Hauptmerkmale von TARDOC**

*   **Einzelleistungsbasiert:** Jede Leistung wird separat codiert
*   **Tarifpunkte:** Leistungen werden in Taxpunkten bewertet
*   **Taxpunktwert:** Variable Umrechnung in Franken je nach Kanton
*   **Limitationen:** Mengenbegrenzungen bei bestimmten Leistungen
*   **11 Hauptkapitel:** 55 Kapitel, 176 Unterkapitel, 1388 Tarifpositionen

### Struktur des TARDOC-Tarifs

**ACCORDION:**

**Kapitel A: Ärztliche Grundleistungen**

Beinhaltet Grundkonsultationen, Notfallleistungen, Hausbesuche, administrative Leistungen und telemedizinische Leistungen. Dies ist die Basis für die meisten ambulanten Behandlungen.

**Beispiele:**

*   AA.00.0010: Ärztliche Konsultation, erste 5 Min.
*   AA.10.0010: Telemedizinische Konsultation, erste 5 Min.
*   AA.25.0010: Bericht an Arzt, pro 1 Min.

**Weitere Kapitel: Diagnostik und Therapie**

Umfasst bildgebende Verfahren, Laborleistungen, therapeutische Maßnahmen, EKG, Ultraschall, Röntgenuntersuchungen, chirurgische Eingriffe und fachspezifische Leistungen.

### Berechnung der Vergütung

**INFO-BOX SUCCESS: Berechnungsformel**

**Vergütung = Taxpunkte × Taxpunktwert**

**Beispiel:**

*   Leistung: Grundkonsultation (150 Taxpunkte)
*   Taxpunktwert: CHF 0.90
*   Vergütung: 150 × 0.90 = CHF 135.00

### Wichtige Regelungen

*   **Kumulation:** Bestimmte Leistungen können nicht zusammen am gleichen Tag abgerechnet werden
*   **Zuschläge:** Für Notfälle, Nacht-/Wochenendarbeit oder besondere Umstände
*   **Limitationen:** Mengenbeschränkungen pro Quartal oder Jahr bei bestimmten Leistungen
*   **Dignität:** Nicht alle Ärzte dürfen alle Leistungen abrechnen (Facharzttitel erforderlich)

**INFO-BOX WARNUNG: Häufige Fehlerquellen**

*   Falsche Zuordnung von Leistungscodes
*   Nichtbeachtung von Kumulationseinschränkungen
*   Überschreitung von Limitationen
*   Abrechnung ohne entsprechende Dignität

### QUIZ

**Frage 1: Wofür steht die Abkürzung TARDOC?**

*   a) Tarif für Doktoren
*   b) Tarif ambulanter Arztleistungen in Arztpraxis und ambulantem Spitalbereich ✓
*   c) Tarifvertrag der Schweizer Ärzte
*   d) Tarif für Dokumentation

**Frage 2: Eine Grundkonsultation kostet 180 Taxpunkte. Bei einem Taxpunktwert von CHF 0.95, wie hoch ist die Vergütung?**

*   a) CHF 150.00
*   b) CHF 171.00 ✓
*   c) CHF 189.50
*   d) CHF 180.00

**Frage 3: Was bedeutet "Dignität" im Kontext von TARDOC?**

*   a) Die Würde des Patienten
*   b) Die Berechtigung zur Abrechnung bestimmter Leistungen ✓
*   c) Die Qualität der Behandlung
*   d) Der Schwierigkeitsgrad einer Leistung

---

## KAPITEL 7: Ambulante Pauschalen (AP)

BUTTON: Kapitel 7: Ambulante Pauschalen  
TITEL: Kapitel 7: Ambulante Pauschalen (AP)

### Was sind Ambulante Pauschalen?

Ambulante Pauschalen sind fallbasierte Vergütungssysteme, bei denen komplexe ambulante Behandlungen nicht nach Einzelleistungen, sondern als Gesamtpaket abgerechnet werden.

**INFO-BOX: Kernprinzip der Pauschalen**

Eine Pauschale deckt alle Leistungen ab, die typischerweise für eine bestimmte Behandlung oder einen bestimmten Eingriff notwendig sind – von der Vorbereitung über die Durchführung bis zur Nachsorge. Das System orientiert sich am stationären SwissDRG-Modell und umfasst 19 Kapitel mit 314 Pauschalen.

### Anwendungsbereiche

Ambulante Pauschalen kommen hauptsächlich zum Einsatz bei:

*   **Chirurgischen Eingriffen:** z.B. Kataraktoperationen, Arthroskopien, kleine Tumorresektionen
*   **Endoskopischen Untersuchungen:** Gastroskopie, Koloskopie mit Polypektomie
*   **Komplexen diagnostischen Verfahren:** PET-CT, spezielle MRI-Untersuchungen
*   **Onkologischen Behandlungen:** Chemotherapie-Zyklen, Strahlentherapie-Serien
*   **Dialysebehandlungen:** Standardisierte Hämodialyse-Sitzungen

### Struktur der Ambulanten Pauschalen

**ACCORDION:**

**AP-Gruppen und Klassifikation**

*   Ambulante Pauschalen sind in 19 Kapitel (Capitulum) eingeteilt
*   Kategorisiert nach medizinischen Kriterien und Behandlungskomplexität
*   Jede Gruppe hat einen eindeutigen Code und eine festgelegte Vergütungshöhe

**Inkludierte Leistungen**

Eine Pauschale beinhaltet typischerweise:

*   Präoperative Voruntersuchungen
*   Der Eingriff/die Behandlung selbst
*   Anästhesieleistungen
*   Verbrauchsmaterialien
*   Postoperative Nachkontrollen (innerhalb definierter Zeiträume)
*   Standard-Medikamente

**Zusatzentgelte**

Bestimmte kostenintensive Leistungen können zusätzlich zur Pauschale abgerechnet werden:

*   Teure Implantate und Prothesen
*   Spezielle Medikamente (z.B. Biologika)
*   Nicht-standardmäßige Diagnostik
*   Komplikationsbehandlungen außerhalb der Norm

### Vorteile der Pauschalen

**INFO-BOX SUCCESS: Für Leistungserbringer**

*   Planungssicherheit bei der Kalkulation
*   Reduktion des administrativen Aufwands
*   Anreiz zur effizienten Behandlung
*   Geringerer Dokumentationsaufwand

**INFO-BOX SUCCESS: Für Kostenträger und Patienten**

*   Transparente und vorhersehbare Kosten
*   Bessere Vergleichbarkeit zwischen Anbietern
*   Vereinfachte Rechnungsprüfung
*   Anreiz zur Qualitätssicherung

### Praktisches Beispiel: Kataraktoperation

**INFO-BOX: Fallbeispiel**

**Situation:** Patient:in benötigt eine Kataraktoperation (Grauer Star)

**Abrechnung über Pauschale:**

*   Ein AP-Code für "Kataraktoperation mit Linsenimplantation"
*   Pauschalbetrag: z.B. CHF 2'500.-
*   Inkludiert: Voruntersuchung, OP, Standardlinse, Anästhesie, 2 Nachkontrollen
*   Zusatzentgelt: Premium-Linse (falls gewünscht): + CHF 800.-

**Ohne Pauschale (TARDOC):**

*   Müsste jede Einzelleistung separat codiert werden (ca. 15-20 verschiedene Positionen)

**INFO-BOX WARNUNG: Wichtige Abgrenzungen**

*   Nicht alle ambulanten Behandlungen können pauschal abgerechnet werden
*   Bei Komplikationen kann eine Umstellung auf TARDOC notwendig sein
*   Pauschalen und TARDOC dürfen nicht beliebig gemischt werden
*   Klare Dokumentation ist essenziell für die Rechtfertigung der Pauschale

### QUIZ

**Frage 1: Was ist das Kernprinzip einer Ambulanten Pauschale?**

*   a) Jede Leistung wird einzeln abgerechnet
*   b) Alle Leistungen einer Behandlung werden als Gesamtpaket abgerechnet ✓
*   c) Nur Medikamente werden pauschal abgerechnet
*   d) Nur die ärztliche Leistung wird pauschal abgerechnet

**Frage 2: Welche Leistungen sind typischerweise in einer Pauschale NICHT inkludiert?**

*   a) Standard-Nachkontrollen
*   b) Teure Spezialimplantate ✓
*   c) Anästhesieleistungen
*   d) Verbrauchsmaterialien

**Frage 3: Was ist ein Vorteil der Pauschalen für Leistungserbringer?**

*   a) Höhere Vergütung als bei TARDOC
*   b) Reduktion des administrativen Aufwands ✓
*   c) Keine Dokumentationspflicht
*   d) Unbegrenzte Abrechnung aller Leistungen

---

## KAPITEL 8: TARDOC vs. ambulante Pauschalen - Der direkte Vergleich

BUTTON: Kapitel 8: Vergleich  
TITEL: Kapitel 8: TARDOC vs. Ambulante Pauschalen - Der direkte Vergleich

### Gegenüberstellung der Systeme

**TABELLE: TARDOC vs. Ambulante Pauschalen**

| Kriterium | TARDOC | Ambulante Pauschalen |
| --- | --- | --- |
| Abrechnungsprinzip | Einzelleistung | Fallpauschale |
| Vergütungseinheit | Taxpunkte pro Leistung | Pauschalbetrag pro Fall |
| Typische Anwendung | Konsultationen, einfache Behandlungen | Komplexe Eingriffe, Behandlungsserien |
| Infrastruktur | Einfach (Sprechzimmer, Ultraschall, Röntgen) | Aufwändig (OP, Nuklearmedizin, Endoskopien) |
| Dokumentationsaufwand | Hoch (jede Leistung) | Moderat (Gesamtbehandlung) |
| Planbarkeit | Variable Kosten | Fixe Kosten |
| Flexibilität | Sehr hoch | Begrenzt |
| Transparenz | Detailliert | Pauschal |
| Effizienzanreiz | Gering | Hoch |
| Tariftyp | 007 | 005 |

### Wann welches System?

**INFO-BOX: Entscheidungshilfe**

**TARDOC verwenden bei:**

*   Routinekonsultationen
*   Einfachen diagnostischen Verfahren
*   Einzelnen therapeutischen Maßnahmen
*   Hausbesuchen
*   Notfallbehandlungen ohne nachfolgende OP
*   Präventionsleistungen (Impfungen, Check-ups)

**Ambulante Pauschalen verwenden bei:**

*   Chirurgischen Eingriffen (auch kleinere)
*   Endoskopischen Interventionen
*   Komplexen bildgebenden Verfahren mit mehreren Sequenzen
*   Behandlungsserien (Chemotherapie, Dialyse)
*   Standardisierten ambulanten Operationen

### Kombinationsmöglichkeiten

**ACCORDION:**

**Grundsätzlich: Keine Mischung im selben Fall**

*   Innerhalb desselben Behandlungsfalls sollten TARDOC und Pauschalen grundsätzlich nicht gemischt werden
*   Die Entscheidung für ein System muss zu Beginn der Behandlung getroffen werden
*   Eine Mischform ist nicht möglich

**Ausnahme: Zwei Behandlungen am gleichen Tag**

Zwei ambulante Behandlungen am gleichen Tag bei gleichem Patienten sind möglich, wenn:

*   Anderer Garant (z.B. Krankheit/Unfall)
*   Diagnose in einem anderen Capitulum aufgeführt ist

**Ausnahme: Zusatzentgelte**

*   Bei Pauschalen können definierte Zusatzentgelte (z.B. teure Implantate, Spezialmedikamente) zusätzlich abgerechnet werden
*   Diese sind aber klar definiert und nicht beliebig

**Ausnahme: Komplikationen**

*   Bei schweren Komplikationen, die nicht durch die Pauschale abgedeckt sind, kann eine Umstellung auf TARDOC erfolgen
*   Dies erfordert jedoch eine klare Dokumentation und Begründung

### Praktische Fallbeispiele

**INFO-BOX SUCCESS: Fall 1 - Arthroskopische Meniskusoperation**

**Richtig:** Abrechnung über Ambulante Pauschale

*   Standardisierter Eingriff
*   Klarer Behandlungspfad
*   Alle Leistungen im Paket
*   Pauschale: ca. CHF 3'200.-

**INFO-BOX SUCCESS: Fall 2 - Behandlung einer akuten Bronchitis**

**Richtig:** Abrechnung über TARDOC

*   Konsultation (150 TP)
*   Auskultation (30 TP)
*   Verschreibung (20 TP)
*   Gesamt: ca. 200 TP = CHF 180.- (bei TP-Wert 0.90)

**INFO-BOX WARNUNG: Fall 3 - Fehlentscheidung vermeiden**

**Situation:** Geplante Koloskopie mit möglicher Polypektomie

*   **Falsch:** Start mit TARDOC, dann Wechsel zu Pauschale während Eingriff
*   **Richtig:** Von Anfang an Pauschale wählen, da Eingriff möglich

### QUIZ

**Frage 1: Welches System bietet höhere Flexibilität in der Abrechnung?**

*   a) Ambulante Pauschalen
*   b) TARDOC ✓
*   c) Beide gleich flexibel
*   d) Keines der Systeme ist flexibel

**Frage 2: Für welche Situation ist TARDOC die richtige Wahl?**

*   a) Kataraktoperation
*   b) Routinekonsultation bei Erkältung ✓
*   c) Koloskopie mit Polypektomie
*   d) Arthroskopische Operation

**Frage 3: Dürfen TARDOC und Pauschalen grundsätzlich im selben Behandlungsfall gemischt werden?**

*   a) Ja, jederzeit
*   b) Nein, grundsätzlich nicht (außer definierte Ausnahmen) ✓
*   c) Ja, aber nur bei Notfällen
*   d) Nur mit Genehmigung der Krankenkasse

---

## KAPITEL 9: Praxisanwendung und Best Practices

BUTTON: Kapitel 9: Praxisanwendung  
TITEL: Kapitel 9: Praxisanwendung und Best Practices

### Der Workflow in der Praxis

Die korrekte Anwendung des Tarifsystems beginnt bereits bei der Patientenanmeldung und durchzieht den gesamten Behandlungsprozess.

**ACCORDION:**

**Schritt 1: Patientenanmeldung und Vorabklärung**

**Zu prüfen:**

*   Versicherungsstatus des Patienten
*   Art der geplanten Behandlung
*   Ist eine Pauschale verfügbar?
*   Kostenübernahmegarantie bei elektiven Eingriffen

**Best Practice:** Bei geplanten Eingriffen immer vorab mit der Krankenversicherung klären, welches Abrechnungssystem akzeptiert wird

**Schritt 2: Behandlung und Dokumentation**

**Bei TARDOC:**

*   Jede erbrachte Leistung zeitnah im LKAAT erfassen
*   Korrekte Leistungscodes verwenden
*   Zeitaufwand und Material festhalten
*   Kumulationsregeln beachten

**Bei Pauschalen:**

*   Triggerposition im LKAAT erfassen
*   Behandlungsverlauf als Ganzes dokumentieren
*   Besonderheiten und Abweichungen vermerken
*   Zusatzentgelte separat erfassen
*   Komplikationen genau beschreiben
*   ICD-10-Diagnose und Capitulum zuordnen

**Schritt 3: Codierung und Rechnungsstellung**

**Qualitätssicherung:**

*   Vollständigkeit der Dokumentation prüfen
*   Codes mit medizinischer Dokumentation abgleichen
*   Plausibilitätsprüfung durchführen
*   Vier-Augen-Prinzip bei komplexen Fällen

### Häufige Fehlerquellen und deren Vermeidung

**INFO-BOX WARNUNG: Top 5 Fehler und Lösungen**

**1\. Falsche Systemwahl**

*   **Problem:** TARDOC für pauschalfähigen Eingriff gewählt
*   **Lösung:** LKAAT-Katalog vorab konsultieren, Triggerposition erkennen

**2\. Unvollständige Dokumentation**

*   **Problem:** Fehlende Angaben führen zu Rückfragen und Zahlungsverzögerungen
*   **Lösung:** Checklisten verwenden, zeitnahe Dokumentation

**3\. Kumulationsfehler bei TARDOC**

*   **Problem:** Nicht kombinierbare Leistungen gleichzeitig abgerechnet
*   **Lösung:** Software mit Kumulationsprüfung nutzen

**4\. Übersehen von Zusatzentgelten**

*   **Problem:** Anspruchsberechtigte Zusatzentgelte nicht geltend gemacht
*   **Lösung:** Materialverbrauch systematisch erfassen

**5\. Fehlende Kostengutsprache**

*   **Problem:** Elektiver Eingriff ohne vorherige Genehmigung
*   **Lösung:** Standardprozess für Kostengutsprachen etablieren

### Tipps für effizientes Arbeiten

**INFO-BOX SUCCESS: Effizienz-Tipps**

**Für LKAAT:**

*   LKAAT plus Browser nutzen für schnelle Suche
*   Triggerpositionen markieren und kennen
*   Regelmäßige Updates zu neuen Leistungen beachten

**Für TARDOC:**

*   Häufig verwendete Leistungskombinationen als Vorlagen speichern
*   Codier-Software mit Plausibilitätsprüfung nutzen
*   Regelmäßige Schulungen für Mitarbeitende
*   Aktuelle Tarifversionen verwenden

**Für Pauschalen:**

*   Standardisierte Behandlungspfade etablieren
*   Material-Sets für typische Eingriffe vorbereiten
*   Klare Prozesse für Zusatzentgelte definieren
*   Regelmäßiger Austausch mit Kostenträgern

### Rechtliche und ethische Aspekte

**INFO-BOX: Was ist zu beachten?**

**Tarifautonomie:**

*   Tarifsystem und Tarife werden von den Sozialpartnern (Leistungserbringer und Kostenträger) gemeinsam vereinbart
*   Einseitige Abweichungen sind nicht zulässig

**Wirtschaftlichkeitsgebot:**

*   Alle Leistungen müssen wirksam, zweckmäßig und wirtschaftlich sein (WZW-Kriterien)
*   Dies gilt für beide Systeme gleichermaßen

**Dokumentationspflicht:**

*   Jede abgerechnete Leistung muss durch die Krankengeschichte belegt sein
*   Bei Kontrollen durch Krankenversicherer oder Trustcenter muss die Dokumentation nachvollziehbar sein

**Datenschutz:**

*   Bei der Übermittlung von Rechnungsdaten sind die datenschutzrechtlichen Bestimmungen strikt einzuhalten

### Zukunftsperspektiven

Das ambulante Tarifsystem entwickelt sich kontinuierlich weiter. Aktuelle Trends sind:

*   **Ausweitung der Pauschalen:** Mehr Behandlungen werden künftig pauschal abrechenbar sein
*   **Digitalisierung:** Automatisierte Codierung und elektronische Rechnungsstellung
*   **Qualitätsindikatoren:** Vergütung zunehmend an Qualitätsparameter gekoppelt
*   **Integrierte Versorgung:** Sektorenübergreifende Pauschalen für komplexe Behandlungspfade

### QUIZ

**Frage 1: Was sollte bereits bei der Patientenanmeldung für geplante Eingriffe geklärt werden?**

*   a) Nur der Versicherungsstatus
*   b) Welches Abrechnungssystem verwendet wird und ob eine Kostenübernahmegarantie vorliegt ✓
*   c) Nur das OP-Datum
*   d) Die Krankengeschichte

**Frage 2: Was ist ein häufiger Fehler bei der TARDOC-Abrechnung?**

*   a) Zu viele Leistungen abrechnen
*   b) Nicht kombinierbare Leistungen gleichzeitig abrechnen (Kumulationsfehler) ✓
*   c) Zu hohe Taxpunktwerte verwenden
*   d) Rechnungen zu spät stellen

**Frage 3: Was bedeutet das WZW-Gebot?**

*   a) Wöchentliche Zeiterfassung und Weitergabe
*   b) Wirtschaftlich, zweckmäßig und wirksam ✓
*   c) Wahl zwischen zwei Werktagen
*   d) Weltweite Zulassung und Werbung

---

## Abschlusstest

BUTTON: Abschlusstest  
TITEL: Abschlusstest

**INFO-BOX: Hinweise zum Abschlusstest**

Dieser Test umfasst 12 Fragen zu allen Kapiteln. Du benötigst mindestens 10 von 12 richtigen Antworten, um die Schulung erfolgreich abzuschließen. Viel Erfolg!

### QUIZ - ABSCHLUSSTEST

**Frage 1: Welche Hauptkomponenten umfasst das ambulante Gesamt-Tarifsystem?**

*   a) TARMED und DRG
*   b) LKAAT, TARDOC und Ambulante Pauschalen ✓
*   c) SwissDRG und TARDOC
*   d) Nur TARDOC

**Frage 2: Wofür steht LKAAT?**

*   a) Leistungskatalog aller ambulanten Tarife
*   b) Leistungskatalog ambulante Arzttarife ✓
*   c) Leistungskosten ambulanter Arzt-Behandlungen
*   d) Leistungsverzeichnis klinischer ambulanter Tarife

**Frage 3: Was ist die Hauptfunktion des LKAAT?**

*   a) Abrechnung der Leistungen
*   b) Leistungserfassung und Bestimmung des Abrechnungssystems ✓
*   c) Kostenkontrolle
*   d) Qualitätssicherung

**Frage 4: Wie viele Stellen hat eine LKN-Nummer für Pauschalen-Positionen?**

*   a) 7 Stellen
*   b) 8 Stellen
*   c) 9 Stellen ✓
*   d) 10 Stellen

**Frage 5: Wie wird die Vergütung bei TARDOC berechnet?**

*   a) Pauschalbetrag pro Fall
*   b) Taxpunkte × Taxpunktwert ✓
*   c) Zeitaufwand × Stundensatz
*   d) Nach Anzahl der Patienten

**Frage 6: Was ist der Hauptvorteil von Ambulanten Pauschalen für Leistungserbringer?**

*   a) Höhere Gesamtvergütung
*   b) Planungssicherheit und reduzierter administrativer Aufwand ✓
*   c) Keine Dokumentationspflicht
*   d) Freie Preisgestaltung

**Frage 7: Bei welcher Behandlung sollte TARDOC angewendet werden?**

*   a) Kataraktoperation
*   b) Arthroskopie
*   c) Routinekonsultation bei Bluthochdruck ✓
*   d) Koloskopie mit Polypektomie

**Frage 8: Was beinhaltet eine Ambulante Pauschale typischerweise NICHT?**

*   a) Anästhesieleistungen
*   b) Teure Spezialimplantate (als Zusatzentgelt separat) ✓
*   c) Standard-Verbrauchsmaterialien
*   d) Nachkontrollen

**Frage 9: 200 Taxpunkte × Taxpunktwert CHF 0.95 = ?**

*   a) CHF 185.00
*   b) CHF 190.00 ✓
*   c) CHF 195.00
*   d) CHF 200.00

**Frage 10: Dürfen TARDOC und Pauschalen im gleichen Behandlungsfall beliebig kombiniert werden?**

*   a) Ja, ohne Einschränkungen
*   b) Nein, grundsätzlich nicht (außer definierte Ausnahmen wie Zusatzentgelte) ✓
*   c) Ja, aber nur mit Zustimmung des Patienten
*   d) Nur bei Komplikationen jeder Art

**Frage 11: Was bedeutet "Dignität" im TARDOC-Kontext?**

*   a) Der Respekt gegenüber dem Patienten
*   b) Die Berechtigung zur Abrechnung bestimmter Leistungen ✓
*   c) Die Qualifikation des Pflegepersonals
*   d) Die Höhe der Vergütung

**Frage 12: Was sollte bei geplanten elektiven Eingriffen vorab eingeholt werden?**

*   a) Nur die Zustimmung des Patienten
*   b) Eine Kostengutsprache der Krankenkasse ✓
*   c) Eine ärztliche Zweitmeinung
*   d) Nur der OP-Termin

---

## FAQ - Häufig gestellte Fragen

BUTTON: FAQ  
TITEL: FAQ - Häufig gestellte Fragen

### Allgemeine Fragen zum System

**ACCORDION:**

**Was ist der Unterschied zwischen LKAAT, TARDOC und Ambulanten Pauschalen?**

*   **LKAAT** ist der Leistungskatalog zur **Erfassung** aller ambulanten Leistungen
*   **TARDOC** ist das Tarifsystem zur **Abrechnung** von Einzelleistungen
*   **Ambulante Pauschalen** sind das Tarifsystem zur **Abrechnung** komplexer Behandlungen als Gesamtpaket

Merkhilfe: LKAAT = Was wurde gemacht? TARDOC/Pauschalen = Wie wird abgerechnet?

**Wann wird welches Abrechnungssystem verwendet?**

Das System wird durch die erfasste Leistung im LKAAT bestimmt:

*   Wurde eine **Triggerposition (Typ P)** erfasst → Abrechnung über **Ambulante Pauschalen**
*   Wurden **nur Einzelleistungen (Typ E/EZ)** erfasst → Abrechnung über **TARDOC**

Die Entscheidung wird automatisch durch das System getroffen, sobald du die Leistung im LKAAT erfasst.

**Kann ich zwischen TARDOC und Pauschalen frei wählen?**

Nein. Die Wahl des Abrechnungssystems ist nicht beliebig:

*   Jede Leistung im LKAAT ist entweder als TARDOC-Position (E/EZ) oder als Pauschalen-Position (P/PZ) definiert
*   Diese Zuordnung kannst du nicht ändern
*   Das System bestimmt automatisch das korrekte Abrechnungssystem

**Was passiert, wenn ich eine Triggerposition übersehe?**

Dies führt zu einem Abrechnungsfehler:

*   Du rechnest fälschlicherweise über TARDOC ab, obwohl eine Pauschale anwendbar wäre
*   Die Rechnung kann von der Krankenkasse zurückgewiesen werden
*   Finanzielle Nachteile für deine Praxis/dein Spital

**Tipp:** Nutze den LKAAT plus Browser, der Triggerpositionen deutlich markiert.

### Fragen zu TARDOC

**ACCORDION:**

**Wie erkenne ich, ob eine Leistung über TARDOC abrechenbar ist?**

TARDOC-Leistungen haben im LKAAT:

*   Eine **8-stellige LKN-Nummer** (z.B. AA.00.0010)
*   Den **Typ E** (Einzelleistung) oder **EZ** (Zusatzleistung)
*   Eine Bewertung in **Taxpunkten**

**Was sind Taxpunkte und wie werden sie in Franken umgerechnet?**

*   Taxpunkte (TP) sind die Bewertungseinheit im TARDOC
*   Die Umrechnung erfolgt über den Taxpunktwert, der kantonal unterschiedlich ist
*   **Formel:** Vergütung = Taxpunkte × Taxpunktwert
*   **Beispiel:** 200 TP × CHF 0.95 = CHF 190.00

**Was bedeutet "Kumulation" bei TARDOC?**

Kumulation beschreibt, ob Leistungen zusammen am gleichen Tag abgerechnet werden können:

*   Manche Leistungen **schließen sich gegenseitig aus** (nicht kumulierbar)
*   Andere können **zusammen abgerechnet** werden (kumulierbar)
*   Die Kumulationsregeln sind im TARDOC definiert
*   Moderne Abrechnungssoftware prüft dies automatisch

**Muss ich bei TARDOC jede einzelne Minute dokumentieren?**

Ja und Nein:

*   Du musst die **erbrachten Leistungen** dokumentieren
*   Zeitbasierte Leistungen (z.B. Konsultationen) erfordern Zeitangaben
*   Bei nicht-zeitbasierten Leistungen (z.B. EKG) genügt die Dokumentation der Durchführung
*   **Best Practice:** Zeitaufwand immer notieren für Nachvollziehbarkeit

**Was ist "Dignität" und betrifft sie mich?**

Dignität bezeichnet die **Berechtigung zur Abrechnung** bestimmter Leistungen:

*   Nicht alle Ärzte dürfen alle TARDOC-Leistungen abrechnen
*   Manche Leistungen erfordern einen **Facharzttitel** oder **spezielle Qualifikation**
*   Prüfe im TARDOC, welche Dignität für eine Leistung erforderlich ist
*   Bei unberechtigter Abrechnung droht Rückforderung

### Fragen zu Ambulanten Pauschalen

**ACCORDION:**

**Wie erkenne ich, dass eine Pauschale anwendbar ist?**

Pauschalen werden durch **Triggerpositionen** ausgelöst:

*   **9-stellige LKN-Nummer** (z.B. C05.GB.0080)
*   **Typ P** (Pauschalen-Position) im LKAAT
*   Meist **chirurgische Eingriffe**, Endoskopien oder komplexe Diagnostik

Sobald du eine solche Position erfasst, rechnet das System automatisch über Pauschalen ab.

**Was ist alles in einer Pauschale inkludiert?**

Eine Pauschale deckt typischerweise ab:

*   Präoperative Voruntersuchungen
*   Der Eingriff/die Behandlung selbst
*   Anästhesieleistungen
*   Standard-Verbrauchsmaterialien
*   Postoperative Nachkontrollen (definierter Zeitraum)
*   Standard-Medikamente

**Nicht inkludiert** (separat abrechenbar als Zusatzentgelte):

*   Teure Spezialimplantate
*   Spezielle Medikamente (z.B. Biologika)
*   Nicht-standardmäßige Diagnostik

**Was sind Zusatzentgelte und wie rechne ich sie ab?**

Zusatzentgelte sind **definierte Zusatzkosten** zur Pauschale:

*   Teure Implantate (z.B. Premium-Linsen bei Katarakt-OP)
*   Spezielle Medikamente
*   Nur die im LKAAT definierten Zusatzentgelte sind abrechenbar
*   Werden **zusätzlich zur Pauschale** in Rechnung gestellt

**Wichtig:** Du kannst nicht beliebig Leistungen zusätzlich abrechnen!

**Was passiert bei Komplikationen während/nach dem Eingriff?**

Bei **erwartbaren Komplikationen:**

*   Diese sind durch die Pauschale abgedeckt
*   Keine zusätzliche Abrechnung möglich

Bei **schweren, unerwarteten Komplikationen:**

*   Dokumentiere den Sachverhalt genau
*   Kontaktiere ggf. den Kostenträger
*   In Ausnahmefällen kann eine Zusatzvergütung möglich sein

**Kann ich bei Pauschalen auch TARDOC-Leistungen zusätzlich abrechnen?**

Grundsätzlich **nein**:

*   Innerhalb desselben Behandlungsfalls keine Mischung
*   Ausnahme: Definierte Zusatzentgelte (keine TARDOC-Positionen!)
*   Bei separater Behandlung am gleichen Tag (anderes Capitulum, anderer Grund): Ja, dann ist eine zweite ambulante Behandlung möglich

### Fragen zu ICD-10-GM und Diagnosen

**ACCORDION:**

**Wann muss ich ICD-10-GM verwenden?**

**Verpflichtend:**

*   Bei allen Sitzungen mit **Triggerposition** (Ambulante Pauschalen)
*   Bei mehreren Sitzungen am gleichen Tag, wenn mindestens eine eine Triggerposition enthält

**Optional, aber empfohlen:**

*   Bei TARDOC-Abrechnung (alternativ: Tessinercode)

**Best Practice:** Verwende konsequent ICD-10-GM für alle Sitzungen.

**Wie finde ich den richtigen ICD-10-Code?**

Schrittweise Vorgehen:

1.  **Identifiziere** die Hauptdiagnose (größter Behandlungsaufwand)
2.  **Suche** im ICD-10-Katalog nach dem Organsystem (Kapitel A-Z)
3.  **Wähle** die spezifischste Kategorie
4.  **Erfasse** den endständigen Code (so detailliert wie möglich)

**Hilfsmittel:** ICD-10-Browser, Suchfunktion in deiner Praxissoftware

**Was ist der Unterschied zwischen endständig und nicht-endständig?**

*   **Endständig:** Detaillierteste Ebene der Klassifikation (z.B. J45.0)
*   **Nicht-endständig:** Übergeordnete Kategorie (z.B. J45)

**Ziel:** Immer den endständigen Code verwenden, soweit möglich. Nur in begründeten Ausnahmefällen nicht-endständige Codes.

**Wann erfasse ich Symptomcodes und wann Organdiagnosen?**

**Organdiagnose bevorzugen:**

*   Immer wenn zum Zeitpunkt der Behandlung eine Organdiagnose bekannt ist
*   **Beispiel:** J45.0 (Allergisches Asthma) statt R06.0 (Dyspnoe)

**Symptomcode nur wenn:**

*   Keine organbezogene Diagnose zum Zeitpunkt der Leistungserbringung verfügbar
*   **Beispiel:** Akute Bauchschmerzen ohne klare Ursache → R10.x

**Was mache ich bei Verdachtsdiagnosen?**

*   **Verdacht bestätigt sich:** Diagnose wird entsprechend dem aktuellen Wissensstand erfasst
*   **Verdacht wird ausgeschlossen:** Erfasse die Verdachtsdiagnose, da diese Anlass für die Untersuchung war
*   **Beispiel:** V.a. Appendizitis → nach Untersuchung ausgeschlossen → Dennoch K35.- erfassen

**Wichtig:** Du erfasst den Wissensstand **zum Zeitpunkt der Behandlung**, nicht Laborresultate von drei Tagen später!

### Fragen zur Praxisanwendung

**ACCORDION:**

**Wie organisiere ich meinen Workflow am besten?**

**Empfohlener Workflow:**

1.  **Bei Anmeldung:** Versicherungsstatus prüfen, Art der Behandlung klären
2.  **Vor Behandlung:** Ist eine Pauschale verfügbar? Kostengutsprache nötig?
3.  **Während Behandlung:** Leistungen zeitnah im LKAAT erfassen
4.  **Nach Behandlung:** Dokumentation vervollständigen, Diagnose erfassen
5.  **Vor Rechnungsstellung:** Plausibilitätsprüfung durchführen

**Was mache ich, wenn die Krankenkasse die Rechnung zurückweist?**

**Typische Gründe für Rückweisungen:**

*   Fehlende oder unvollständige Dokumentation
*   Falsches Abrechnungssystem verwendet
*   Kumulationsfehler bei TARDOC
*   Fehlende Kostengutsprache

**Vorgehen:**

1.  Rückweisungsgrund genau prüfen
2.  Fehlende Informationen ergänzen
3.  Dokumentation nachreichen
4.  Bei Unklarheiten: Kontakt mit Krankenkasse aufnehmen
5.  Rechnung korrigiert neu einreichen

**Wie halte ich mich über Änderungen auf dem Laufenden?**

**Informationsquellen:**

*   **FMH (Verbindung der Schweizer Ärztinnen und Ärzte):** Offizielle Informationen
*   **OAAT (Organisation ambulante Arzttarife):** Tarifupdates, Dokumentationen
*   **Ärztekasse:** Schulungen, Newsletter, LKAAT plus Browser
*   **Fachverbände:** Spezifische Informationen für deine Fachrichtung
*   **Praxissoftware-Anbieter:** Software-Updates mit neuen Tarifversionen

**Empfehlung:** Regelmäßige Schulungen für Mitarbeitende (mind. 1x jährlich)

**Benötige ich spezielle Software?**

**Mindestanforderungen:**

*   Abrechnungssoftware mit aktuellem LKAAT
*   Zugriff auf TARDOC- und Pauschalen-Katalog
*   ICD-10-GM Browser

**Empfehlenswert:**

*   Software mit automatischer Kumulationsprüfung
*   Plausibilitätschecks
*   LKAAT plus Browser für Recherchen
*   Elektronische Rechnungsstellung

**Was mache ich bei Unsicherheiten?**

**Anlaufstellen:**

*   **Trustcenter:** Neutrale Beratung zu Abrechnungsfragen
*   **Ärztekasse:** Tarifberatung für Mitglieder
*   **Fachverband:** Spezifische Fragen für deine Fachrichtung
*   **Kollegium:** Erfahrungsaustausch
*   **Kostenträger:** Bei Unklarheiten zur Kostenübernahme

**Grundsatz:** Lieber einmal zu viel nachfragen als eine falsche Rechnung stellen!

### Technische Fragen

**ACCORDION:**

**Was ist der LKAAT plus Browser?**

Der LKAAT plus Browser ist ein **Online-Tool** zur Tarifrecherche:

*   Umfassende Suchfunktionen für LKAAT-Leistungen
*   Zeigt an, welche Leistungen Pauschalen auslösen
*   Vergleich mit TARMED-Leistungen
*   ICD-10-Zuordnung zu Capitulum
*   Kostenlos verfügbar (Anbieter: Ärztekasse, FMH)

**Wie funktioniert die elektronische Rechnungsstellung?**

**Prozess:**

1.  Rechnung in deiner Praxissoftware erstellen
2.  Daten im standardisierten Format (XML) exportieren
3.  Übermittlung via gesichertem Kanal an Trustcenter oder Krankenkasse
4.  Automatische Plausibilitätsprüfung
5.  Zahlung auf dein Konto

**Vorteile:** Schneller, weniger Fehler, automatisierte Prozesse

**Welche Datenschutzbestimmungen muss ich beachten?**

**Bei der Rechnungsstellung:**

*   Übermittlung über verschlüsselte Kanäle
*   Bei Datenschutzbedenken: Verkürzte ICD-10-Codes möglich (mind. 1. Buchstabe)
*   Keine Weitergabe an Dritte ohne Einwilligung
*   Aufbewahrungspflicht: 10 Jahre

**Muss ich alte Rechnungen aufbewahren?**

Ja, die **Aufbewahrungspflicht** beträgt:

*   **10 Jahre** für Rechnungen und Behandlungsdokumentationen
*   Elektronisch oder in Papierform
*   Zugriff muss jederzeit möglich sein (bei Kontrollen)

### FAQ zu Übergangsregelungen

**ACCORDION:**

**Was ist mit meinen alten TARMED-Abrechnungen?**

*   TARDOC ist der **Nachfolger von TARMED**
*   Alte TARMED-Rechnungen bleiben gültig
*   Neue Rechnungen erfolgen über TARDOC
*   Viele TARDOC-Codes entsprechen TARMED-Codes (aber nicht alle!)
*   Nutze den LKAAT plus Browser für Vergleiche

**Gibt es noch Übergangsfristen?**

Die Übergangsfrist ist abgelaufen:

*   TARDOC und Ambulante Pauschalen sind seit 2025 vollständig in Kraft
*   Schulungen und Anlaufstellen stehen weiterhin zur Verfügung
*   Bei Fragen: Fachverbände und Trustcenter kontaktieren

---

## Ende der Content-Datei