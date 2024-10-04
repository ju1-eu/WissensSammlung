#!/bin/bash

DOCS_DIR=docs

# Finde alle .md-Dateien und füge YAML Front Matter hinzu, falls sie noch nicht vorhanden sind
find "$DOCS_DIR" -type f -name "*.md" | while read mdfile; do
    # Überprüfen, ob die Datei bereits Front Matter enthält
    if ! grep -q "^---" "$mdfile"; then
        # Extrahiere den Dateinamen ohne Pfad und Erweiterung
        filename=$(basename "$mdfile" .md)

        # Erstelle temporäre Datei mit Front Matter
        {
            echo "---"
            echo "title: \"$filename\""
            echo "author: \"Jan Unger\""
            echo "date: \"$(date +%Y-%m-%d)\""
            echo "---"
            echo ""
            cat "$mdfile"
        } > "${mdfile}.tmp"

        # Ersetze die Originaldatei mit der neuen Datei
        mv "${mdfile}.tmp" "$mdfile"

        echo "Fügte YAML Front Matter zu $mdfile hinzu."
    else
        echo "YAML Front Matter bereits in $mdfile vorhanden."
    fi
done
