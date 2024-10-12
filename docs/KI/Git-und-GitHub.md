---
title: "Git und GitHub"
author: "Jan Unger"
date: "2024-10-12"
---

# Git und GitHub

bearbeitet am 12. Oktober 2024

## Inhaltsverzeichnis

- [Git und GitHub](#git-und-github)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Einführung](#einführung)
  - [Git-Konfiguration und Fortgeschrittene Konzepte](#git-konfiguration-und-fortgeschrittene-konzepte)
    - [Git-Konfiguration verstehen und anpassen](#git-konfiguration-verstehen-und-anpassen)
    - [Erklärung der fortgeschrittenen Konfigurationen](#erklärung-der-fortgeschrittenen-konfigurationen)
  - [SSH-Schlüssel für GitHub](#ssh-schlüssel-für-github)
  - [GitHub-Repository-Management](#github-repository-management)
    - [Repository-Erstellung und -Verbindung](#repository-erstellung-und--verbindung)
    - [Branching-Strategien](#branching-strategien)
  - [Workflow-Optimierung](#workflow-optimierung)
    - [Git Hooks für automatisierte Prozesse](#git-hooks-für-automatisierte-prozesse)
    - [Kontinuierliche Integration mit GitHub Actions](#kontinuierliche-integration-mit-github-actions)
  - [Fortgeschrittene Git-Techniken](#fortgeschrittene-git-techniken)
    - [Interaktives Rebasing](#interaktives-rebasing)
    - [Git Reflog für Datenrettung](#git-reflog-für-datenrettung)
    - [Submodule für Projektabhängigkeiten](#submodule-für-projektabhängigkeiten)
  - [Fehlerbehebung und Best Practices](#fehlerbehebung-und-best-practices)
    - [Typische Fehlerszenarien und Lösungen](#typische-fehlerszenarien-und-lösungen)
    - [Best Practices für Teamarbeit](#best-practices-für-teamarbeit)
  - [Zusammenfassung und weiterführende Ressourcen](#zusammenfassung-und-weiterführende-ressourcen)
  - [Globale .gitignore erweitern](#globale-gitignore-erweitern)
  - [Bereinigung des Git-Repositories, GitHub-Synchronisation und Setzen der Berechtigungen](#bereinigung-des-git-repositories-github-synchronisation-und-setzen-der-berechtigungen)
  - [Repository zu klonen und Änderungen vorzunehmen - zwischen zwei Rechnern (iMac und MacBook)](#repository-zu-klonen-und-änderungen-vorzunehmen---zwischen-zwei-rechnern-imac-und-macbook)
  - [GitHub - Passwort-Authentifizierung SSH verwenden](#github---passwort-authentifizierung-ssh-verwenden)
  - [Git-Version erstellen](#git-version-erstellen)

## Einführung

Dieses Dokument richtet sich an Entwickler, die ihre Git- und GitHub-Kenntnisse vertiefen möchten. Es behandelt komplexe Konzepte, Best Practices und Workflow-Optimierungen.

## Git-Konfiguration und Fortgeschrittene Konzepte

### Git-Konfiguration verstehen und anpassen

```bash
#!/bin/bash

# Benutzeridentifikation
git config --global user.name "Jan Unger"
git config --global user.email "esel573@gmail.com"

# Standard-Branch auf 'main' setzen
git config --global init.defaultBranch main

# Fortgeschrittene Konfigurationen
git config --global core.autocrlf input  # Zeilenende-Behandlung
git config --global core.editor "vim"    # Bevorzugter Editor
git config --global pull.rebase true     # Rebase statt Merge bei Pull
git config --global fetch.prune true     # Automatisches Entfernen alter Branches

# Git-Aliase für Effizienz
git config --global alias.lg "log --oneline --graph --decorate --all"
git config --global alias.undo "reset HEAD~1 --mixed"
git config --global alias.amend "commit --amend --no-edit"

# Erweiterte Diff-Einstellungen
git config --global diff.algorithm histogram
git config --global diff.compactionHeuristic true
```

### Erklärung der fortgeschrittenen Konfigurationen

- `core.autocrlf`: Verhindert Probleme mit unterschiedlichen Zeilenenden zwischen Betriebssystemen.
- `pull.rebase`: Verwendet Rebase statt Merge beim Pullen, um eine lineare Historie zu erhalten.
- `fetch.prune`: Entfernt automatisch Referenzen zu nicht mehr existierenden Remote-Branches.
- `diff.algorithm`: Der Histogram-Algorithmus bietet oft bessere Diff-Ergebnisse als der Standard.
- `diff.compactionHeuristic`: Verbessert die Lesbarkeit von Diffs durch intelligentere Gruppierung von Änderungen.

## SSH-Schlüssel für GitHub

Die Verwendung von SSH-Schlüsseln erhöht die Sicherheit und Bequemlichkeit bei der Interaktion mit GitHub.

```bash
# Generieren eines neuen ED25519 SSH-Schlüssels
ssh-keygen -t ed25519 -C "esel573@gmail.com"

# SSH-Agenten starten und Schlüssel hinzufügen
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Öffentlichen Schlüssel anzeigen (zur Einfügung in GitHub)
cat ~/.ssh/id_ed25519.pub
```

**Hinweis:** ED25519 wird aufgrund seiner Sicherheit und Effizienz gegenüber RSA empfohlen.

## GitHub-Repository-Management

### Repository-Erstellung und -Verbindung

```bash
# Lokales Repository initialisieren
git init

# Remote-Repository hinzufügen
git remote add origin git@github.com:username/repo.git

# Erste Commit und Push
git add .
git commit -m "Initial commit"
git push -u origin main
```

### Branching-Strategien

Implementieren Sie eine Branching-Strategie wie Git Flow für größere Projekte:

```bash
# Feature-Branch erstellen
git checkout -b feature/neue-funktion

# Nach Fertigstellung in develop mergen
git checkout develop
git merge --no-ff feature/neue-funktion

# Release-Branch erstellen
git checkout -b release/v1.0

# Nach Tests in main und develop mergen
git checkout main
git merge --no-ff release/v1.0
git tag -a v1.0 -m "Version 1.0 Release"
```

## Workflow-Optimierung

### Git Hooks für automatisierte Prozesse

Beispiel eines pre-commit Hooks zur automatischen Code-Formatierung:

```bash
#!/bin/sh
# .git/hooks/pre-commit

files=$(git diff --cached --name-only --diff-filter=ACM | grep ".py$")
if [ -n "$files" ]; then
    python -m black $files
    git add $files
fi
```

### Kontinuierliche Integration mit GitHub Actions

Erstellen Sie eine `.github/workflows/ci.yml` Datei:

```yaml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: python -m unittest discover tests
```

## Fortgeschrittene Git-Techniken

### Interaktives Rebasing

Nutzen Sie interaktives Rebasing, um die Commit-Historie zu bereinigen:

```bash
git rebase -i HEAD~5
```

### Git Reflog für Datenrettung

```bash
# Verloren geglaubte Commits finden
git reflog

# Zu einem bestimmten Commit zurückkehren
git reset --hard HEAD@{2}
```

### Submodule für Projektabhängigkeiten

```bash
# Submodul hinzufügen
git submodule add https://github.com/example/library.git

# Submodule aktualisieren
git submodule update --init --recursive
```

## Fehlerbehebung und Best Practices

### Typische Fehlerszenarien und Lösungen

1. **Merge-Konflikte**
   ```bash
   git merge --abort  # Abbrechen des Merge
   # Manuelles Lösen der Konflikte
   git add .
   git merge --continue
   ```

2. **Versehentlicher Commit in falschen Branch**
   ```bash
   git cherry-pick <commit-hash>  # Commit in richtigen Branch übernehmen
   git reset --hard HEAD~1        # Commit aus falschem Branch entfernen
   ```

3. **Große Binärdateien im Repository**
   ```bash
   git filter-branch --tree-filter 'rm -f pfad/zur/großen/datei' HEAD
   ```

### Best Practices für Teamarbeit

- Verwenden Sie aussagekräftige Commit-Nachrichten.
- Führen Sie regelmäßige Code-Reviews durch.
- Halten Sie Branches kurzlebig und fokussiert.
- Nutzen Sie Pull Requests für Diskussionen und Qualitätssicherung.

## Zusammenfassung und weiterführende Ressourcen

Diese Anleitung bietet eine umfassende Übersicht über Git und GitHub. Für weitere Vertiefung empfehlen wir:

- [Pro Git Book](https://git-scm.com/book/en/v2)
- [GitHub Skills](https://skills.github.com/)
- [Git Internals](https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain)

## Globale .gitignore erweitern

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
*.aux *.log *.out *.toc *.bbl *.blg *.fdb_latexmk *.synctex.gz *.fls *.bcf *.run.xml

# HTML
*.html
# Ausnahme: Verfolge die Datei template.html
!template.html

# Editor spezifisch
!.vscode/
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

## GitHub - Passwort-Authentifizierung SSH verwenden

1. Wechseln Sie zu SSH:
   - Generieren Sie einen SSH-Schlüssel:
     ```
     ssh-keygen -t ed25519 -C "your_email@example.com"
     ```

2. Kopieren Sie den öffentlichen Schlüssel:
   ```
   cat ~/.ssh/id_ed25519.pub | pbcopy
   ```
   Dies kopiert den Inhalt Ihres öffentlichen Schlüssels in die Zwischenablage.

3. Fügen Sie den Schlüssel zu Ihrem GitHub-Konto hinzu:
   - Gehen Sie zu GitHub.com und melden Sie sich an.
   - Klicken Sie auf Ihr Profilbild oben rechts und wählen Sie "Settings".
   - Klicken Sie im linken Seitenmenü auf "SSH and GPG keys".
   - Klicken Sie auf "New SSH key" oder "Add SSH key".
   - Geben Sie einen aussagekräftigen Titel für den Schlüssel ein (z.B. "MacBook").
   - Fügen Sie den kopierten öffentlichen Schlüssel in das Feld "Key" ein.
   - Klicken Sie auf "Add SSH key".

4. Ändern Sie die Remote-URL Ihres Repositories zu SSH:
   ```
   git remote set-url origin git@github.com:ju1-eu/WissensSammlung.git
   ```

5. Überprüfen Sie die Änderung:
   ```
   git remote -v
   ```
   Sie sollten nun die SSH-URL für Ihr Repository sehen.

6. Testen Sie die SSH-Verbindung zu GitHub:
   ```
   ssh -T git@github.com
   ```
   Sie sollten eine Begrüßungsnachricht von GitHub erhalten.

7. Versuchen Sie erneut zu pushen:
   ```
   git push origin main
   ```

Jetzt sollten Sie in der Lage sein, Änderungen zu pushen und zu pullen, ohne jedes Mal Ihre Anmeldedaten eingeben zu müssen. Der SSH-Schlüssel authentifiziert Sie automatisch bei GitHub.

Wenn Sie auf Ihrem iMac arbeiten möchten, müssen Sie dort einen ähnlichen Prozess durchführen: einen neuen SSH-Schlüssel generieren, ihn zu GitHub hinzufügen und die Remote-URL des Repositories aktualisieren.

## Git-Version erstellen

1. Zuerst committen Sie die Änderungen an der .gitignore-Datei:

   ```
   git add .gitignore
   git commit -m "Update .gitignore"
   ```

2. Stellen Sie sicher, dass alle gewünschten Änderungen committed sind:

   ```
   git status
   ```

3. Erstellen Sie einen Tag für Version 1.0:

   ```
   git tag -a v1.0 -m "Version 1.0"
   ```

4. Pushen Sie den Tag zu GitHub:

   ```
   git push origin v1.0
   ```

5. Wenn Sie möchten, können Sie auch einen Release auf GitHub erstellen:
   - Gehen Sie zur GitHub-Repository-Seite
   - Klicken Sie auf "Releases"
   - Klicken Sie auf "Draft a new release"
   - Wählen Sie den Tag v1.0
   - Geben Sie einen Titel ein, z.B. "Version 1.0"
   - Fügen Sie Release-Notizen hinzu, die die wichtigsten Änderungen und Features beschreiben
   - Klicken Sie auf "Publish release"

6. Aktualisieren Sie die README.md-Datei, um die neue Version zu reflektieren:

   ```
   vim README.md
   # Fügen Sie Informationen über Version 1.0 hinzu
   git add README.md
   git commit -m "Update README.md for version 1.0"
   git push origin main
   ```

7. Wenn Sie einen Entwicklungszweig für zukünftige Änderungen erstellen möchten:

   ```
   git checkout -b develop
   git push -u origin develop
   ```

Diese Schritte erstellen eine offizielle Version 1.0 Ihres Projekts, markieren sie mit einem Git-Tag und optional mit einem GitHub-Release, und bereiten das Repository für zukünftige Entwicklungen vor. Vergessen Sie nicht, die README.md und andere relevante Dokumentation zu aktualisieren, um die neue Version und eventuelle wichtige Änderungen zu reflektieren.