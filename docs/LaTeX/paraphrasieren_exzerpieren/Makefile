# Makefile für LaTeX-Dokumente mit XeLaTeX und Biber

# Konfiguration
TEX_ENGINE = xelatex
BIBER = biber
TEX_FLAGS = -interaction=nonstopmode -shell-escape

# Liste aller TEX-Dateien
TEX_FILES = vorlage_exzerpt_paraphrase.tex \
            motorthermodynamik.tex

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
.PHONY: all clean view purge help watch bibliography

# Alle PDFs erstellen
all: $(PDF_FILES)

# Bibliographie erstellen nur wenn nötig
bibliografie.bib: ;

# Regel für einzelne PDF-Erstellung mit Biber
%.pdf: %.tex bibliografie.bib
	@if [ ! -f $@ ] || [ -n "$$(find $< bibliografie.bib -newer $@ 2>/dev/null)" ]; then \
		echo "Änderungen erkannt, erstelle $@ neu..."; \
		echo "Erstelle $@ (1/4)..."; \
		$(TEX_ENGINE) $(TEX_FLAGS) $< >/dev/null 2>&1; \
		echo "Verarbeite Bibliographie mit Biber..."; \
		$(BIBER) $(basename $<) >/dev/null 2>&1; \
		echo "Erstelle $@ (2/4)..."; \
		$(TEX_ENGINE) $(TEX_FLAGS) $< >/dev/null 2>&1; \
		echo "Erstelle $@ (Finale Version)..."; \
		$(TEX_ENGINE) $(TEX_FLAGS) $< >/dev/null 2>&1; \
		echo "PDF-Erstellung abgeschlossen: $@"; \
	else \
		echo "$@ ist bereits aktuell."; \
	fi

# PDF anzeigen (einzeln)
view-%: %.pdf
	$(VIEWER) $<

# Alle PDFs anzeigen
view-all: $(PDF_FILES)
	for pdf in $(PDF_FILES); do \
		$(VIEWER) $$pdf; \
	done

# Überwachungsmodus mit Biber
watch-%: %.tex
	@if command -v fswatch > /dev/null; then \
		echo "Überwache $< auf Änderungen..."; \
		fswatch -o $< bibliografie.bib | xargs -n1 -I{} sh -c 'make $*.pdf'; \
	else \
		echo "fswatch ist nicht installiert. Installiere es mit 'brew install fswatch'"; \
	fi

# Aufräumen (temporäre Dateien)
clean:
	@echo "Räume temporäre Dateien auf..."
	@rm -f *.aux *.log *.out *.toc *.lof *.lot \
		*.bbl *.blg *.nav *.snm *.synctex.gz \
		*.fls *.fdb_latexmk *.xdv *.xmpi \
		*.bcf *.run.xml *.bbl *.blg
	@echo "Aufräumen abgeschlossen."

# Alles löschen (inkl. PDFs)
purge: clean
	@echo "Lösche PDF-Dateien..."
	@rm -f $(PDF_FILES)
	@echo "Purge abgeschlossen."

# Hilfe anzeigen
help:
	@echo "Verfügbare Make-Befehle:"
	@echo "  make              - Alle PDFs erstellen (nur bei Änderungen)"
	@echo "  make %.pdf        - Einzelne PDF erstellen (nur bei Änderungen)"
	@echo "  make view-%       - Einzelne PDF anzeigen"
	@echo "  make view-all     - Alle PDFs anzeigen"
	@echo "  make watch-%      - Einzelne Datei überwachen"
	@echo "  make clean        - Temporäre Dateien löschen"
	@echo "  make purge        - Alle generierten Dateien löschen"
	@echo "  make help         - Diese Hilfe anzeigen"

# Standard-Ziel
.DEFAULT_GOAL := all