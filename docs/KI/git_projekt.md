---
title: "git_projekt"
author: "Jan Unger"
date: "2024-09-28"
---

# Git

bearbeitet am 11. Oktober 2024

- [Git](#git)
  - [Git-Konfigurationsbefehle verstehen](#git-konfigurationsbefehle-verstehen)
  - [Umsetzung der Git-Konfiguration](#umsetzung-der-git-konfiguration)
  - [SSH-Schlüssel für GitHub einrichten](#ssh-schlüssel-für-github-einrichten)
    - [Überprüfe, ob bereits ein SSH-Schlüssel existiert](#überprüfe-ob-bereits-ein-ssh-schlüssel-existiert)
    - [Generiere einen neuen SSH-Schlüssel](#generiere-einen-neuen-ssh-schlüssel)
    - [Füge den SSH-Schlüssel zum SSH-Agent hinzu](#füge-den-ssh-schlüssel-zum-ssh-agent-hinzu)
    - [Füge den öffentlichen SSH-Schlüssel zu GitHub hinzu](#füge-den-öffentlichen-ssh-schlüssel-zu-github-hinzu)
  - [GitHub-Repository erstellen und verbinden](#github-repository-erstellen-und-verbinden)
    - [GitHub-Repository erstellen](#github-repository-erstellen)
    - [Lokales Git-Repository initialisieren und verbinden](#lokales-git-repository-initialisieren-und-verbinden)
    - [Ausschließen von .html-Dateien mit Ausnahme von template.html in Git](#ausschließen-von-html-dateien-mit-ausnahme-von-templatehtml-in-git)
  - [Jupyter Notebook als Python-Skript exportieren](#jupyter-notebook-als-python-skript-exportieren)
    - [Automatisches Exportieren bei jedem Commit](#automatisches-exportieren-bei-jedem-commit)
  - [Weitere nützliche Git-Befehle und Best Practices](#weitere-nützliche-git-befehle-und-best-practices)
    - [Git-Aliase nutzen](#git-aliase-nutzen)
    - [Branching und Pull Requests](#branching-und-pull-requests)
    - [Globale .gitignore erweitern](#globale-gitignore-erweitern)
  - [Bereinigung des Git-Repositories, GitHub-Synchronisation und Setzen der Berechtigungen](#bereinigung-des-git-repositories-github-synchronisation-und-setzen-der-berechtigungen)
  - [Repository zu klonen und Änderungen vorzunehmen - zwischen zwei Rechnern (iMac und MacBook)](#repository-zu-klonen-und-änderungen-vorzunehmen---zwischen-zwei-rechnern-imac-und-macbook)

## Git-Konfigurationsbefehle verstehen

- **Benutzeridentifikation**: Setzt deinen Namen und deine E-Mail-Adresse, die bei jedem Commit verwendet werden.
- **Standard-Branch**: Setzt den Standard-Branch-Namen auf `main` statt `master`.
- **Globale `.gitignore`**: Legt eine globale `.gitignore`-Datei fest, die bestimmte Dateien und Verzeichnisse in allen Repositories ignoriert.
- **Git-Aliase**: Erstellt Kurzbefehle für häufig verwendete Git-Befehle.
- **Farben aktivieren**: Verbessert die Lesbarkeit der Git-Ausgabe durch Farbgebung.
- **Standard-Editor**: Setzt den Standard-Editor für Git-Commits (z.B. Visual Studio Code).
- **Pull-Strategie**: Ändert die Pull-Strategie auf `rebase`, um eine sauberere Commit-Historie zu ermöglichen.
- **Automatisches Entfernen von gemergten Branches**: Entfernt lokale Branches, die bereits gemergt wurden.
- **Whitespace-Änderungen anzeigen**: Hebt Änderungen in Leerzeichen hervor.

## Umsetzung der Git-Konfiguration

1. **Erstelle eine neue Datei namens `git_setup.sh`:**

   ```bash
   vim git_setup.sh
   ```

2. **Füge die Git-Konfigurationsbefehle in die Datei ein:**

   ```bash
   #!/bin/bash

   # Benutzeridentifikation
   git config --global user.name "Jan Unger"
   git config --global user.email "esel573@gmail.com"

   # Standard-Branch auf 'main' setzen
   git config --global init.defaultBranch main

   # Globale .gitignore festlegen
   touch ~/.gitignore_global
   echo -e "# macOS\n.DS_Store\n\n# Python\n__pycache__/\n*.py[cod]\n*.pyo\n*.pyd\n*.env\n.env\n*.egg\n*.egg-info/\ndist/\nbuild/" > ~/.gitignore_global
   git config --global core.excludesfile ~/.gitignore_global

   # Git-Aliase einrichten
   git config --global alias.st status
   git config --global alias.co checkout
   git config --global alias.br branch
   git config --global alias.ci commit
   git config --global alias.lg "log --oneline --graph --decorate --all"

   # Farben aktivieren
   git config --global color.ui auto

   # Standard-Editor festlegen (Beispiel: VS Code: code --wait)
   git config --global core.editor "vim"

   # Pull-Strategie auf Rebase setzen
   git config --global pull.rebase true

   # Automatisches Entfernen von gemergten Branches
   git config --global fetch.prune true

   # Whitespace-Änderungen anzeigen
   git config --global core.whitespace trailing-space,space-before-tab
   ```

3. **Speichere die Datei und mache das Skript ausführbar:**

   - **Mache das Skript ausführbar:**

     ```bash
     chmod +x git_setup.sh
     ./git_setup.sh
     # Überprüfe die Git-Konfiguration
     git config --list
     ```

## SSH-Schlüssel für GitHub einrichten

Um die Sicherheit und Benutzerfreundlichkeit zu erhöhen, ist es empfehlenswert, SSH-Schlüssel für die Authentifizierung mit GitHub zu verwenden.

### Überprüfe, ob bereits ein SSH-Schlüssel existiert

```bash
ls -al ~/.ssh
```

Suche nach Dateien wie `id_rsa.pub` oder `id_ed25519.pub`. Wenn keine SSH-Schlüssel vorhanden sind, erstelle einen neuen.

### Generiere einen neuen SSH-Schlüssel

1. **Erstelle einen neuen SSH-Schlüssel mit deiner GitHub-E-Mail-Adresse:**

   ```bash
   ssh-keygen -t ed25519 -C "esel573@gmail.com"
   ```

   **Hinweis:** Wenn dein System keine Unterstützung für Ed25519 bietet, verwende RSA:

   ```bash
   ssh-keygen -t rsa -b 4096 -C "esel573@gmail.com"
   ```

2. **Folge den Anweisungen im Terminal:**
   - Drücke `Enter`, um den Schlüssel im Standardverzeichnis zu speichern (`~/.ssh/id_ed25519`).
   - Optional: Lege ein sicheres Passwort fest oder drücke einfach `Enter`, um kein Passwort zu verwenden.

### Füge den SSH-Schlüssel zum SSH-Agent hinzu

1. **Starte den SSH-Agenten im Hintergrund:**

   ```bash
   eval "$(ssh-agent -s)"
   ```

2. **Füge deinen SSH-Schlüssel zum Agenten hinzu:**

   ```bash
   ssh-add ~/.ssh/id_ed25519
   ```

   **Hinweis:** Passe den Pfad an, falls du RSA verwendet hast (`~/.ssh/id_rsa`).

### Füge den öffentlichen SSH-Schlüssel zu GitHub hinzu

1. **Kopiere den Inhalt deines öffentlichen SSH-Schlüssels in die Zwischenablage:**

   ```bash
   pbcopy < ~/.ssh/id_ed25519.pub
   ```

   **Hinweis:** Falls du RSA verwendet hast, ersetze `id_ed25519.pub` durch `id_rsa.pub`.

2. **Gehe zu GitHub:**
   - Melde dich bei [GitHub](https://github.com/) an.
   - Navigiere zu **Settings** > **SSH and GPG keys**.
   - Klicke auf **"New SSH key"**.
   - Füge den kopierten Schlüssel in das Feld **"Key"** ein und gib ihm einen aussagekräftigen Titel.
   - Klicke auf **"Add SSH key"**.

3. **Überprüfe die SSH-Verbindung zu GitHub:**

   ```bash
   ssh -T git@github.com
   ```

   **Erwartete Ausgabe:**

   ```
   Hi JanUnger! You've successfully authenticated, but GitHub does not provide shell access.
   ```

## GitHub-Repository erstellen und verbinden

Falls du dies noch nicht getan hast, erstelle ein Repository auf GitHub und verbinde es mit deinem lokalen Projekt.

### GitHub-Repository erstellen

1. **Gehe zu [GitHub](https://github.com/) und melde dich an.**
2. **Klicke auf das Plus-Symbol (`+`) oben rechts und wähle "New repository".**
3. **Fülle die erforderlichen Informationen aus:**
   - **Repository-Name:** `mechanik` (oder ein anderer Name deiner Wahl).
   - **Beschreibung:** Optional, z.B. "Simulation der Rollreibung".
   - **Sichtbarkeit:** Wähle zwischen "Public" oder "Private".
   - **README hinzufügen:** Aktiviere **"Initialize this repository with a README"**.
4. **Klicke auf "Create repository".**

### Lokales Git-Repository initialisieren und verbinden

```bash
echo "# Spieleentwicklung mit Python" >> README.md
git init
git add README.md
git commit -m "Initialer Commit"

# GitHub-Repository verbinden und pushen
git branch -M main
git remote add origin git@github.com:ju1-eu/spieleentwicklung-mit-python.git
git push -u origin main

# Tagging der Version 1.0
git tag -a v1.0 -m "Version 1.0: Initiale Veröffentlichung"
git push origin v1.0
```

### Ausschließen von .html-Dateien mit Ausnahme von template.html in Git

```bash
# 1. .gitignore aktualisieren
echo "*.html" >> .gitignore
echo "!template.html" >> .gitignore

# 2. Entfernen Sie die .html-Dateien aus dem Git-Tracking außer template.html
git rm --cached *.html
git reset template.html

# 3. Commit der Änderungen
git add .gitignore
git commit -m "Alle .html-Dateien ignorieren außer template.html"

# 4. Füge template.html hinzu
git add template.html
git commit -m "Füge template.html hinzu und verfolge sie trotz .gitignore"

# 5. Push der Änderungen zum Remote-Repository
git push origin main

# 6. Überprüfen Sie den Status
git status
```

## Jupyter Notebook als Python-Skript exportieren

Um dein Jupyter Notebook (`mein_notebook.ipynb`) als Python-Skript zu exportieren, verwende den folgenden Befehl:

```bash
jupyter nbconvert --to script mein_notebook.ipynb
```

Dies erstellt eine Datei namens `mein_notebook.py` im selben Verzeichnis.

### Automatisches Exportieren bei jedem Commit

Um sicherzustellen, dass dein Python-Skript immer auf dem neuesten Stand ist, kannst du einen Git Hook einrichten, der das Notebook automatisch bei jedem Commit exportiert.

1. **Navigiere zum Git-Hooks-Verzeichnis:**

   ```bash
   cd .git/hooks
   ```

2. **Erstelle einen `pre-commit` Hook:**

   ```bash
   vim pre-commit
   ```

3. **Füge folgendes Skript hinzu:**

   ```bash
   #!/bin/sh
   jupyter nbconvert --to script ../mein_notebook.ipynb
   git add ../mein_notebook.py
   ```

   **Hinweis:** Passe den Pfad zu deinem Notebook entsprechend an.

4. **Speichere die Datei und mache den Hook ausführbar:**

   - **Speichern und Beenden in `vim`:** Drücke `Ctrl + O`, dann `Enter`, und dann `Ctrl + X`.
   - **Mache den Hook ausführbar:**

     ```bash
     chmod +x pre-commit
     ```

Jetzt wird bei jedem Commit dein Notebook automatisch als Python-Skript exportiert und hinzugefügt.

## Weitere nützliche Git-Befehle und Best Practices

### Git-Aliase nutzen

- **Status anzeigen:**

  ```bash
  git st
  ```

- **Checkout zu einem Branch:**

  ```bash
  git co branch-name
  ```

- **Branch erstellen und wechseln:**

  ```bash
  git co -b neuer-branch
  ```

- **Commit erstellen:**

  ```bash
  git ci -m "Nachricht"
  ```

- **Commit-Historie anzeigen:**

  ```bash
  git lg
  ```

### Branching und Pull Requests

Für eine saubere Entwicklung ist es empfehlenswert, neue Features in separaten Branches zu entwickeln und diese über Pull Requests zu mergen.

1. **Neuen Branch erstellen:**

   ```bash
   git checkout -b feature/neues-feature
   ```

2. **Änderungen vornehmen und committen:**

   ```bash
   git add .
   git commit -m "Beschreibung der Änderungen"
   ```

3. **Branch zu GitHub pushen:**

   ```bash
   git push -u origin feature/neues-feature
   ```

4. **Pull Request auf GitHub erstellen:**
   - Gehe zu deinem Repository auf GitHub.
   - Du siehst eine Meldung, dass ein neuer Branch gepusht wurde. Klicke auf **"Compare & pull request"**.
   - Füge eine Beschreibung hinzu und klicke auf **"Create pull request"**.

### Globale .gitignore erweitern

Falls du zusätzliche Dateien oder Verzeichnisse global ignorieren möchtest, bearbeite die globale `.gitignore`-Datei:

```bash
vim ~/.gitignore_global
# macOS
.DS_Store
*~

# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
*.env
.env
*.egg
*.egg-info/
dist/
build/

# Virtuelle Umgebungen
meinenv/
venv/
.env/

# Jupyter Notebook Checkpoints
.ipynb_checkpoints/
.virtual_documents/

# LaTeX
*.aux
*.log
*.out
*.toc

# HTML
*.html
# Ausnahme: Verfolge die Datei template.html
!template.html

# Editor spezifisch
.vscode/
.idea/
```

## Bereinigung des Git-Repositories, GitHub-Synchronisation und Setzen der Berechtigungen

1. Lokales Repository bereinigen:
   * Nicht-versionierte Dateien entfernen:
     ```
     git clean -fd
     ```
   * .DS_Store Dateien entfernen:
     ```
     find . -name ".DS_Store" -delete
     ```
   * Temporäre Python-Dateien löschen:
     ```
     find . -name "*.pyc" -delete
     find . -name "__pycache__" -type d -exec rm -r {} +
     ```

2. Berechtigungen unter macOS setzen:
   * Ausführbare Dateien:
     ```
     find . -name "*.py" -exec chmod 644 {} +
     chmod +x main.py run_tests.py
     ```
   * Verzeichnisse:
     ```
     find . -type d -exec chmod 755 {} +
     ```

3. .gitignore aktualisieren:
   * Öffnen und bearbeiten:
     ```
     nano .gitignore
     ```
   * Wichtige Einträge:
     ```
     .venv/
     __pycache__/
     *.pyc
     *.html
     !template.html
     .DS_Store
     ```

4. Git-Verlauf bereinigen:
   * Unerwünschte Dateien aus dem Verlauf entfernen:
     ```
     git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch **/*.pyc **/__pycache__/* **/.DS_Store' --prune-empty --tag-name-filter cat -- --all
     ```

5. Änderungen auf GitHub übertragen:
   * Force-Push der bereinigten Historie:
     ```
     git push origin --force --all
     ```

6. Lokales Repository aufräumen:
   ```
   git for-each-ref --format='delete %(refname)' refs/original | git update-ref --stdin
   git reflog expire --expire=now --all
   git gc --prune=now
   ```

7. Überprüfen auf verbleibende .html-Dateien:
   ```
   git ls-files | grep '\.html$'
   ```

* Wenn dieser Befehl keine Ausgabe liefert, sind keine .html-Dateien mehr im Repository.

Diese Schritte stellen sicher, dass das Repository von unerwünschten Dateien bereinigt, die Berechtigungen korrekt gesetzt und alle Änderungen mit GitHub synchronisiert sind.

## Repository zu klonen und Änderungen vorzunehmen - zwischen zwei Rechnern (iMac und MacBook)

1. Klonen des Repositories auf dem MacBook:
   ```
   git clone https://github.com/ju1-eu/WissensSammlung.git
   cd WissensSammlung
   ```

2. Vor dem Arbeiten, immer den aktuellen Stand holen:
   ```
   git pull origin main
   ```

3. Änderungen vornehmen und committen:
   ```
   # Änderungen an Dateien vornehmen
   git add .
   git commit -m "Beschreibung der Änderungen"
   ```

4. Änderungen auf GitHub pushen:
   ```
   git push origin main
   ```

5. Wenn Sie zum iMac wechseln:
   ```
   cd WissensSammlung
   git pull origin main
   # Arbeiten Sie nun an Ihren Dateien
   ```

6. Nach dem Arbeiten auf dem iMac:
   ```
   git add .
   git commit -m "Beschreibung der Änderungen auf dem iMac"
   git push origin main
   ```

7. Zurück auf dem MacBook:
   ```
   git pull origin main
   # Fahren Sie mit der Arbeit fort
   ```

Wichtige Hinweise:

- Führen Sie immer ein `git pull` aus, bevor Sie mit der Arbeit beginnen, um sicherzustellen, dass Sie die neueste Version haben.
- Committen und pushen Sie regelmäßig, um Ihre Arbeit zu sichern und zwischen den Geräten zu synchronisieren.
- Vermeiden Sie, gleichzeitig auf beiden Geräten an denselben Dateien zu arbeiten, um Konflikte zu minimieren.
- Falls doch Konflikte auftreten, lösen Sie diese manuell und committen Sie die Lösung.

Mit dieser Vorgehensweise können Sie effektiv an Ihrem Projekt arbeiten und die Änderungen zwischen Ihren beiden Rechnern synchron halten.