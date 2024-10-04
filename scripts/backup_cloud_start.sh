#!/bin/bash -e
# ju 2024-10-04 backup.sh
# Zuletzt aktualisiert: 2024-10-04
# Backup erstellen

# Funktionen für Logging
log_info() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') [INFO] $1"
}

log_error() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') [ERROR] $1" >&2
}

# Variablen
QUELLE="/Users/jan/daten"
WORK="start"
CLOUD="$HOME/Library/Mobile Documents/com~apple~CloudDocs/data"

# Prüfen, ob Quellverzeichnis existiert
if [ ! -d "$QUELLE" ]; then
    log_error "Quellverzeichnis $QUELLE existiert nicht!"
    exit 1
fi

# Backup
if [ ! -d "$CLOUD" ]; then # Cloud vorhanden?
    log_error "$CLOUD kein Zugriff!"
    exit 1
else 
    # In das Quellverzeichnis wechseln
    if ! cd "$QUELLE"; then
        log_error "Konnte nicht in das Verzeichnis $QUELLE wechseln!"
        exit 1
    fi
    
    log_info "Starte Backup von $WORK nach $CLOUD/$WORK"
    
    # Backup durchführen
    if rsync -av --delete "$WORK/" "$CLOUD/$WORK/"; then
        log_info "Backup erfolgreich abgeschlossen"
    else
        log_error "Backup fehlgeschlagen"
        exit 1
    fi
fi

# Log
log_info "Backup-Vorgang abgeschlossen"