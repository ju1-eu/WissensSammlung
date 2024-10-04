# Makefile HTML

# Pfade
DOCS_DIR=docs
CSS_FILE=$(DOCS_DIR)/markdown_styles.css
TEMPLATE_FILE=template.html
CODE_DIR=code
SCRIPTS_DIR=scripts
ASSETS_DIR=assets
INDEX_MD=$(DOCS_DIR)/start.md
INDEX_HTML=$(DOCS_DIR)/start.html
ADD_FRONT_MATTER_SCRIPT=$(SCRIPTS_DIR)/add_front_matter.sh

# Farben für Konsolenausgabe
GREEN=\033[0;32m
YELLOW=\033[0;33m
NC=\033[0m # No Color

# Ziel: Alle Dokumente konvertieren und Index aktualisieren
all: html index
	@echo "${GREEN}Build erfolgreich abgeschlossen.${NC}"

# Füge Front Matter hinzu
add_front_matter:
	@echo "${YELLOW}Füge Front Matter hinzu...${NC}"
	@./$(ADD_FRONT_MATTER_SCRIPT)
	@echo "${GREEN}Front Matter erfolgreich hinzugefügt.${NC}"

# Markdown zu HTML konvertieren mit Pandoc, benutzerdefiniertem CSS und Template
html: add_front_matter
	@echo "${YELLOW}Konvertiere Markdown-Dateien zu HTML...${NC}"
	@find $(DOCS_DIR) -type f -name "*.md" -exec sh -c '\
		echo "${YELLOW}Konvertiere $$(basename "$$1")...${NC}" && \
		pandoc "$$1" -o "$$(dirname "$$1")/$$(basename "$$1" .md).html" \
		--mathjax --css=$(CSS_FILE) --template=$(TEMPLATE_FILE) && \
		echo "${GREEN}$$(basename "$$1") erfolgreich konvertiert.${NC}"' _ {} \;

# Index.md generieren und dann zu HTML konvertieren
index: generate_index_md
	@echo "${YELLOW}Konvertiere start.md zu HTML...${NC}"
	@pandoc $(INDEX_MD) -o $(INDEX_HTML) --mathjax --css=$(CSS_FILE) --template=$(TEMPLATE_FILE) --metadata title="Startseite"
	@echo "${GREEN}start.html erfolgreich erstellt.${NC}"

# Generiere die start.md mit Links zu allen HTML-Dokumenten
generate_index_md: $(DOCS_DIR)/start.md

$(DOCS_DIR)/start.md: 
	@echo "${YELLOW}Generiere start.md...${NC}"
	@echo "---" > $(INDEX_MD)
	@echo "title: Startseite" >> $(INDEX_MD)
	@echo "---" >> $(INDEX_MD)
	@echo "" >> $(INDEX_MD)
	@echo "# Start" >> $(INDEX_MD)
	@echo "" >> $(INDEX_MD)
	@find $(DOCS_DIR) -maxdepth 1 -type f -name "*.html" ! -name "start.html" | sort | while read file; do \
		file_name=$$(basename "$$file" .html); \
		title=$$(echo $$file_name | sed 's/_/ /g'); \
		echo "- [$$title]($$file_name.html)" >> $(INDEX_MD); \
	done
	@echo "" >> $(INDEX_MD)
	@echo "## KI" >> $(INDEX_MD)
	@echo "" >> $(INDEX_MD)
	@find $(DOCS_DIR)/KI -type f -name "*.html" | sort | while read file; do \
		rel_path=$$(echo $$file | sed 's|$(DOCS_DIR)/||'); \
		file_name=$$(basename "$$file" .html); \
		title=$$(echo $$file_name | sed 's/_/ /g'); \
		echo "- [$$title]($$rel_path)" >> $(INDEX_MD); \
	done

# temporäre Dateien löschen
clean:
	@echo "${YELLOW}Lösche generierte HTML-Dateien...${NC}"
	@find $(DOCS_DIR) -type f -name "*.html" ! -name "start.html" -exec rm {} \;
	@rm -f $(INDEX_HTML) $(INDEX_MD)
	@echo "${GREEN}Aufräumen abgeschlossen.${NC}"

.PHONY: all html index generate_index_md clean add_front_matter