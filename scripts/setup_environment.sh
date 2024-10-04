#!/bin/bash

# Einrichtung der Python-Entwicklungsumgebung
# --------------------------------------------------

# Erstellen eines virtuellen Environments
python3 -m venv venv
echo "Virtuelle Umgebung 'venv' erstellt."

# Aktivieren der virtuellen Umgebung
source venv/bin/activate
echo "Virtuelle Umgebung aktiviert."

# Installieren der Abhängigkeiten
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
    echo "Abhängigkeiten installiert."
else
    echo "Keine 'requirements.txt' gefunden. Bitte Abhängigkeiten manuell installieren."
fi

# Deaktivieren der virtuellen Umgebung
deactivate
echo "Virtuelle Umgebung deaktiviert."
