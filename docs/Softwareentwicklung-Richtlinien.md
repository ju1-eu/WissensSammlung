---
title: Softwareentwicklung-Richtlinien
---

# Systematischer Ansatz zur Softwareentwicklung - Richtlinien

Diese drei Phasen bilden zusammen einen systematischen Ansatz zur Softwareentwicklung, bei dem zuerst das Problem vollständig verstanden und dann schrittweise in eine technische Lösung überführt wird.

- [Systematischer Ansatz zur Softwareentwicklung - Richtlinien](#systematischer-ansatz-zur-softwareentwicklung---richtlinien)
  - [Phase 1: Fragen – Rechnen – Verstehen](#phase-1-fragen--rechnen--verstehen)
    - [Fragen](#fragen)
    - [Rechnen](#rechnen)
    - [Verstehen](#verstehen)
  - [Phase 2: Algorithmus – Struktogramm – Implementieren](#phase-2-algorithmus--struktogramm--implementieren)
    - [Algorithmus](#algorithmus)
    - [Struktogramm](#struktogramm)
      - [Nassi-Shneiderman-Diagramm (Struktogramm) mit Mermaid](#nassi-shneiderman-diagramm-struktogramm-mit-mermaid)
    - [Implementieren](#implementieren)
  - [Phase 3: Prüfe Python-Skript](#phase-3-prüfe-python-skript)

## Phase 1: Fragen – Rechnen – Verstehen

Dies beschreibt den analytischen Problemlösungsprozess.

### Fragen

- Das Problem präzise definieren.
- Die Anforderungen klären.
- Die Ein- und Ausgabewerte identifizieren.

### Rechnen

- Beispielrechnungen durchführen.
- Die mathematischen Zusammenhänge ermitteln, beispielsweise Funktionen $f(x)$, Gleichungen oder Algorithmen.
- Die Lösungswege überprüfen.

### Verstehen

- Die zugrunde liegende Logik erfassen.
- Muster und Strukturen erkennen.
- Den Lösungsansatz validieren.

## Phase 2: Algorithmus – Struktogramm – Implementieren

Dies beschreibt den technischen Umsetzungsprozess.

### Algorithmus

- Die Verarbeitungsschritte entwickeln.
- Die Ablauflogik festlegen.
- Kontrollstrukturen definieren, wie Schleifen und Verzweigungen.

### Struktogramm

- Den Algorithmus visualisieren.
- Die Programmstruktur darstellen.
- Verzweigungen und Schleifen abbilden.

*Ein Struktogramm ist eine grafische Methode zur Darstellung von Algorithmen, die die Programmstruktur mit Sequenzen, Verzweigungen und Schleifen visualisiert.*

#### Nassi-Shneiderman-Diagramm (Struktogramm) mit Mermaid

NASSI-SHNEIDERMAN MERMAID TEMPLATE:

1. Grundstruktur
```mermaid
flowchart TB
    classDef default fill:none,stroke:#000
```

2. Formatierung:
   - direction TB für Hauptablauf (Top->Bottom)
   - Blöcke: direction LR für horizontale Anordnungen
   - style für alle subgraphs: fill:none,stroke:#000
   - Verbindungen innerhalb Blöcke mit ---
   - Ablaufpfeile zwischen Blöcken mit -->

3. Block-Template:
```
    subgraph BlockName["Titel"]
        direction LR
        Element1["Text1"] --- Element2["Text2"]
        style BlockName fill:none,stroke:#000
    end
```

4. Wichtige Eigenschaften:
   - Klare Hierarchie der Blöcke
   - Einheitliche Rechteckform
   - Keine Füllfarben
   - Mathematische Formeln in ["..."]
   - Zweizeilige Anordnung für lange Berechnungsketten
   - Zentrierung der Blöcke

5. Beispielanwendung: Sturz-Simulation mit 5 Hauptblöcken:
   - Parameter einlesen
   - Phase 1: Freier Fall
   - Phase 2: Abbremsung 
   - Bewegungsdaten generieren
   - Ergebnisausgabe


### Implementieren

- In Python-Programmcode übersetzen.
- Die Strukturen umsetzen.
- Die Funktionalität testen.

## Phase 3: Prüfe Python-Skript

- sinnvollen Dateinamen
- Code-Qualität
- Benutzerfreundlichkeit
- Code Refactoring
- Berechnungsgenauigkeit
- Dokumentation
- Plausibilität
