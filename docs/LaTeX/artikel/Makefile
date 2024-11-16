# Makefile für mehrere LaTeX-Dokumente (Multi-OS Version mit XeLaTeX)

# Konfiguration
TEX_ENGINE = xelatex
TEX_FLAGS = -interaction=nonstopmode -shell-escape

# Liste aller TEX-Dateien
TEX_FILES = vorlage_checkliste_latex.tex

# Generiere PDF-Ziele aus TEX-Dateien
PDF_FILES = $(TEX_FILES:.tex=.pdf)

# Erkennung des Betriebssystems
ifeq ($(shell uname), Darwin)  # macOS
    VIEWER = open
else ifeq ($(OS),Windows_NT)  # Windows
    VIEWER = start
else  # Linux und andere
    VIEWER = xdg-open
endif

# Hauptziele
.PHONY: all clean view purge help watch

# Alle PDFs erstellen
all: $(PDF_FILES)

# Regel für einzelne PDF-Erstellung
%.pdf: %.tex
	$(TEX_ENGINE) $(TEX_FLAGS) $<
	$(TEX_ENGINE) $(TEX_FLAGS) $<  # Zweiter Durchlauf für Referenzen

# PDF anzeigen (einzeln)
view-%: %.pdf
	$(VIEWER) $<

# Alle PDFs anzeigen
view-all: $(PDF_FILES)
	for pdf in $(PDF_FILES); do \
		$(VIEWER) $$pdf; \
	done

# Überwachungsmodus für einzelne Datei (nur für macOS mit fswatch)
watch-%: %.tex
	@if command -v fswatch > /dev/null; then \
		echo "Überwache $< auf Änderungen..."; \
		fswatch -o $< | xargs -n1 -I{} make $*.pdf; \
	else \
		echo "fswatch ist nicht installiert. Installiere es mit 'brew install fswatch'"; \
	fi

# Aufräumen (temporäre Dateien)
clean:
	rm -f *.aux *.log *.out *.toc *.lof *.lot \
		*.bbl *.blg *.nav *.snm *.synctex.gz \
		*.fls *.fdb_latexmk *.xdv

# Alles löschen (inkl. PDFs)
purge: clean
	rm -f $(PDF_FILES)

# Hilfe anzeigen
help:
	@echo "Verfügbare Make-Befehle:"
	@echo "  make              - Alle PDFs erstellen"
	@echo "  make %.pdf        - Einzelne PDF erstellen (z.B. make 01-KSK-Vorbereitung-Workout.pdf)"
	@echo "  make view-%       - Einzelne PDF anzeigen (z.B. make view-01-KSK-Vorbereitung-Workout)"
	@echo "  make view-all     - Alle PDFs anzeigen"
	@echo "  make watch-%      - Einzelne Datei überwachen (z.B. make watch-01-KSK-Vorbereitung-Workout)"
	@echo "  make clean        - Temporäre Dateien löschen"
	@echo "  make purge        - Alle generierten Dateien löschen"
	@echo "  make help         - Diese Hilfe anzeigen"

# Standard-Ziel
.DEFAULT_GOAL := all