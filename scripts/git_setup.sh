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

# (Optional) Commit-Signierung einrichten
# git config --global user.signingkey KEYID
# git config --global commit.gpgsign true
