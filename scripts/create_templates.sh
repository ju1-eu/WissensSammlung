#!/bin/bash

# Erstelle Hauptverzeichnis für Vorlagen
TEMPLATE_DIR="wissenschaftliche_vorlagen"
mkdir -p "$TEMPLATE_DIR"

# Funktion zum Erstellen einer Vorlage mit Standardinhalt
create_template() {
    local filename="$1"
    local title="$2"
    local focus="$3"
    
    cat > "$TEMPLATE_DIR/$filename" << EOF
# ${title}

## Überblick
- **Dokumenttyp:** ${title}
- **Schwerpunkt:** ${focus}
- **Version:** 1.0
- **Datum:** $(date +%Y-%m-%d)

## Struktur

### 1. Einleitung
- Kontext
- Zielsetzung
- Methodische Vorgehensweise

### 2. Hauptteil
- Kernelemente
- Analyseschritte
- Wichtige Aspekte

### 3. Abschluss
- Zusammenfassung
- Schlussfolgerungen
- Ausblick

## Hinweise zur Verwendung
- Diese Vorlage dient als Grundgerüst
- Anpassungen nach spezifischen Anforderungen vornehmen
- Wissenschaftliche Standards beachten

## Qualitätskriterien
- Vollständigkeit
- Präzision
- Wissenschaftlichkeit
- Nachvollziehbarkeit

---
*Letzte Aktualisierung: $(date +%Y-%m-%d)*
EOF

    echo "Erstellt: $filename"
}

# Erstelle die Hauptvorlagen
create_template "paraphrase_vorlage.md" "Paraphrasierung" "Sinnerhaltende Umformulierung"
create_template "exzerpt_vorlage.md" "Exzerpt" "Kernaussagen erfassen"
create_template "zusammenfassung_vorlage.md" "Zusammenfassung" "Kompakte Inhaltsdarstellung"
create_template "textanalyse_kritisch_vorlage.md" "Textanalyse" "Argumentative Bewertung"
create_template "wissenschaftliche_analyse_vorlage.md" "Wissenschaftliche Analyse" "Methodisches Vorgehen"
create_template "wissenschaftliche_arbeit_vorlage.md" "Wissenschaftliche Arbeit" "Akademische Strukturierung"
create_template "wissenschaftlicher_stil_vorlage.md" "Wissenschaftlicher Sprachstil" "Fachsprachliche Formulierung"

# Erstelle Index-Datei
cat > "$TEMPLATE_DIR/vorlagen_index.md" << EOF
# Übersicht der wissenschaftlichen Vorlagen

## Hauptvorlagen
1. [Paraphrasierung](paraphrase_vorlage.md)
2. [Exzerpt](exzerpt_vorlage.md)
3. [Zusammenfassung](zusammenfassung_vorlage.md)
4. [Textanalyse](textanalyse_kritisch_vorlage.md)
5. [Wissenschaftliche Analyse](wissenschaftliche_analyse_vorlage.md)
6. [Wissenschaftliche Arbeit](wissenschaftliche_arbeit_vorlage.md)
7. [Wissenschaftlicher Sprachstil](wissenschaftlicher_stil_vorlage.md)

## Ergänzende Materialien
- [Formatierungsrichtlinien](formatierung_richtlinien.md)
- [Checklisten](checklisten_sammlung.md)

*Generiert am: $(date +%Y-%m-%d)*
EOF

# Erstelle Formatierungsrichtlinien
cat > "$TEMPLATE_DIR/formatierung_richtlinien.md" << EOF
# Formatierungsrichtlinien

## Allgemeine Formatierung
- Schriftart: Times New Roman/Arial
- Schriftgröße: 12pt
- Zeilenabstand: 1,5
- Seitenränder: 2,5 cm

## Markdown-Spezifika
- Überschriften mit #
- Listen mit - oder *
- Hervorhebungen mit * oder **
- Zitate mit >

## Zitierweise
- Direkte Zitate: "..."
- Indirekte Zitate: vgl.
- Quellenangaben: (Autor Jahr: Seite)

## Dokumentstruktur
- Klare Hierarchie
- Konsistente Nummerierung
- Logischer Aufbau

*Stand: $(date +%Y-%m-%d)*
EOF

# Erstelle Checklisten
cat > "$TEMPLATE_DIR/checklisten_sammlung.md" << EOF
# Checklisten für wissenschaftliche Arbeiten

## Vor dem Schreiben
- [ ] Thema eingegrenzt
- [ ] Forschungsfrage formuliert
- [ ] Literatur recherchiert
- [ ] Gliederung erstellt

## Während des Schreibens
- [ ] Wissenschaftlicher Stil
- [ ] Quellenangaben
- [ ] Argumentationsstruktur
- [ ] Formatierung

## Finale Prüfung
- [ ] Rechtschreibung/Grammatik
- [ ] Zitierweise
- [ ] Literaturverzeichnis
- [ ] Formale Anforderungen

*Aktualisiert: $(date +%Y-%m-%d)*
EOF

echo "Vorlagenverzeichnis wurde erfolgreich erstellt in: $TEMPLATE_DIR"
echo "Folgende Dateien wurden generiert:"
ls -l "$TEMPLATE_DIR"
