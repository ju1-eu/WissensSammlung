# WissensSammlung

Version: 1.1
Zuletzt aktualisiert: 2024-10-04

**Zusammenfassung**

Die WissensSammlung ist ein Open-Source-Projekt, das als zentraler Hub für verschiedene Ressourcen, Dokumentationen und Skripte dient. Es deckt eine breite Palette von Themen ab, darunter Künstliche Intelligenz (KI), LaTeX und MindMaps.

## Inhaltsverzeichnis

- [WissensSammlung](#wissenssammlung)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Überblick](#überblick)
  - [Inhalte](#inhalte)
    - [KI (Künstliche Intelligenz)](#ki-künstliche-intelligenz)
    - [LaTeX](#latex)
    - [MindMaps](#mindmaps)
    - [Skripte](#skripte)
  - [Anleitungen](#anleitungen)
    - [Voraussetzungen](#voraussetzungen)
    - [Installation](#installation)
    - [Dokumentenkonvertierung](#dokumentenkonvertierung)
    - [LaTeX-Kompilierung](#latex-kompilierung)
  - [Projektstruktur](#projektstruktur)
  - [Mitwirken](#mitwirken)
    - [**1. Repository forken**](#1-repository-forken)
    - [**2. Repository klonen**](#2-repository-klonen)
    - [**3. Neuen Branch erstellen**](#3-neuen-branch-erstellen)
    - [**4. Änderungen vornehmen**](#4-änderungen-vornehmen)
    - [**5. Änderungen committen**](#5-änderungen-committen)
    - [**6. Änderungen pushen**](#6-änderungen-pushen)
    - [**7. Pull Request erstellen**](#7-pull-request-erstellen)
    - [**Zusätzliche Tipps:**](#zusätzliche-tipps)
  - [Lizenz](#lizenz)
  - [Kontakt](#kontakt)

---

## Überblick

Im Ordner `docs` finden sich detaillierte Anleitungen und Beispiele:

- **KI (Künstliche Intelligenz)**: Enthält Prompts und Projektideen zur Interaktion mit KI-Modellen, Anleitungen zur Einrichtung von Python-Umgebungen und Git-Projekten.

- **LaTeX**: Bietet Vorlagen, Einstellungen und Beispiele für wissenschaftliche Arbeiten.

- **MindMaps**: Beinhaltet LaTeX-Dateien zur Erstellung von Mindmaps mit TikZ, einschließlich Makefiles zur Automatisierung der Kompilierung.

Zusätzlich enthält das Projekt Skripte im Ordner `scripts`, die Automatisierungsaufgaben wie das Hinzufügen von Front Matter zu Markdown-Dateien und Backups erleichtern. Das Haupt-Makefile ermöglicht die einfache Konvertierung von Markdown zu HTML und die Generierung einer Indexseite.

---

## Inhalte

### KI (Künstliche Intelligenz)

Im Ordner `docs/KI` finden Sie Ressourcen und Dokumentationen rund um das Thema Künstliche Intelligenz:

- **KI_Prompts.md / .html**: Eine Sammlung von Prompts und Beispielen zur Interaktion mit KI-Modellen.
- **Python-Umgebung.md / .html**: Anleitungen zur Einrichtung von Python-Umgebungen für KI-Projekte.
- **git_projekt.md / .html**: Anleitung zur Einrichtung und Verwaltung von Git-Projekten.
- **projekt_ideen_prompts.md / .html**: Ideen und Anregungen für KI-Projekte, inklusive detaillierter Beschreibungen.

### LaTeX

Der Ordner `docs/LaTeX` enthält LaTeX-Vorlagen und Einstellungen:

- **latex_vorlage.tex**: Eine LaTeX-Vorlage für wissenschaftliche Arbeiten.
- **latex_vorlage.pdf**: Die kompilierte PDF-Version der Vorlage.
- **colors_settings.tex**: Vordefinierte Farbeinstellungen für Ihre LaTeX-Dokumente.
- **listing_settings.tex**: Einstellungen für Code-Listings in LaTeX.
- **references.bib**: Eine Beispiel-Bibliographie-Datei für Literaturverweise.

### MindMaps

Im Ordner `docs/MindMaps` finden Sie:

- **mindmap.tex**: Eine LaTeX-Datei zur Erstellung von Mindmaps mit TikZ und der Mindmap-Bibliothek.
- **mindmap.pdf**: Die kompilierte PDF-Version der Mindmap.
- **Makefile**: Ein Makefile zur Automatisierung der Kompilierung der Mindmap.

### Skripte

Der Ordner `scripts` enthält nützliche Shell-Skripte zur Automatisierung von Aufgaben:

- **setup_environment.sh**: Einrichtungsskript für die Python-Umgebung, installiert benötigte Pakete aus `requirements.txt`.
- **backup.sh**: Skript zum Sichern wichtiger Dateien und Verzeichnisse.
- **git_setup.sh**: Automatisiert die Einrichtung des Git-Repositories und die Verbindung zu GitHub.

---

## Anleitungen

### Voraussetzungen

- **Git**: Für die Versionskontrolle und Zusammenarbeit.
- **Pandoc**: Für die Konvertierung von Markdown zu HTML.
- **LaTeX-Distribution**: Wie TeX Live oder MiKTeX für die Kompilierung von LaTeX-Dokumenten.
- **Python**: Falls Sie die Python-Umgebung oder Skripte nutzen möchten.
- **Make**: Für die Nutzung der Makefiles zur Automatisierung.
- **Bash**: Für die Ausführung der Shell-Skripte.

### Installation

1. **Repository erstellen**

   ```bash
   # Repository neu
   echo "# WissensSammlung" >> README.md
   # Symlink zeigt auf die README.md im Hauptverzeichnis
   ln -s ../README.md docs/README_alias.md
   ls -l docs/README_alias.md
   git init
   git add .
   # Git-Versionskontrolle: Conventional Commit erstellen (präzise Nachricht)
   # git commit -m "chore(docs): update README.md"
   git commit -m "chore(docs): add initial README, LICENSE, and project structure"
   git branch -M main
   git remote add origin git@github.com:ju1-eu/WissensSammlung.git
   git push -u origin main

   # Repository push
   git remote add origin git@github.com:ju1-eu/WissensSammlung.git
   git branch -M main
   git push -u origin main
   ```

2. **Python-Umgebung einrichten** (optional)

   Wenn Sie die Python-Skripte verwenden möchten, richten Sie eine virtuelle Umgebung ein:

   ```bash
   brew update && brew upgrade python
   #cat ~/.zshrc | grep alias
   source ~/.zshrc
   echo $PATH
   brew unlink python@3.12
   brew link --overwrite --force python@3.12
   deactivate
   rm -rf meinenv
   python -m venv meinenv
   source meinenv/bin/activate
   pip install --upgrade pip
   #pip freeze > installed_packages.txt
   pip install -r requirements.txt
   pip install torch torchvision torchaudio
   # Test
   python src/test_installation.py
   ```

   Oder verwenden Sie Conda:

   ```bash
   conda deactivate
   #conda remove -n meinenv --all
   conda update conda
   conda update anaconda
   #conda env create -f environment.yml
   conda env update -f environment.yml
   conda activate meinenv
   conda update --all
   #conda config --set channel_priority flexible
   #conda install pytorch torchvision torchaudio -c pytorch --solver=classic
   # Test
   jupyter lab
   jupyter notebook
   # Erweiterungen über den Jupyter Notebook Extension Manager.
   conda install -c conda-forge jupyter_contrib_nbextensions
   jupyter contrib nbextension install --user
   # Jupyter Notebook als Python-Skript exportieren
   jupyter nbconvert --to script src/test_installation.ipynb
   jupyter nbconvert --to html src/test_installation.ipynb
   ```

   ```bash
   # Install Node.js und Tkinter
   #brew install node     
   #brew install tcl-tk

   # Version
   which python3
   python3 --version
   pip --version
   pip list               # Zeigt die Python-Pakete an   
   ```

### Dokumentenkonvertierung

Um die Markdown-Dokumente zu HTML zu konvertieren, nutzen Sie das bereitgestellte Makefile im Hauptverzeichnis:

1. **Konvertierung starten**

   ```bash
   make
   ```

   Dies konvertiert alle Markdown-Dateien im `docs`-Verzeichnis zu HTML und generiert eine `start.html` als Indexseite.

2. **Bereinigung**

   Um generierte HTML-Dateien und temporäre Dateien zu löschen:

   ```bash
   make clean
   ```

### LaTeX-Kompilierung

Für die LaTeX-Dokumente stehen in den jeweiligen Ordnern Makefiles zur Verfügung.

**Beispiel für die Mindmap:**

1. **Wechseln Sie in das MindMaps-Verzeichnis**

   ```bash
   cd docs/MindMaps
   ```

2. **Mindmap kompilieren**

   ```bash
   make
   ```

   Dies erzeugt die `mindmap.pdf` aus der `mindmap.tex`.

3. **Temporäre Dateien löschen**

   ```bash
   make clean
   ```

---

## Projektstruktur

```
WissensSammlung/
├── LICENSE
├── README.md
├── Makefile
├── environment.yml
├── requirements.txt
├── template.html
├── docs/
│   ├── KI/
│   │   ├── KI_Prompts.md
│   │   ├── Python-Umgebung.md
│   │   ├── git_projekt.md
│   │   ├── projekt_ideen_prompts.md
│   ├── LaTeX/
│   │   ├── latex_vorlage.tex
│   │   ├── colors_settings.tex
│   │   ├── listing_settings.tex
│   │   └── references.bib
│   ├── MindMaps/
│   │   ├── mindmap.tex
│   │   └── Makefile
│   ├── images/
│   ├── markdown_styles.css
│   ├── start.md
├── scripts/
│   ├── backup.sh
│   ├── git_setup.sh
│   └── setup_environment.sh
```

---

## Mitwirken

Beiträge zu diesem Projekt sind herzlich willkommen! Wenn Sie Ideen, Verbesserungen oder Fehlerkorrekturen haben, folgen Sie bitte diesen Schritten:

### **1. Repository forken**

Falls Sie keine direkten Schreibrechte zum Repository haben, müssen Sie es zunächst forken, um eine persönliche Kopie zu erstellen.

1. Navigieren Sie zu [WissensSammlung auf GitHub](https://github.com/ju1-eu/WissensSammlung).
2. Klicken Sie auf den Button "Fork" oben rechts, um eine Kopie des Repositorys in Ihrem eigenen GitHub-Account zu erstellen.

### **2. Repository klonen**

Klonen Sie nun das geforkte Repository auf Ihren lokalen Computer.

```bash
git clone git@github.com:ju1-eu/WissensSammlung.git
cd WissensSammlung
```

### **3. Neuen Branch erstellen**

Erstellen Sie einen neuen Branch für Ihre Änderungen, um die Übersichtlichkeit zu bewahren und Konflikte zu vermeiden.

```bash
git checkout -b feature/neues-feature
```

*Ersetzen Sie `neues-feature` durch einen aussagekräftigen Namen für Ihren Branch.*

### **4. Änderungen vornehmen**

Nehmen Sie die gewünschten Änderungen am Projekt vor.

### **5. Änderungen committen**

Committen Sie Ihre Änderungen mit einer aussagekräftigen Commit-Nachricht nach dem [Conventional Commits Standard](https://www.conventionalcommits.org/de/v1.0.0/).

Beispiel:

```bash
git add .
git commit -m "feat(docs): add detailed installation instructions"
```

### **6. Änderungen pushen**

Pushen Sie Ihren Branch zu Ihrem geforkten Repository auf GitHub.

```bash
git push origin feature/neues-feature
```

### **7. Pull Request erstellen**

1. Gehen Sie zu Ihrem geforkten Repository auf GitHub.
2. Sie sollten eine Meldung sehen, dass ein neuer Branch gepusht wurde. Klicken Sie auf "Compare & pull request".
3. Fügen Sie eine Beschreibung hinzu, die Ihre Änderungen erklärt, und klicken Sie auf "Create pull request".

**Anmerkung:** Wenn Sie bereits Schreibrechte zum Original-Repository haben, können Sie Schritt 1 (Fork) überspringen und direkt das Original-Repository klonen.

### **Zusätzliche Tipps:**

- **Upstream-Repository konfigurieren:**

  Wenn Sie das Repository geforkt haben, ist es hilfreich, das Original-Repository als `upstream` hinzuzufügen, um Ihre lokale Kopie auf dem neuesten Stand zu halten.

  ```bash
  git remote add upstream https://github.com/ju1-eu/WissensSammlung.git
  ```

- **Aktualisieren Ihrer lokalen Kopie:**

  Halten Sie Ihre lokale Kopie mit dem Original-Repository synchronisiert.

  ```bash
  git fetch upstream
  git checkout main
  git merge upstream/main
  ```

**Zusammenfassung:**

- **`git fork`** erstellt eine persönliche Kopie des Repositorys auf GitHub und ist besonders nützlich, wenn Sie keine direkten Schreibrechte haben.
- **`git clone`** kopiert ein Repository (Original oder Fork) lokal auf Ihren Computer.
- **Workflow:** Fork → Clone → Branch → Commit → Push → Pull Request.

---

## Lizenz

Dieses Projekt steht unter der [MIT License](LICENSE). Sie sind frei, den Code zu nutzen, zu verändern und zu verbreiten, solange Sie die ursprünglichen Urheber nennen.

---

## Kontakt

Bei Fragen, Anregungen oder Feedback können Sie mich gerne kontaktieren:

- **Name**: Jan Unger
- **E-Mail**: mail@example.com
- **GitHub**: [ju1-eu](https://github.com/ju1-eu)
