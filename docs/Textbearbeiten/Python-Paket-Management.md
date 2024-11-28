---
title: "Python-Paket-Management"
author: "Jan Unger"
date: "2024-11-26"
---

# Python Paket-Management unter macOS

## Virtuelle Umgebung einrichten

```bash
# Terminal öffnen und zum Projektverzeichnis navigieren
# Virtuelle Umgebung deaktivieren
deactivate
# Optional: Virtuelle Umgebung löschen
rm -rf venv
# Virtuelle Umgebung erstellen
python3 -m venv venv
# Virtuelle Umgebung aktivieren
source venv/bin/activate
```

## Pakete installieren

| **Paket**                  | **Funktionalität**                                                    |
| -------------------------- | --------------------------------------------------------------------- |
| `PyPDF2`                   | Verarbeitung von PDF-Dateien (z. B. Extraktion von Inhalten).         |
| `pytube`                   | Herunterladen von Videos von YouTube.                                 |
| `whisper`                  | Sprach-zu-Text-Transkription (z. B. OpenAI Whisper).                  |
| `youtube-transcript-api`   | Abrufen von Transkripten von YouTube-Videos.                          |
| `black`, `isort`, `flake8` | Tools für Code-Formatierung, Import-Sortierung und Linting.           |
| `mypy`                     | Statische Typprüfung für Python-Code.                                 |
| `Pillow`                   | Bildbearbeitung (z. B. Extraktion und Verarbeitung von Bildern).      |
| `PyMuPDF`                  | Verarbeitung von PDFs (Extraktion von Bildern, Texten etc.).          |
| `rich`                     | Formatierte Konsolenausgabe (z. B. Fortschrittsbalken, farbige Logs). |
| `Jinja2`                   | Template-Engine für Python (z. B. HTML-Generierung).                  |
| `PyYAML`                   | Verarbeitung von YAML-Dateien (Konfiguration, Datenaustausch).        |
| `tqdm`                     | Fortschrittsanzeigen für Schleifen und Iterationen.                   |
| `requests`                 | HTTP-Bibliothek für API-Anfragen und Webzugriffe.                     |
| `certifi`                  | Zertifikate für sichere HTTPS-Verbindungen.                           |
| `typing_extensions`        | Erweiterte Typhinweise für Python < 3.10.                             |

Die Pakete bilden ein kohärentes Set:

- Medienverarbeitung (Video, Audio, PDF, Bilder)
- Entwicklungswerkzeuge (Formatierung, Linting, Typing)
- Webinteraktion (Downloads, API-Zugriffe)
- Ausgabeformatierung und Benutzerinteraktion


```bash
# pip aktualisieren
pip install --upgrade pip
# Benötigte Pakete installieren
pip install PyPDF2 pytube whisper youtube-transcript-api PyMuPDF Pillow rich
# HTML & PDF
pip install Jinja2 MarkupSafe PyYAML tqdm
# Tools installieren
pip install black isort flake8 mypy pipdeptree
```

## Pakete in requirements.txt speichern

```bash
# Alle installierten Pakete in requirements.txt speichern
pip freeze > requirements.txt
# Inhalt anzeigen
cat requirements.txt
# Alle Pakete aus der requirements.txt installieren
pip install -r requirements.txt
```

## Pakete aktualisieren

```bash
# Aktuelle Paketliste anzeigen
pip list
# Veraltete Pakete anzeigen
pip list --outdated
# Alle Pakete aktualisieren
pip list --outdated | cut -d ' ' -f1 | tail -n +3 | xargs -n1 pip install -U
# Nach der Aktualisierung requirements.txt erneuern
pip freeze > requirements.txt
```

## Troubleshooting

```bash
# Cache leeren bei Problemen
pip cache purge

# Paket neu installieren
pip uninstall PyPDF2
pip install PyPDF2

# Konfliktprüfung
pip check

# Requirements als Graph visualisieren
pip install pipdeptree
pipdeptree
```

## Code-Qualität prüfen

```bash
pip install black isort flake8 mypy
# black: Gibt aus, welche Dateien neu formatiert wurden.
black create_gallery.py extract_pdf_images.py pdf_extractor.py
# isort: Ändert die Importreihenfolge oder zeigt fehlerhafte Sortierungen an.
isort create_gallery.py extract_pdf_images.py pdf_extractor.py
# flake8: Gibt Warnungen oder Fehler basierend auf PEP8-Konventionen aus
flake8 create_gallery.py extract_pdf_images.py pdf_extractor.py
# mypy: Gibt Typfehler aus, falls die Typannotationen nicht korrekt sind.
mypy create_gallery.py extract_pdf_images.py pdf_extractor.py

# PDF Kapitel Extraktor *.pdf, Seiten von bis?
python pdf_extractor.py
# Extrahiere Bilder aus *.pdf
python extract_pdf_images.py
# Gallerie: gallery/*_gallery.html
python create_gallery.py

# aktuelle Verzeichnis ($(pwd)) wird zum Python-Suchpfad hinzugefügt. Python Module und Pakete, die sich in diesem Verzeichnis befinden, erkennt und importieren kann.
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
# Im Entwicklungsmodus wird das Paket nicht kopiert und installiert, sondern als Referenz zur aktuellen Verzeichnisstruktur verlinkt.
# Änderungen am Quellcode sind sofort in der Umgebung verfügbar, ohne dass man das Paket erneut installieren muss.
# Voraussetzung: setup.py
pip install -e .
```

**Konfiguration:**

```bash
# .flake8
[flake8]
max-line-length = 100
exclude = venv, .git

# pyproject.toml (für black und isort)
[tool.black]
line-length = 100

[tool.isort]
profile = "black"
line_length = 100
```


## pre-commit-Tool

1. **pre-commit installieren**
   Installiere `pre-commit` in der virtuellen Umgebung:

   ```bash
   pip install pre-commit
   ```

2. **Prüfen, ob die Installation erfolgreich war**
   Verifiziere die Installation mit:

   ```bash
   pre-commit --version
   ```

3. **Pre-Commit-Hooks erneut installieren**
   Nachdem das Tool verfügbar ist, führe den Installationsbefehl erneut aus:

   ```bash
   pre-commit clean
   pre-commit install
   pre-commit autoupdate
   ```

4. **Pre-Commit-Hooks testen**
   Überprüfe, ob die Hooks korrekt funktionieren:

   ```bash
   ./update_python_packages.sh
   ./check_pythoncode_quality.sh
   pre-commit run --all-files
   ```

`.pre-commit-config.yaml`

```
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
        args: ['--maxkb=500']
      - id: check-merge-conflict
      - id: mixed-line-ending
        args: ['--fix=lf']

  - repo: https://github.com/psf/black
    rev: 24.1.1
    hooks:
      - id: black
        language_version: python3.12

  - repo: https://github.com/PyCQA/isort
    rev: 5.13.2
    hooks:
      - id: isort

  - repo: https://github.com/PyCQA/flake8
    rev: 7.0.0
    hooks:
      - id: flake8
        additional_dependencies: [flake8-docstrings]
```

## Projektspezifische requirements.txt

```text
# requirements.txt
black==24.10.0
certifi==2024.8.30
charset-normalizer==3.4.0
click==8.1.7
defusedxml==0.7.1
flake8==7.1.1
idna==3.10
isort==5.13.2
markdown-it-py==3.0.0
mccabe==0.7.0
mdurl==0.1.2
mypy==1.13.0
mypy-extensions==1.0.0
packaging==24.2
pathspec==0.12.1
pillow==11.0.0
pipdeptree==2.23.4
platformdirs==4.3.6
pycodestyle==2.12.1
pyflakes==3.2.0
Pygments==2.18.0
PyMuPDF==1.24.14
PyPDF2==3.0.1
pytube==15.0.0
requests==2.32.3
rich==13.9.4
six==1.16.0
typing_extensions==4.12.2
urllib3==2.2.3
whisper==1.1.10
youtube-transcript-api==0.6.3
```

# Projektstruktur

```plaintext
# Projektstruktur anzeigen
tree -L 2 --dirsfirst
# Projektstruktur erfolgt nach Python-Projektstandards
# Ausgabe kommentieren
```

## Tipps und Best Practices

1. **Virtuelle Umgebung**:
   - Immer in einer virtuellen Umgebung arbeiten
   - Für jedes Projekt eine separate Umgebung erstellen
   - Namen der virtuellen Umgebung (venv) in .gitignore aufnehmen

2. **Requirements**:
   - Requirements.txt regelmäßig aktualisieren
   - Version in Kommentaren dokumentieren
   - Backup der funktionierenden requirements.txt anlegen

3. **Sicherheit**:
   - Regelmäßig nach Sicherheitsupdates suchen
   - Pakete nur aus vertrauenswürdigen Quellen installieren
   - Bei Produktivnutzung fixe Versionen verwenden

## Automatisierungsskript I

```bash
#!/bin/bash
# update_python_packages.sh

echo "Starte Paket-Update..."

# Aktiviere virtuelle Umgebung
source venv/bin/activate

# Backup von requirements.txt
cp requirements.txt requirements.backup.txt

# Aktualisiere pip
pip install --upgrade pip

# Aktualisiere alle Pakete
pip list --outdated | cut -d ' ' -f1 | tail -n +3 | xargs -n1 pip install -U

# Erstelle neue requirements.txt
pip freeze > requirements.txt

echo "Update abgeschlossen. Neue Paketversionen:"
cat requirements.txt

# Deaktiviere virtuelle Umgebung
#deactivate
```

Nutzung:
```bash
chmod +x update_python_packages.sh
#source venv/bin/activate
./update_python_packages.sh
```

## Automatisierungsskript I

```bash
#!/bin/bash
# check_pythoncode_quality.sh

# Skript zur Code-Qualitätsprüfung
echo "Starte Code-Qualitätsprüfung..."

# Definiere Verzeichnis für Python-Skripte
SCRIPT_DIR="python-scripte"

# Definiere die zu prüfenden Python-Dateien
PYTHON_FILES="$SCRIPT_DIR/dateien_inhaltsverzeichnis.py \
              $SCRIPT_DIR/dokumentation.py \
              $SCRIPT_DIR/git_hilfsprogramm.py \
              $SCRIPT_DIR/html1_konverter_pandoc.py \
              $SCRIPT_DIR/html2_dateien_verarbeiten.py \
              $SCRIPT_DIR/html3_navigation.py \
              $SCRIPT_DIR/html4_entfernen.py \
              $SCRIPT_DIR/latex_convert1.py \
              $SCRIPT_DIR/latexcode_entfernen2.py \
              $SCRIPT_DIR/suchen_ersetzen.py \
              $SCRIPT_DIR/sync_tex.py \
              image_resizer.py \
              scriptauswahl.py"

# Prüfe, ob das Verzeichnis existiert
if [ ! -d "$SCRIPT_DIR" ]; then
    echo "Fehler: Verzeichnis $SCRIPT_DIR nicht gefunden!"
    exit 1
fi

# Führe die Prüfungen aus
echo "=== Führe Black aus ==="
black $PYTHON_FILES

echo -e "\n=== Führe isort aus ==="
isort $PYTHON_FILES

echo -e "\n=== Führe flake8 aus ==="
flake8 $PYTHON_FILES

echo -e "\n=== Führe mypy aus ==="
mypy $PYTHON_FILES

echo -e "\nCode-Qualitätsprüfung abgeschlossen."
```

Nutzung:
```bash
chmod +x check_pythoncode_quality.sh
#source venv/bin/activate
./check_pythoncode_quality.sh
```
