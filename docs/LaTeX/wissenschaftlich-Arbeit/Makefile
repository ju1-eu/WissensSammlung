# Makefile zum Kompilieren von LaTeX-Dateien

# Liste aller .tex-Dateien, bestimmte Dateien ausschließend
TEX_FILES = $(filter-out colors_settings.tex listing_settings.tex, $(wildcard *.tex))

# Dateien, die Bibliographie-Kompilierung benötigen
BIB_FILES = wissenschaftlicheArbeit-Vorlage.tex wissenschaftlicheArbeit-Feedback.tex latex_vorlage.tex

# Standardziel: Kompiliere alle PDFs
all: $(TEX_FILES:.tex=.pdf)

# Regel zum Konvertieren von .tex zu .pdf mit mehrfachen Kompilierungen
%.pdf: %.tex
	@if echo $(BIB_FILES) | grep -q $<; then \
		xelatex -halt-on-error $<; \
		biber $(basename $<); \
		xelatex -halt-on-error $<; \
		xelatex -halt-on-error $<; \
	else \
		xelatex -halt-on-error $<; \
		xelatex -halt-on-error $<; \
	fi

# Bereinige Hilfsdateien
clean:
	rm -f *.aux *.log *.out *.toc *.bbl *.blg *.fdb_latexmk *.synctex.gz *.fls *.bcf *.run.xml *.lof *.lot

# Bereinige alle generierten Dateien einschließlich PDFs
cleanall: clean
	rm -f *.pdf

# Deklariere Pseudoziele
.PHONY: all clean cleanall

# Hinweis: Zur Verwendung von Parallelisierung führen Sie 'make -j4' aus (passen Sie die Zahl nach Bedarf an)