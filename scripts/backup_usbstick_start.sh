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
INFO="+ Backup"
QUELLE="/Users/jan/daten"
ZIEL="/Volumes/start"
WORK="start"
FILE="backup-usb-start.txt"
TIMESTAMP=$(date +"%d-%h-%y") # 11-Aug-20
COPYRIGHT="+ ju $TIMESTAMP $FILE"
TRENNER="----------------------------------------"

# Backup
# Laufwerk vorhanden?
if [ ! -d "$ZIEL" ]; then
    log_error "$ZIEL Laufwerk mounten."
    exit 1
else 
    # In das Quellverzeichnis wechseln
    if ! cd "$QUELLE"; then
        log_error "Konnte nicht in das Verzeichnis $QUELLE wechseln!"
        exit 1
    fi
    
    log_info "Starte Backup von $WORK nach $ZIEL/$WORK"
    
    # Backup durchführen
    if rsync -av --delete "$WORK/" "$ZIEL/$WORK/"; then
        log_info "Backup erfolgreich abgeschlossen"
    else
        log_error "Backup fehlgeschlagen"
        exit 1
    fi
fi

# Archiv
echo
echo "$TRENNER"
read -p "+ Archiv *.zip erstellen? [j/n] " antwort
if [ -z "$antwort" ]; then
    log_info "Keine Eingabe - Archiv wird nicht erstellt"
elif [ "$antwort" = "j" ]; then
    if ! cd "$QUELLE"; then
        log_error "Konnte nicht in das Verzeichnis $QUELLE wechseln!"
        exit 1
    fi
    
    if [ -f "$WORK.zip" ]; then
        rm -f "$WORK.zip"
        log_info "Altes Archiv gelöscht"
    fi
    
    if zip -r "$WORK.zip" "$WORK"; then
        log_info "Neues Archiv erstellt"
        if [ -f "$ZIEL/$WORK.zip" ]; then
            rm -f "$ZIEL/$WORK.zip"
            log_info "Altes Zielarchiv gelöscht"
        fi
        if mv "$WORK.zip" "$ZIEL"; then
            log_info "Archiv nach $ZIEL verschoben"
        else
            log_error "Konnte Archiv nicht verschieben"
            exit 1
        fi
    else
        log_error "Konnte Archiv nicht erstellen"
        exit 1
    fi
else
    log_info "Archiv wird nicht erstellt"
fi

# Log
{
    echo "$TRENNER"
    echo
    echo "$COPYRIGHT"
    echo
    echo "+ Speichergröße"
    df -lh "$ZIEL"
    echo
    echo "$INFO"
    ls -lh "$ZIEL"
    echo
    echo "$TRENNER"
} > "$ZIEL/$FILE"

log_info "Log-Datei erstellt: $ZIEL/$FILE"
log_info "Backup-Vorgang abgeschlossen"