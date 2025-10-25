# eLearning TAP - Content Source

**Version:** 1.1  
**Letzte Aktualisierung:** 2025-10-25  
**Zweck:** Diese Datei dient als zentrale Content-Quelle für eLearning.html

---

## Hinweise zur Nutzung

Diese Markdown-Datei enthält alle Inhalte der eLearning-Schulung in strukturierter Form. Sie können diese Datei manuell bearbeiten, um Inhalte zu erweitern oder anzupassen. Claude kann dann die `eLearning.html` Datei basierend auf Ihren Änderungen aktualisieren.

### Struktur-Konventionen:

*   **INFO-BOX**: Wird zu `<div class="info-box">` konvertiert
*   **INFO-BOX WARNUNG**: Wird zu `<div class="info-box warning">` konvertiert
*   **INFO-BOX SUCCESS**: Wird zu `<div class="info-box success">` konvertiert
*   **ACCORDION**: Wird zu `<div class="accordion">` konvertiert
*   **TABELLE**: Markdown-Tabellen werden zu HTML `<table>` konvertiert
*   **QUIZ**: Quiz-Fragen mit Antwortoptionen (✓ markiert die korrekte Antwort)

---

## Vorwort

### Willkommen zur eLearning-Schulung

Herzlich willkommen zu dieser umfassenden Schulung zum ambulanten Gesamt-Tarifsystem der Schweiz. Diese Schulung wurde entwickelt, um Ihnen ein fundiertes Verständnis der komplexen Strukturen und Prozesse der ambulanten Abrechnung zu vermitteln.

**INFO-BOX: Zielgruppe dieser Schulung**

*   Medizinisches Fachpersonal
*   Mitarbeitende in der Abrechnung und Kodierung
*   Zentrumsmanager:innen und Verwaltungspersonal
*   Alle, die mit der ambulanten Leistungserfassung und -abrechnung befasst sind

### Aufbau und Struktur

Diese Schulung ist in 9 Kapitel gegliedert, die aufeinander aufbauen und Sie Schritt für Schritt durch das Tarifsystem führen:

**ACCORDION:**

**Grundlagen (Kapitel 1-3)**

Sie lernen zunächst die Komponenten des Systems kennen, verstehen was ambulante Behandlungen sind und wie der LKAAT als zentrales Erfassungsinstrument funktioniert.

**Diagnosen und Abrechnungssysteme (Kapitel 4-6)**

Hier vertiefen Sie Ihr Wissen über die Diagnosecodierung mit ICD-10-GM, den TARDOC-Einzelleistungstarif und die Ambulanten Pauschalen.

**Vergleich und Praxis (Kapitel 7-8)**

Sie lernen die Unterschiede zwischen TARDOC und Pauschalen kennen und erhalten praxisnahe Anleitungen für den Arbeitsalltag.

**Abschlusstest**

Ein umfassender Test überprüft Ihr erworbenes Wissen über alle Kapitel hinweg.

### Wie Sie diese Schulung nutzen

**INFO-BOX SUCCESS: Lernempfehlungen**

*   Arbeiten Sie die Kapitel nacheinander durch
*   Nutzen Sie die INFO-Boxen für wichtige Hinweise
*   Öffnen Sie die Accordion-Bereiche für zusätzliche Details
*   Bearbeiten Sie die Quiz-Fragen am Ende jedes Kapitels
*   Machen Sie sich Notizen zu Unklarheiten
*   Nehmen Sie sich Zeit für den Abschlusstest

### Interaktive Elemente

In dieser Schulung finden Sie verschiedene didaktische Elemente:

**INFO-BOX: Verwendete Elemente**

*   **INFO-BOX:** Wichtige Informationen und Zusammenfassungen
*   **INFO-BOX WARNUNG:** Hinweise auf häufige Fehler und kritische Punkte
*   **INFO-BOX SUCCESS:** Best Practices und Erfolgstipps
*   **ACCORDION:** Zusätzliche Details, die Sie bei Bedarf ausklappen können
*   **TABELLE:** Übersichtliche Gegenüberstellungen
*   **QUIZ:** Wissensfragen zur Selbstkontrolle

### Zeitaufwand

Die gesamte Schulung dauert je nach Vorkenntnissen und Lerntempo etwa **3-4 Stunden**. Sie können die Schulung jederzeit unterbrechen und später fortsetzen. Ihr Fortschritt wird automatisch gespeichert.

**INFO-BOX: Geschätzter Zeitaufwand pro Kapitel**

*   Vorwort: 5 Minuten
*   Kapitel 1 (Einführung): 20 Minuten
*   Kapitel 2 (Ambulante Behandlung): 25 Minuten
*   Kapitel 3 (LKAAT): 25 Minuten
*   Kapitel 4 (ICD-10 Diagnosen): 30 Minuten
*   Kapitel 5 (TARDOC): 20 Minuten
*   Kapitel 6 (Ambulante Pauschalen): 20 Minuten
*   Kapitel 7 (Vergleich): 20 Minuten
*   Kapitel 8 (Praxisanwendung): 25 Minuten
*   Abschlusstest: 15 Minuten

### Lernziele der Gesamtschulung

Nach erfolgreichem Abschluss dieser Schulung sind Sie in der Lage:

*   Die Struktur und Komponenten des ambulanten Gesamt-Tarifsystems zu erklären
*   Ambulante von stationären Behandlungen abzugrenzen
*   Den LKAAT zur korrekten Leistungserfassung zu nutzen
*   Diagnosen korrekt nach ICD-10-GM zu codieren
*   TARDOC-Leistungen zu identifizieren und abzurechnen
*   Ambulante Pauschalen zu erkennen und anzuwenden
*   Das richtige Abrechnungssystem für verschiedene Behandlungssituationen auszuwählen
*   Häufige Fehlerquellen zu vermeiden und Best Practices anzuwenden

### Technische Voraussetzungen

**INFO-BOX: Was Sie benötigen**

*   Einen modernen Webbrowser (Chrome, Firefox, Safari, Edge)
*   Eine stabile Internetverbindung
*   Etwa 1 Stunde ungestörte Lernzeit
*   Optional: Notizblock für eigene Anmerkungen

### Support und Fragen

Bei Fragen oder technischen Problemen wenden Sie sich bitte an Ihre Schulungsverantwortlichen oder nutzen Sie die bereitgestellten Support-Kanäle.

**INFO-BOX SUCCESS: Bereit zu starten?**

Klicken Sie auf "Weiter", um mit Kapitel 1 zu beginnen. Wir wünschen Ihnen viel Erfolg beim Lernen!

---

## KAPITEL 1: Einführung in das ambulante Gesamt-Tarifsystem

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

Als Anwender:in müssen Sie verstehen, wann welches System anzuwenden ist. Eine falsche Zuordnung kann zu Abrechnungsfehlern und finanziellen Nachteilen führen.

### Lernziele dieses Moduls

Nach Abschluss dieser Schulung können Sie:

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

## KAPITEL 2: Ambulante Behandlung

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

## KAPITEL 3: LKAAT - Der Leistungskatalog

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

**INFO-BOX SUCCESS: So erkennen Sie den Unterschied**

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

## KAPITEL 4: Diagnosen als ICD-10 Code

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

## KAPITEL 5: TARDOC - Der Einzelleistungstarif

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

## KAPITEL 6: Ambulante Pauschalen (AP)

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

## KAPITEL 7: TARDOC vs. Ambulante Pauschalen - Der direkte Vergleich

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

## KAPITEL 8: Praxisanwendung und Best Practices

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

**INFO-BOX: Hinweise zum Abschlusstest**

Dieser Test umfasst 12 Fragen zu allen Kapiteln. Sie benötigen mindestens 10 von 12 richtigen Antworten, um die Schulung erfolgreich abzuschließen. Viel Erfolg!

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

## Ende der Content-Datei