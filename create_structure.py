#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
create_structure.py

Erstellt die Projektstruktur mit allen notwendigen Verzeichnissen,
aber nur wenn diese noch nicht existieren.
"""

from pathlib import Path


def create_project_structure():
    """Erstellt die Projektstruktur mit allen notwendigen Verzeichnissen."""

    # Definiere die Verzeichnisstruktur
    directories = ["src", "data", "output", "tests"]

    # Erstelle die Verzeichnisse und .gitkeep Dateien
    for directory in directories:
        dir_path = Path(directory)
        gitkeep_path = dir_path / ".gitkeep"

        # Prüfe und erstelle Verzeichnis
        if not dir_path.exists():
            dir_path.mkdir(parents=True)
            print(f"Verzeichnis erstellt: {directory}/")
        else:
            print(f"Verzeichnis existiert bereits: {directory}/")

        # Prüfe und erstelle .gitkeep
        if not gitkeep_path.exists():
            gitkeep_path.touch()
            print(f"Datei erstellt: {directory}/.gitkeep")
        else:
            print(f"Datei existiert bereits: {directory}/.gitkeep")


if __name__ == "__main__":
    print("Erstelle Projektstruktur...")
    create_project_structure()
    print("\nFertig!")
