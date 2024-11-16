---
title: Softwareentwicklung-Richtlinien
---

# Systematischer Ansatz zur Softwareentwicklung - Richtlinien

Letzte Aktualisierung: 2024-11-16

Diese drei Phasen bilden zusammen einen systematischen Ansatz zur Softwareentwicklung, bei dem zuerst das Problem vollständig verstanden und dann schrittweise in eine technische Lösung überführt wird.

- [Systematischer Ansatz zur Softwareentwicklung - Richtlinien](#systematischer-ansatz-zur-softwareentwicklung---richtlinien)
  - [Phase 1: Fragen – Rechnen – Verstehen](#phase-1-fragen--rechnen--verstehen)
    - [1. Fragen](#1-fragen)
    - [2. Rechnen](#2-rechnen)
    - [3. Verstehen](#3-verstehen)
  - [Phase 2: Algorithmus – Struktogramm – Implementieren](#phase-2-algorithmus--struktogramm--implementieren)
    - [1. Algorithmus](#1-algorithmus)
    - [2. Struktogramm](#2-struktogramm)
    - [3. Implementieren](#3-implementieren)
    - [Herausforderungen und Beachtenswertes](#herausforderungen-und-beachtenswertes)
    - [Nassi-Shneiderman-Diagramm (Struktogramm) mit Mermaid](#nassi-shneiderman-diagramm-struktogramm-mit-mermaid)
      - [Grundprinzip](#grundprinzip)
      - [Hauptelemente](#hauptelemente)
      - [Vorteile](#vorteile)
      - [Anwendungsbereiche](#anwendungsbereiche)
      - [Standardisierung und Verbreitung](#standardisierung-und-verbreitung)
      - [Besonderheiten](#besonderheiten)
    - [Implementieren](#implementieren)
  - [Phase 3: Prüfung des Python-Skripts](#phase-3-prüfung-des-python-skripts)
    - [Sinnvoller Dateiname](#sinnvoller-dateiname)
    - [Code-Qualität](#code-qualität)
    - [Benutzerfreundlichkeit](#benutzerfreundlichkeit)
    - [Code Refactoring](#code-refactoring)
    - [Berechnungsgenauigkeit](#berechnungsgenauigkeit)
    - [Dokumentation](#dokumentation)
    - [Plausibilität](#plausibilität)
  - [systematischer Ansatz zur Softwareentwicklung](#systematischer-ansatz-zur-softwareentwicklung)
    - [Phasen des Software-Lebenszyklus](#phasen-des-software-lebenszyklus)
    - [Vorgehensmodelle](#vorgehensmodelle)
      - [Klassische Modelle](#klassische-modelle)
      - [Agile Modelle](#agile-modelle)
      - [Hybride Ansätze](#hybride-ansätze)
    - [Prinzipien](#prinzipien)
    - [Methoden und Praktiken](#methoden-und-praktiken)

## Phase 1: Fragen – Rechnen – Verstehen

Die Phase "Fragen – Rechnen – Verstehen" beschreibt einen grundlegenden analytischen Problemlösungsprozess.

### 1. Fragen

In dieser ersten Stufe geht es darum, das Problem zu definieren und relevante Informationen zu sammeln:

- Problemstellung präzise formulieren
- Kernfragen identifizieren
- Annahmen hinterfragen
- Relevante Daten und Informationen sammeln
- Randbedingungen und Einschränkungen erfassen

### 2. Rechnen

Diese Stufe beinhaltet die quantitative Analyse und Berechnung:

- Geeignete mathematische Modelle auswählen
- Daten aufbereiten und bereinigen
- Berechnungen durchführen
- Statistische Analysen anwenden
- Simulationen erstellen (falls erforderlich)
- Ergebnisse visualisieren (z.B. Graphen, Diagramme)

### 3. Verstehen

In der letzten Stufe werden die Ergebnisse interpretiert und in einen größeren Kontext eingeordnet:

- Ergebnisse kritisch hinterfragen
- Muster und Trends identifizieren
- Zusammenhänge zwischen verschiedenen Faktoren erkennen
- Schlussfolgerungen ziehen
- Implikationen für die Praxis ableiten
- Grenzen der Analyse erkennen

Durch die systematische Anwendung von "Fragen – Rechnen – Verstehen" können komplexe Probleme effektiv analysiert und gelöst werden. Dieser Prozess ermöglicht es, von der initialen Problemstellung über die quantitative Analyse bis hin zu einem tiefgreifenden Verständnis und praktischen Implikationen zu gelangen.

## Phase 2: Algorithmus – Struktogramm – Implementieren

Die Phase "Algorithmus – Struktogramm – Implementieren" beschreibt den technischen Umsetzungsprozess in der Softwareentwicklung. Hier ist eine detaillierte Erläuterung dieser Phase:

### 1. Algorithmus

In diesem ersten Schritt wird die logische Lösung des Problems entwickelt:

- Problemstellung in einzelne Schritte zerlegen
- Logische Abfolge der Schritte festlegen
- Entscheidungspunkte und Verzweigungen identifizieren
- Schleifen und Wiederholungen definieren
- Effizienz und Komplexität berücksichtigen

### 2. Struktogramm

Das Struktogramm (auch Nassi-Shneiderman-Diagramm genannt) visualisiert den Algorithmus:

- Grafische Darstellung des Kontroll- und Datenflusses
- Verwendung standardisierter Symbole:
  - Rechtecke für Anweisungen
  - Rauten für Verzweigungen
  - Schleifen-Symbole für Wiederholungen
- Hierarchische Strukturierung des Algorithmus
- Förderung der Übersichtlichkeit und Lesbarkeit

### 3. Implementieren

In dieser Phase wird der Algorithmus in Programmcode umgesetzt:

- Auswahl der geeigneten Programmiersprache
- Umsetzung der Struktogramm-Elemente in Code
- Implementierung von Datenstrukturen
- Einhaltung von Coding-Standards und Best Practices
- Kommentierung des Codes für bessere Verständlichkeit
- Modularisierung und Strukturierung des Codes

### Herausforderungen und Beachtenswertes

- Konsistenz zwischen Algorithmus, Struktogramm und Code sicherstellen
- Anpassung an sich ändernde Anforderungen berücksichtigen
- Balance zwischen detaillierter Planung und flexibler Umsetzung finden

Dieser dreistufige Prozess "Algorithmus – Struktogramm – Implementieren" ermöglicht eine strukturierte und nachvollziehbare Umsetzung von der konzeptionellen Lösung bis zum fertigen Code. Er fördert klares Denken, saubere Strukturierung und effiziente Implementierung in der Softwareentwicklung.

### Nassi-Shneiderman-Diagramm (Struktogramm) mit Mermaid

Das Nassi-Shneiderman-Diagramm, auch als Struktogramm bekannt, ist eine grafische Darstellungsmethode für strukturierte Programmierung.

#### Grundprinzip

- Entwickelt 1972 von Isaac Nassi und Ben Shneiderman
- Zeigt die Struktur eines Programms oder Algorithmus
- Verwendet verschachtelte Kästen zur Darstellung von Teilproblemen

#### Hauptelemente

1. **Prozessblöcke**: Einfache Anweisungen ohne weitere Analyse
2. **Verzweigungsblöcke**: 
   - Einfache Ja/Nein-Verzweigungen
   - Mehrfachverzweigungen für Fallunterscheidungen
3. **Schleifenblöcke**:
   - Test-First: Bedingung wird vor der Ausführung geprüft
   - Test-Last: Bedingung wird nach der Ausführung geprüft
4. **Parallele Ausführung**: Darstellung nebeneinander liegender Blöcke

#### Vorteile

- Klare Darstellung von Algorithmen und Programmstrukturen
- Keine Darstellung von GOTO-Anweisungen (strukturierte Programmierung)
- Förderung des Top-Down-Designs
- Nützlich für Lehrzwecke und Algorithmenvisualisierung

#### Anwendungsbereiche

- Softwareentwicklung und Algorithmendesign
- Lehre der Programmierung
- Technisches Schreiben und Dokumentation

#### Standardisierung und Verbreitung

- In Deutschland als DIN 66261 standardisiert (1985)
- Häufig in deutschen Programmiereinführungen verwendet

#### Besonderheiten

- Abstraktionsniveau nahe an strukturiertem Programmcode
- Erfordert Neuzeichnung bei Änderungen (Nachteil bei manueller Erstellung)
- Grafische Editoren haben diese Einschränkung weitgehend beseitigt

Struktogramme bieten eine übersichtliche und strukturierte Methode zur Visualisierung von Algorithmen und Programmabläufen. Sie sind besonders nützlich für die Planung und Dokumentation von Software sowie für didaktische Zwecke in der Programmierausbildung.


### Implementieren

Um die beschriebenen Strukturen in Python-Programmcode zu übersetzen, die Funktionalität zu implementieren und zu testen, können wir folgende Schritte durchführen:

1. Implementierung der Strukturen
   - Basierend auf den gegebenen Codebeispielen können wir eine Funktion und eine Klasse implementieren:

2. Funktionalität testen
   - Um die implementierte Funktionalität zu testen, führen wir Beispielaufrufe durch:

3. Ausführung und Überprüfung
   - Die Ausführung des Codes liefert folgende Ergebnisse:

   - Diese Ausgabe zeigt, dass sowohl die Funktion als auch die Klasse korrekt implementiert wurden und wie erwartet funktionieren.

4. Erweiterungsmöglichkeiten
   - Je nach Anforderungen könnten weitere Funktionen oder Methoden hinzugefügt werden. Zum Beispiel:

5. Zusätzliche Tests
   - Um die Robustheit des Codes zu gewährleisten, könnten weitere Tests implementiert werden.

## Phase 3: Prüfung des Python-Skripts

### Sinnvoller Dateiname

- Wählen Sie einen beschreibenden, aber knappen Namen
- Beispiel: `data_analysis_tool.py` oder `inventory_management.py`
- Verwenden Sie Unterstriche für Worttrennungen (Snake Case)

### Code-Qualität

- Überprüfen Sie die Einhaltung von PEP 8 (Python Style Guide)
- Nutzen Sie Tools wie `pylint` oder `flake8`
- Achten Sie auf konsistente Einrückung und Formatierung
- Vermeiden Sie unnötige Komplexität und Redundanz

### Benutzerfreundlichkeit

- Implementieren Sie klare Benutzerführung
- Fügen Sie hilfreiche Fehlermeldungen hinzu
- Bieten Sie sinnvolle Standardwerte an

### Code Refactoring

- Identifizieren Sie wiederholten Code und extrahieren Sie ihn in Funktionen
- Verbessern Sie die Lesbarkeit durch aussagekräftige Variablen- und Funktionsnamen
- Optimieren Sie die Struktur für bessere Wartbarkeit

### Berechnungsgenauigkeit

- Verwenden Sie geeignete Datentypen für präzise Berechnungen
- Berücksichtigen Sie Rundungsfehler bei Fließkommazahlen
- Implementieren Sie Unit-Tests für kritische Berechnungen

### Dokumentation

- Fügen Sie Docstrings zu Funktionen und Klassen hinzu
- Kommentieren Sie komplexe Codeabschnitte
- Erstellen Sie eine README-Datei mit Übersicht, Installation und Nutzungsanleitung

### Plausibilität

- Überprüfen Sie die Ergebnisse auf Plausibilität
- Implementieren Sie Grenzwertprüfungen
- Fügen Sie Logging für wichtige Zwischenschritte hinzu

## systematischer Ansatz zur Softwareentwicklung

### Phasen des Software-Lebenszyklus

Der Software-Lebenszyklus lässt sich in folgende Hauptphasen unterteilen:

1. Anforderungsanalyse und Spezifikation
2. Design und Architektur  
3. Implementierung/Programmierung
4. Testen und Integration
5. Auslieferung und Einführung
6. Wartung und Support

Diese Phasen werden je nach gewähltem Vorgehensmodell sequentiell oder iterativ durchlaufen.

### Vorgehensmodelle

Es gibt verschiedene Vorgehensmodelle für die systematische Softwareentwicklung:

#### Klassische Modelle

- Wasserfallmodell: Sequentieller Ablauf der Phasen
- V-Modell: Erweiterung des Wasserfallmodells mit Qualitätssicherung

#### Agile Modelle  

- Scrum: Iterative Entwicklung in Sprints
- Extreme Programming (XP): Fokus auf Kundenzufriedenheit und Teamarbeit
- Kanban: Kontinuierlicher Fluss der Arbeit

#### Hybride Ansätze

Kombinieren klassische und agile Elemente je nach Projektanforderungen.

### Prinzipien

Wichtige Prinzipien für eine systematische Entwicklung sind:

- Modularität und Wiederverwendbarkeit
- Trennung von Verantwortlichkeiten  
- Abstraktion und Kapselung
- Iterative Verbesserung
- Kontinuierliche Integration und Auslieferung
- Automatisiertes Testen

### Methoden und Praktiken

- Anforderungsmanagement
- Softwarearchitektur 
- Versionskontrolle
- Code-Reviews
- Testautomatisierung
- Continuous Integration/Delivery
- Agile Praktiken wie Daily Standups, Retrospektiven etc.

Ein systematischer Ansatz kombiniert diese Elemente, um eine strukturierte, effiziente und qualitativ hochwertige Softwareentwicklung zu ermöglichen. Die konkrete Ausgestaltung hängt von den spezifischen Projektanforderungen und Rahmenbedingungen ab.
