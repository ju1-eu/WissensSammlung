---
title: "KI-Softwareentwicklung"
author: "Jan Unger"
date: "2024-10-12"
---

# KI-Assistenten in der Softwareentwicklung: ChatGPT und Claude

bearbeitet am 12. Oktober 2024

## Inhaltsverzeichnis
1. [Einleitung](#einleitung)
2. [Projektvorbereitung](#projektvorbereitung)
3. [Entwicklungsumgebung](#entwicklungsumgebung)
4. [Algorithmusentwicklung und Implementierung](#algorithmusentwicklung-und-implementierung)
5. [Dokumentation](#dokumentation)
6. [Qualitätssicherung](#qualitätssicherung)
7. [Visualisierung und Interaktivität](#visualisierung-und-interaktivität)
8. [Glossar](#glossar)

## Einleitung

Dieses Dokument dient als Leitfaden für fortgeschrittene Entwickler und KFZ-Technik-Meister zur effektiven Nutzung von KI-Assistenten (ChatGPT und Claude) in Softwareentwicklungsprojekten. Es deckt den gesamten Entwicklungsprozess ab, von der Projektvorbereitung bis zur Qualitätssicherung, mit Fokus auf Best Practices und moderne Technologien.

## Projektvorbereitung

### Überblick verschaffen und Projekt-/Ordnerstruktur erstellen

- Erstellen einer erweiterbaren Ordnerstruktur für zukünftige Kapitel
- Einbeziehung von Ressourcen für eine Makefile (mit Debug-Option)
- Verwendung von C++20
- Optimierung für macOS mit VSCode und Terminal

Beispiel für eine grundlegende Ordnerstruktur:

```
projekt/
│
├── src/
│   ├── main.cpp
│   └── algorithmus.cpp
│
├── include/
│   └── algorithmus.h
│
├── tests/
│   └── test_algorithmus.cpp
│
├── docs/
│   └── README.md
│
└── Makefile
```

## Entwicklungsumgebung

### VSCode-Konfiguration unter macOS

1. Anpassung der `c_cpp_properties.json`:

```json
{
    "configurations": [
        {
            "name": "Mac",
            "includePath": [
                "${workspaceFolder}/**"
            ],
            "defines": [],
            "macFrameworkPath": [
                "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/System/Library/Frameworks"
            ],
            "compilerPath": "/usr/bin/clang++",
            "cStandard": "c17",
            "cppStandard": "c++20",
            "intelliSenseMode": "macos-clang-x64"
        }
    ],
    "version": 4
}
```

2. Anpassung der `settings.json`, `tasks.json`, und `launch.json` (Details auf Anfrage)

### Makefile mit C++20 und Debug-Option

```makefile
CXX = g++
CXXFLAGS = -std=c++20 -Wall -Wextra
DEBUGFLAGS = -g

SRC_DIR = src
BUILD_DIR = build
TARGET = myprogram

SRCS = $(wildcard $(SRC_DIR)/*.cpp)
OBJS = $(patsubst $(SRC_DIR)/%.cpp,$(BUILD_DIR)/%.o,$(SRCS))

all: $(TARGET)

debug: CXXFLAGS += $(DEBUGFLAGS)
debug: all

$(TARGET): $(OBJS)
    $(CXX) $(CXXFLAGS) -o $@ $^

$(BUILD_DIR)/%.o: $(SRC_DIR)/%.cpp | $(BUILD_DIR)
    $(CXX) $(CXXFLAGS) -c -o $@ $<

$(BUILD_DIR):
    mkdir -p $@

clean:
    rm -rf $(BUILD_DIR) $(TARGET)

.PHONY: all debug clean
```

## Algorithmusentwicklung und Implementierung

### Schritte zur Algorithmusentwicklung

1. Problem definieren
2. Algorithmus entwerfen (Pseudocode oder Struktogramm)
3. Implementierung in C++20
4. Testen und Optimieren

### Beispiel: Einfacher Sortieralgorithmus (Bubble Sort)

```cpp
#include <vector>

void bubbleSort(std::vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                std::swap(arr[j], arr[j+1]);
            }
        }
    }
}
```

## Dokumentation

### Strukturierte Darstellung erstellen

1. Struktogramm im ASCII-Art-Stil
2. C++-Code mit deutschen Kommentaren
3. Codeerklärung
4. Erläuterung wichtiger Konzepte
5. Mathematische Grundlagen
6. Anwendungsbeispiele
7. MindMap zur Projektdokumentation

### Beispiel: Struktogramm für Bubble Sort (ASCII-Art)

```
┌─────────────────────────────────────┐
│ Bubble Sort                         │
├─────────────────────────────────────┤
│ Eingabe: Array arr mit n Elementen  │
├─────────────────────────────────────┤
│ Für i = 0 bis n-2                   │
│  ┌───────────────────────────────┐  │
│  │ Für j = 0 bis n-i-2           │  │
│  │  ┌───────────────────────────┐│  │
│  │  │ Wenn arr[j] > arr[j+1]    ││  │
│  │  │  ┌────────────────────┐   ││  │
│  │  │  │ Tausche arr[j] und │   ││  │
│  │  │  │ arr[j+1]           │   ││  │
│  │  │  └────────────────────┘   ││  │
│  │  └───────────────────────────┘│  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

## Qualitätssicherung

1. Code-Review durchführen
2. Unittests implementieren
3. Statische Code-Analyse durchführen
4. Performanztests durchführen
5. Dokumentation auf Vollständigkeit und Klarheit prüfen

### Beispiel: Unittest für Bubble Sort

```cpp
#include <gtest/gtest.h>
#include "sort.h"

TEST(BubbleSortTest, SortsCorrectly) {
    std::vector<int> input = {5, 2, 8, 12, 1, 6};
    std::vector<int> expected = {1, 2, 5, 6, 8, 12};
    
    bubbleSort(input);
    
    EXPECT_EQ(input, expected);
}
```

## Visualisierung und Interaktivität

### Interaktive Visualisierung mit Python

```python
import matplotlib.pyplot as plt
import numpy as np

def visualize_bubble_sort(arr):
    n = len(arr)
    fig, ax = plt.subplots()
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
            plt.cla()
            plt.bar(range(n), arr)
            plt.pause(0.1)
    
    plt.show()

# Beispielaufruf
arr = np.random.randint(1, 100, 20)
visualize_bubble_sort(arr)
```

## Glossar

- **Algorithmus**: Eine Schritt-für-Schritt-Anleitung zur Lösung eines Problems oder zur Durchführung einer Aufgabe.
- **C++20**: Die im Jahr 2020 standardisierte Version der Programmiersprache C++.
- **Makefile**: Eine Datei, die Anweisungen für das Build-Automatisierungstool 'make' enthält.
- **Struktogramm**: Eine grafische Darstellung eines Algorithmus, auch bekannt als Nassi-Shneiderman-Diagramm.
- **Unittest**: Ein automatisierter Test, der eine spezifische Funktion oder Methode eines Programms überprüft.
- **VSCode**: Visual Studio Code, eine quelloffene Entwicklungsumgebung von Microsoft.