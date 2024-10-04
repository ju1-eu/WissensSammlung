# Name der LaTeX-Datei ohne Erweiterung
TEXFILE = mindmap

# Standardziel
all: $(TEXFILE).pdf

# Regel zum Erzeugen der PDF-Datei
$(TEXFILE).pdf: $(TEXFILE).tex
	# Kompiliert die LaTeX-Datei mit xelatex
	xelatex $(TEXFILE).tex

# Bereinigung der temporären Dateien
clean:
	# Entfernt temporäre Dateien, behält jedoch das PDF bei
	rm -f $(TEXFILE).aux $(TEXFILE).log $(TEXFILE).out $(TEXFILE).toc \
	      $(TEXFILE).fls $(TEXFILE).fdb_latexmk $(TEXFILE).synctex.gz

# Vollständige Bereinigung inklusive PDF
cleanall: clean
	# Entfernt auch das generierte PDF-Dokument
	rm -f $(TEXFILE).pdf

# Hinweise zur Benutzung:
# - 'make' erstellt das PDF-Dokument aus der LaTeX-Datei.
# - 'make clean' entfernt temporäre Dateien, das PDF bleibt erhalten.
# - 'make cleanall' entfernt alle generierten Dateien inklusive des PDFs.
