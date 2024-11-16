---
title: "Python-Paket-Management"
author: "Jan Unger"
date: "2024-11-16"
---

# Python Paket-Management unter macOS
## Schritt-für-Schritt Anleitung

### 1. Virtuelle Umgebung einrichten
```bash
# Terminal öffnen und zum Projektverzeichnis navigieren
cd /pfad/zum/projekt

# Virtuelle Umgebung erstellen
python3 -m venv venv

# Virtuelle Umgebung aktivieren
source venv/bin/activate

# Überprüfen ob aktiviert - (venv) sollte am Anfang der Zeile erscheinen
# (venv) jan@imacj $
```

### 2. Pakete installieren
```bash
# pip aktualisieren
pip install --upgrade pip

# Benötigte Pakete installieren
pip install PyPDF2
pip install pytube
pip install whisper
pip install youtube-transcript-api
```

### 3. Aktuelle Pakete in requirements.txt speichern
```bash
# Alle installierten Pakete in requirements.txt speichern
pip freeze > requirements.txt

# Inhalt anzeigen
cat requirements.txt
```

### 4. Pakete aus requirements.txt installieren
```bash
# Alle Pakete aus der requirements.txt installieren
pip install -r requirements.txt
```

### 5. Pakete aktualisieren
```bash
# Veraltete Pakete anzeigen
pip list --outdated

# Einzelnes Paket aktualisieren
pip install --upgrade PyPDF2

# Alle Pakete aktualisieren
pip list --outdated | cut -d ' ' -f1 | tail -n +3 | xargs -n1 pip install -U

# Nach der Aktualisierung requirements.txt erneuern
pip freeze > requirements.txt
```

### 6. Paketliste verwalten
```bash
# Aktuelle Paketliste anzeigen
pip list

# Detaillierte Paketinformationen
pip show PyPDF2

# Requirements in eine neue Datei speichern
pip freeze > requirements_neu.txt

# Unterschiede zwischen alter und neuer requirements.txt anzeigen
diff requirements.txt requirements_neu.txt
```

### 7. Virtuelle Umgebung verlassen/löschen
```bash
# Virtuelle Umgebung deaktivieren
deactivate

# Optional: Virtuelle Umgebung löschen
rm -rf venv
```

### 8. Projektspezifische requirements.txt
Für Ihr aktuelles Projekt mit den angegebenen Paketen:

```text
# requirements.txt
certifi==2024.8.30
charset-normalizer==3.4.0
idna==3.10
PyPDF2==3.0.1
pytube==15.0.0
requests==2.32.3
six==1.16.0
urllib3==2.2.3
whisper==1.1.10
youtube-transcript-api==0.6.2
```

### 9. Tipps und Best Practices

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

4. **Troubleshooting**:
   ```bash
   # Cache leeren bei Problemen
   pip cache purge
   
   # Paket neu installieren
   pip uninstall PyPDF2
   pip install PyPDF2
   
   # Konfliktprüfung
   pip check
   ```

5. **Weitere nützliche Befehle**:
   ```bash
   # Paketabhängigkeiten anzeigen
   pip show -f PyPDF2
   
   # Nur direkte Abhängigkeiten speichern
   pip freeze --all > requirements_all.txt
   
   # Requirements als Graph visualisieren
   pip install pipdeptree
   pipdeptree
   ```

### 10. Automatisierungsskript
Hier ein einfaches Shell-Script zum Aktualisieren der Pakete:

```bash
#!/bin/bash
# update_packages.sh

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
deactivate
```

Nutzung:
```bash
chmod +x update_packages.sh
./update_packages.sh
```
