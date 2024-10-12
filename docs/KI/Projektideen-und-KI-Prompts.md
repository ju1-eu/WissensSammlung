---
title: "Projektideen und KI-Prompts"
author: "Jan Unger"
date: "2024-09-29"
---

# Projektideen und KI-Prompts

bearbeitet am 12. Oktober 2024

- [Projektideen und KI-Prompts](#projektideen-und-ki-prompts)
  - [Einleitung](#einleitung)
  - [Textbearbeitung und Analyse](#textbearbeitung-und-analyse)
    - [Dokumentzusammenfassung und -analyse](#dokumentzusammenfassung-und--analyse)
    - [SQ3R-Methode für technische Texte](#sq3r-methode-für-technische-texte)
  - [Code-Bearbeitung und Softwareentwicklung](#code-bearbeitung-und-softwareentwicklung)
    - [Code-Überprüfung und -Verbesserung](#code-überprüfung-und--verbesserung)
    - [Projektorientierte Entwicklung](#projektorientierte-entwicklung)
  - [Mathematik und Visualisierung](#mathematik-und-visualisierung)
    - [Mathematische Konzepte und Anwendungen](#mathematische-konzepte-und-anwendungen)
    - [Datenvisualisierung](#datenvisualisierung)
  - [Projektmanagement](#projektmanagement)
    - [SMART-Ziele für technische Projekte](#smart-ziele-für-technische-projekte)
    - [Kanban-Board für Softwareentwicklung](#kanban-board-für-softwareentwicklung)
  - [Lernstrategien](#lernstrategien)
    - [Feynman-Methode für technische Konzepte](#feynman-methode-für-technische-konzepte)
    - [Pomodoro-Technik für effizientes Lernen](#pomodoro-technik-für-effizientes-lernen)
  - [Kommunikationsrichtlinien](#kommunikationsrichtlinien)
  - [Glossar](#glossar)

## Einleitung

Dieses Dokument dient als umfassender Leitfaden zur effektiven Nutzung von KI-Assistenten in verschiedenen Bereichen der Softwareentwicklung, des technischen Lernens und der Textbearbeitung. Es integriert praxisnahe Beispiele aus der Softwareentwicklung und KFZ-Technik.

## Textbearbeitung und Analyse

### Dokumentzusammenfassung und -analyse

1. Kernkonzepte identifizieren und erläutern:
   - Beispiel (Softwareentwicklung): Objektorientierte Programmierung, Datenstrukturen, Algorithmen
   - Beispiel (KFZ-Technik): Motormanagement, Fahrzeugdiagnose, Antriebssysteme

2. Strukturierte Zusammenfassung erstellen:
   - Verwendung von Markdown und LaTeX für mathematische Formeln
   - Beispiel:
     ```markdown
     ## Motormanagement in modernen Fahrzeugen
     
     1. Elektronische Steuergeräte (ECU)
     2. Sensordatenerfassung und -verarbeitung
     3. Kraftstoffeinspritzung und Zündungssteuerung
     4. Abgasnachbehandlung
     
     Die Effizienz eines Motors kann durch die Formel $\eta = \frac{P_{out}}{P_{in}}$ beschrieben werden, wobei $\eta$ der Wirkungsgrad, $P_{out}$ die Nutzleistung und $P_{in}$ die zugeführte Leistung ist.
     ```

3. Themenreflexion:
   - Identifizierung von 3-5 Hauptkonzepten
   - Diskussion von Anwendungen und Auswirkungen
   - Beispiel: Auswirkungen der Elektrifizierung auf traditionelle Verbrennungsmotoren-Expertise

### SQ3R-Methode für technische Texte

1. Survey (Überblick):
   - Schnelles Scannen von Überschriften, Abbildungen und Zusammenfassungen
   - Beispiel: Überblick über ein technisches Handbuch für eine neue Fahrzeugdiagnose-Software

2. Question (Fragen stellen):
   - Formulierung von Fragen zu jedem Abschnitt
   - Beispiel: "Wie integriert sich diese Diagnose-Software in bestehende Werkstattsysteme?"

3. Read (Lesen):
   - Aktives Lesen mit Fokus auf die formulierten Fragen
   - Markieren wichtiger Passagen und Fachbegriffe

4. Recite (Wiedergeben):
   - Zusammenfassung der Hauptaussagen in eigenen Worten
   - Anwendung der Feynman-Technik zur Erklärung komplexer Konzepte

5. Review (Überprüfen):
   - Überprüfung des Verständnisses durch Beantwortung der anfänglichen Fragen
   - Identifikation von Wissenslücken für weitere Recherche

## Code-Bearbeitung und Softwareentwicklung

### Code-Überprüfung und -Verbesserung

1. Codequalität bewerten:
   - Lesbarkeit, Modularität, Effizienz
   - Beispiel: Überprüfung eines Python-Skripts zur Datenanalyse von Fahrzeugsensoren

2. Verbesserungsvorschläge priorisieren:
   - Fokus auf kritische Performanceprobleme und Sicherheitslücken
   - Beispiel:
     ```python
     # Vorher: Ineffiziente Datenverarbeitung
     for sensor_data in large_dataset:
         process_data(sensor_data)
     
     # Nachher: Optimierte Verarbeitung mit Multithreading
     from concurrent.futures import ThreadPoolExecutor
     
     with ThreadPoolExecutor() as executor:
         executor.map(process_data, large_dataset)
     ```

### Projektorientierte Entwicklung

1. Projektstruktur erstellen:
   - Einrichtung eines Git-Repositories
   - Erstellung eines Kanban-Boards für Aufgabenverwaltung

2. Modularer Aufbau von Projekten:
   - Unterteilung in kleinere, aufeinander aufbauende Module
   - Beispiel: Entwicklung eines Fahrzeugdiagnose-Tools
     - Modul 1: OBD-II-Schnittstelle
     - Modul 2: Datenerfassung und -speicherung
     - Modul 3: Datenanalyse und Fehlererkennung
     - Modul 4: Benutzeroberfläche

3. Implementierung und Testing:
   - Schrittweise Umsetzung der Programmlogik
   - Kontinuierliche Integration und Testing
   - Beispiel: Unit-Tests für OBD-II-Kommunikationsmodul

4. Dokumentation:
   - Erstellung von Codekommentaren und Docstrings
   - Verfassen eines umfassenden README.md

## Mathematik und Visualisierung

### Mathematische Konzepte und Anwendungen

1. Rechenbeispiele mit Bezug zur KFZ-Technik:
   - Beispiel: Berechnung des Kraftstoffverbrauchs
     ```latex
     \text{Kraftstoffverbrauch} = \frac{\text{verbrauchter Kraftstoff (L)}}{\text{zurückgelegte Strecke (km)}} \times 100
     ```

2. Formelsammlung für technische Berechnungen:
   - Beispiel: Formel für die Berechnung der Motorleistung
     ```latex
     P = \frac{2\pi \cdot n \cdot M}{60}
     ```
     wobei P die Leistung in Watt, n die Drehzahl in U/min und M das Drehmoment in Nm ist.

### Datenvisualisierung

1. Erstellung von Diagrammen mit Python:
   - Verwendung von Matplotlib oder Seaborn für technische Visualisierungen
   - Beispiel: Visualisierung von Motordrehzahl vs. Kraftstoffverbrauch
     ```python
     import matplotlib.pyplot as plt
     
     rpm = [1000, 2000, 3000, 4000, 5000]
     fuel_consumption = [5, 7, 10, 15, 22]
     
     plt.plot(rpm, fuel_consumption)
     plt.xlabel('Motordrehzahl (U/min)')
     plt.ylabel('Kraftstoffverbrauch (L/100km)')
     plt.title('Drehzahl vs. Kraftstoffverbrauch')
     plt.show()
     ```

## Projektmanagement

### SMART-Ziele für technische Projekte

- Spezifisch: Entwicklung eines OBD-II-Diagnosesystems für Elektrofahrzeuge
- Messbar: Unterstützung von mindestens 10 gängigen Elektrofahrzeugmodellen
- Attraktiv: Ermöglicht effizientere Fehlerdiagnose in Werkstätten
- Realistisch: Nutzung vorhandener OBD-II-Bibliotheken und Expertenwissen
- Terminiert: Fertigstellung innerhalb von 6 Monaten

### Kanban-Board für Softwareentwicklung

| To-Do                 | In Bearbeitung (max. 3)    | Erledigt                        |
| --------------------- | -------------------------- | ------------------------------- |
| GUI-Design            | OBD-II-Kommunikationsmodul | Projektplanung                  |
| Datenbank-Integration | Fehlercodeinterpretation   | Anforderungsanalyse             |
| Benutzerdokumentation |                            | Entwicklungsumgebung einrichten |

## Lernstrategien

### Feynman-Methode für technische Konzepte

1. Komplexes Thema auswählen: z.B. Common-Rail-Einspritzsystem
2. Einfache Erklärung formulieren:
   "Ein Common-Rail-System ist wie ein zentraler Hochdruckspeicher für Kraftstoff. Stell dir vor, du hättest einen Wassertank unter Druck, aus dem mehrere Sprinkler gleichzeitig und präzise gesteuert Wasser verteilen können. So ähnlich funktioniert das Common-Rail-System mit Kraftstoff für die Zylinder eines Motors."

3. Identifizierung von Verständnislücken:
   - Genaue Druckverhältnisse
   - Steuerungsmechanismen der Einspritzventile

4. Vertiefung des Wissens und Überarbeitung der Erklärung

### Pomodoro-Technik für effizientes Lernen

- Arbeitsblöcke: 2-3 x 2 Stunden
- Struktur: 4 x (25 Minuten Arbeit + 5 Minuten Pause)
- Lange Pause: 20-30 Minuten zwischen Blöcken

Beispiel-Tagesplan für das Erlernen neuer Fahrzeugtechnologien:

1. Block: Theorie zu Hybrid-Antriebssystemen
2. Block: Praktische Übungen an Simulationsmodellen
3. Block: Problemlösung und Fehlerdiagnose

## Kommunikationsrichtlinien

Bei der Kommunikation über technische Themen:

- Sachlichen und neutralen Stil verwenden
- Fachbegriffe präzise einsetzen und bei Bedarf erklären
- Beispiele aus der Softwareentwicklung und KFZ-Technik zur Veranschaulichung nutzen
- Wissenschaftlichen Stil mit klarer Struktur und Quellenangaben anwenden
- Interdisziplinäre Verbindungen herstellen (z.B. zwischen Softwareentwicklung und Fahrzeugelektronik)

## Glossar

- **ECU (Electronic Control Unit)**: Elektronisches Steuergerät in Fahrzeugen zur Kontrolle verschiedener Subsysteme
- **OBD-II (On-Board Diagnostics II)**: Standardisiertes Fahrzeugdiagnosesystem
- **Common-Rail-Einspritzsystem**: Hochdruckeinspritzsystem für Dieselmotoren mit einem gemeinsamen Druckspeicher
- **Kanban**: Methode zur Prozesssteuerung in der Softwareentwicklung und Produktion
- **Pomodoro-Technik**: Zeitmanagementmethode mit festgelegten Arbeits- und Pausenintervallen
- **SMART-Ziele**: Akronym für spezifische, messbare, attraktive, realistische und terminierte Ziele