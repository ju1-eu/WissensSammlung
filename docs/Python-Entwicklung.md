---
title: Python-Entwicklung
---

# Python installieren

```bash
brew update
brew install python
brew upgrade python

echo $PATH
which python3
python --version
source ~/.zshrc

# Verwendung von virtuellen Umgebungen
python -m venv venv
source venv/bin/activate

# Verwaltung von Abhängigkeiten
pip install pip-tools
pip-compile requirements.in --no-strip-extras
pip-compile requirements.in --upgrade
#pip freeze > requirements.txt
pip install -r requirements.txt
pip install pip-autoremove

# Automatisierte Tests ausführen
pip install pytest
pytest
pytest --disable-warnings

# Testen von tkinter
python3 -c "import tkinter; print('Tkinter funktioniert!')"
# wenn Fehler
brew unlink tcl-tk && brew link tcl-tk
brew reinstall python@3.13 --build-from-source
# oder
deactivate
brew install python-tk@3.13
source venv/bin/activate
# Testen von tkinter
```


## Hauptpakete

1. **matplotlib**: Ein sehr beliebtes Paket für die Erstellung von Grafiken in Python. Es wird oft verwendet, um Daten zu visualisieren.
2. **numpy**: Ein fundamentales Paket für numerische Berechnungen in Python, besonders für Arbeiten mit Arrays und Matrizen.
3. **pandas**: Ein leistungsfähiges Datenanalysetool, das häufig für Datenverarbeitung, Analysen und Transformationen verwendet wird.
4. **scipy**: Eine Erweiterung zu `numpy`, die Funktionen für wissenschaftliche und technische Berechnungen bietet.
5. **seaborn**: Ein Visualisierungs-Toolkit, das auf `matplotlib` basiert und besonders gut für statistische Grafiken geeignet ist.
6. **pillow**: Ein wichtiges Paket für Bildverarbeitung in Python. Es wird häufig verwendet, um Bilder zu öffnen, zu bearbeiten und zu speichern.
7. **PyPDF2**: Ein Paket zur Manipulation von PDF-Dateien, wie z.B. das Extrahieren von Text, das Zusammenführen von PDF-Dokumenten etc.
8. **openpyxl**: Ein Paket, das für die Bearbeitung von Excel-Dateien (.xlsx) verwendet wird. Es ist nützlich, wenn du mit Tabellenkalkulationen arbeiten möchtest.
9. **sympy**: Ein Paket für symbolische Mathematik. Es kann zur Lösung von algebraischen Gleichungen, zur Differentiation und Integration sowie zur symbolischen Manipulation verwendet werden.
10. **Pint**: Ein Paket, das zum Arbeiten mit Maßeinheiten verwendet wird. Es ist hilfreich, wenn man wissenschaftliche Berechnungen durchführt, die verschiedene Maßeinheiten erfordern.
11. **mpmath**: Ein Paket zur Durchführung hochpräziser arithmetischer Berechnungen. Es wird oft bei wissenschaftlichen Berechnungen benötigt.
12. **python-dateutil**: Dieses Paket erweitert die Funktionalität der Python-eigenen `datetime`-Bibliothek und wird häufig für die Arbeit mit Datums- und Zeitformaten verwendet.
13. **pytz** und **tzdata**: Pakete zur Verwaltung von Zeitzonen, die oft in Kombination mit `pandas` und `datetime` verwendet werden.
14. **flexcache** und **flexparser**: Diese Pakete scheinen spezifische Anwendungen oder Tools zu unterstützen, vermutlich zur Caching- und Parsing-Verarbeitung. Sie sind eher projektspezifisch.

```bash
# requirements.in
matplotlib
numpy
pandas
scipy
seaborn
pillow
PyPDF2
openpyxl
sympy
Pint
mpmath
python-dateutil
```

# Die klassischen Phasen der Softwareentwicklung

Die klassischen Phasen der Softwareentwicklung umfassen:

## 1. Projektplanung und Analyse

- Die **Projektziele** und den **Projektumfang** definieren.
- Das **Projektteam** und die **Ressourcen** planen.
- Ein **Risikomanagement** durchführen.

## 2. Anforderungsanalyse (Requirements Engineering)

- Die **funktionalen** und **nicht-funktionalen Anforderungen** ermitteln.
- Die **Kundenanforderungen** dokumentieren.
- Das **Lastenheft** erstellen (Dokument mit den Anforderungen aus Kundensicht).

## 3. Systemdesign

- Die **Softwarearchitektur** entwickeln.
- Die **technischen Spezifikationen** festlegen.
- Das **Pflichtenheft** erstellen (detaillierte Beschreibung der technischen Umsetzung).
- Die **Systemkomponenten** und deren **Interaktionen** definieren.

## 4. Implementierung

- Das **Design** in Programmcode umsetzen.
- Einzelne **Softwaremodule** entwickeln.
- Die **Versionskontrolle** und **Dokumentation** pflegen.

## 5. Qualitätssicherung und Test

- **Unit-Tests** durchführen (Testen einzelner Module).
- **Integrationstests** durchführen (Überprüfung des Zusammenspiels der Module).
- **Systemtests** durchführen (Überprüfung der Gesamtfunktionalität).
- **Lasttests** und **Performanceanalysen** durchführen.
- Ein **Qualitätsmanagement** etablieren.

## 6. Deployment

- Die Software in der **Produktivumgebung** installieren.
- Die **Systeme** konfigurieren.
- Vorhandene **Daten migrieren**.
- Die **Endanwender** schulen.

## 7. Wartung und Support

- **Fehler beheben**.
- **Updates** und **Patches** implementieren.
- Die **Performance optimieren**.
- Anpassungen an **neue Anforderungen** vornehmen.
