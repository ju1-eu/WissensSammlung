"""
HTML Galerie Generator

Dieses Skript erstellt eine responsive HTML-Galerie mit Lightbox-Funktionalität
für Bildersammlungen. Es bietet erweiterte Funktionen wie Bildkomprimierung,
verschiedene Layouts und Themes.

Funktionen:
----------
- Responsive Grid-Layout
- Lightbox Integration
- Verschiedene Theme-Optionen
- Automatische Bildoptimierung
- SEO-freundliche Ausgabe
- Konfigurierbare Layouts
- Thumbnail-Generierung

Installation:
-----------
pip install pillow

Autor: Jan Unger (verbessert)
Version: 2.0
Datum: 24.11.2024
"""

import logging
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

from PIL import Image

# Logging Konfiguration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("gallery_generation.log"), logging.StreamHandler()],
)


@dataclass
class GalleryConfig:
    """Konfiguration für die Galerie-Generierung"""

    title: str = "Bildergalerie"
    subtitle: Optional[str] = None
    theme: str = "light"  # light, dark, custom
    columns_desktop: int = 4
    columns_tablet: int = 3
    columns_mobile: int = 2
    thumbnail_size: tuple = (300, 300)
    generate_thumbnails: bool = True
    image_quality: int = 85
    enable_lazyload: bool = True
    enable_fullscreen: bool = True
    enable_download: bool = False
    enable_sorting: bool = True
    enable_filtering: bool = True
    image_formats: tuple = (".png", ".jpg", ".jpeg", ".webp")


class GalleryGenerator:
    """Hauptklasse zur Generierung der HTML-Galerie"""

    def __init__(
        self,
        image_dir: str,
        project_name: str,
        output_dir: str = "gallery",
        config: Optional[GalleryConfig] = None,
    ):
        self.image_dir = Path(image_dir)
        self.project_name = project_name
        self.output_dir = Path(output_dir)
        self.config = config or GalleryConfig()
        self.thumbnail_dir = self.output_dir / "thumbnails"

        # Validierung und Initialisierung
        self._setup_directories()

    def _setup_directories(self) -> None:
        """Erstellt benötigte Verzeichnisse"""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        if self.config.generate_thumbnails:
            self.thumbnail_dir.mkdir(parents=True, exist_ok=True)

    def _get_theme_css(self) -> str:
        """Generiert das CSS basierend auf dem gewählten Theme"""
        themes = {
            "light": {
                "bg_color": "#f0f0f0",
                "text_color": "#333333",
                "card_bg": "#ffffff",
                "border_color": "#dddddd",
                "shadow": "0 2px 5px rgba(0, 0, 0, 0.1)",
            },
            "dark": {
                "bg_color": "#1a1a1a",
                "text_color": "#ffffff",
                "card_bg": "#2d2d2d",
                "border_color": "#404040",
                "shadow": "0 2px 5px rgba(0, 0, 0, 0.3)",
            },
        }

        theme = themes.get(self.config.theme, themes["light"])

        return f"""
            :root {{
                --bg-color: {theme['bg_color']};
                --text-color: {theme['text_color']};
                --card-bg: {theme['card_bg']};
                --border-color: {theme['border_color']};
                --shadow: {theme['shadow']};
            }}
        """

    def _generate_css(self) -> str:
        """Generiert das CSS für die Galerie"""
        css = f"""
            {self._get_theme_css()}
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: var(--bg-color);
                color: var(--text-color);
                margin: 0;
                padding: 20px;
                line-height: 1.6;
            }}

            .gallery-header {{
                text-align: center;
                padding: 2rem 1rem;
            }}

            h1 {{
                font-size: 2.5rem;
                margin-bottom: 0.5rem;
            }}

            .subtitle {{
                font-size: 1.2rem;
                opacity: 0.8;
            }}

            .controls {{
                max-width: 1400px;
                margin: 1rem auto;
                display: flex;
                gap: 1rem;
                flex-wrap: wrap;
                justify-content: center;
                padding: 1rem;
            }}

            .gallery {{
                display: grid;
                grid-template-columns: repeat({self.config.columns_desktop}, 1fr);
                gap: 20px;
                padding: 20px;
                max-width: 1400px;
                margin: 0 auto;
            }}

            .gallery-item {{
                position: relative;
                background: var(--card-bg);
                border-radius: 8px;
                overflow: hidden;
                box-shadow: var(--shadow);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }}

            .gallery-item:hover {{
                transform: translateY(-5px);
                box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            }}

            .gallery-item img {{
                width: 100%;
                height: 100%;
                object-fit: cover;
                aspect-ratio: 4/3;
            }}

            .image-info {{
                position: absolute;
                bottom: 0;
                left: 0;
                right: 0;
                background: rgba(0, 0, 0, 0.7);
                color: white;
                padding: 0.5rem;
                transform: translateY(100%);
                transition: transform 0.3s ease;
            }}

            .gallery-item:hover .image-info {{
                transform: translateY(0);
            }}

            @media (max-width: 1200px) {{
                .gallery {{
                    grid-template-columns: repeat({self.config.columns_tablet}, 1fr);
                }}
            }}

            @media (max-width: 768px) {{
                .gallery {{
                    grid-template-columns: repeat({self.config.columns_mobile}, 1fr);
                }}
                h1 {{
                    font-size: 2rem;
                }}
            }}
        """
        return css

    def _create_thumbnail(self, image_path: Path) -> Path:
        """
        Erstellt ein Thumbnail für ein Bild

        Parameter:
            image_path (Path): Pfad zum Originalbild

        Rückgabe:
            Path: Pfad zum erstellten Thumbnail oder zum Originalbild,
                wenn Thumbnail-Generierung deaktiviert ist
        """
        if not self.config.generate_thumbnails:
            return image_path

        # Thumbnail-Pfad mit "thumb_" Prefix erstellen
        thumbnail_path = self.thumbnail_dir / f"thumb_{image_path.name}"

        # Nur ein neues Thumbnail erstellen, wenn es noch nicht existiert
        if not thumbnail_path.exists():
            with Image.open(image_path) as img:
                img.thumbnail(self.config.thumbnail_size)
                img.save(thumbnail_path, quality=self.config.image_quality, optimize=True)
                logging.info(f"Thumbnail erstellt: {thumbnail_path}")

        return thumbnail_path

    def _collect_images(self) -> List[Dict]:
        """Sammelt alle relevanten Bilder mit Metadaten"""
        images = []
        for file in self.image_dir.iterdir():
            if file.suffix.lower() in self.config.image_formats and self.project_name in file.name:
                try:
                    with Image.open(file) as img:
                        images.append(
                            {
                                "path": file,
                                "name": file.stem,
                                "size": file.stat().st_size,
                                "modified": datetime.fromtimestamp(file.stat().st_mtime),
                                "dimensions": img.size,
                            }
                        )
                except Exception as e:
                    logging.warning(f"Konnte Bild nicht verarbeiten: {file.name} - {e}")

        return sorted(images, key=lambda x: x["name"])

    def generate_gallery(self) -> None:
        """Generiert die komplette Galerie"""
        try:
            # Sammle Bilder
            images = self._collect_images()
            if not images:
                raise ValueError(f"Keine Bilder im Verzeichnis {self.image_dir} gefunden")

            # Generiere HTML
            html_content = self._generate_html(images)
            css_content = self._generate_css()

            # Schreibe Dateien
            html_file = self.output_dir / f"{self.project_name}_gallery.html"
            css_file = self.output_dir / "gallery_styles.css"

            html_file.write_text(html_content, encoding="utf-8")
            css_file.write_text(css_content, encoding="utf-8")

            # Kopiere Bilder wenn nötig
            if self.output_dir != self.image_dir.parent:
                for image in images:
                    shutil.copy2(image["path"], self.output_dir)

            logging.info(
                f"""
                Galerie erfolgreich erstellt:
                - HTML: {html_file}
                - CSS: {css_file}
                - Bilder verarbeitet: {len(images)}
                - Thumbnails erstellt: {self.config.generate_thumbnails}
            """
            )

        except Exception as e:
            logging.error(f"Fehler bei der Galerie-Generierung: {e}")
            raise

    def _generate_html(self, images: List[Dict]) -> str:
        """Generiert den HTML-Code für die Galerie"""
        html = f"""<!DOCTYPE html>
        <html lang="de">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta name="description" content="{self.config.title}">
            <title>{self.config.title}</title>
            <link rel="stylesheet" href="gallery_styles.css">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/css/lightbox.min.css">
            {self._get_optional_head_content()}
        </head>
        <body>
            <div class="gallery-header">
                <h1>{self.config.title}</h1>
                {f'<div class="subtitle">{self.config.subtitle}</div>' if self.config.subtitle else ''}
            </div>
            {self._generate_controls() if self.config.enable_sorting or self.config.enable_filtering else ''}
            <div class="gallery" id="gallery">
                {self._generate_gallery_items(images)}
            </div>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/js/lightbox-plus-jquery.min.js"></script>
            {self._get_optional_scripts()}
        </body>
        </html>
        """
        return html

    def _get_optional_head_content(self) -> str:
        """Generiert optionale Head-Inhalte basierend auf der Konfiguration"""
        content = []

        if self.config.enable_lazyload:
            content.append('<link rel="preload" as="image" href="loading.gif">')

        return "\n".join(content)

    def _generate_controls(self) -> str:
        """Generiert Filter- und Sortierkontrollen"""
        controls = ['<div class="controls">']

        if self.config.enable_sorting:
            controls.append(
                """
                <select id="sort-select" onchange="sortGallery()">
                    <option value="name">Nach Name</option>
                    <option value="date">Nach Datum</option>
                    <option value="size">Nach Größe</option>
                </select>
            """
            )

        if self.config.enable_filtering:
            controls.append(
                """
                <input type="text" id="filter-input"
                       placeholder="Suchen..." onkeyup="filterGallery()">
            """
            )

        controls.append("</div>")
        return "\n".join(controls)

    def _generate_gallery_items(self, images: List[Dict]) -> str:
        """Generiert die HTML-Struktur für die Galerie-Items"""
        items = []
        for img in images:
            # Thumbnail erstellen und relative Pfade abrufen
            thumbnail = self._create_thumbnail(img["path"])

            # Relative Pfade für Thumbnail und Originalbild berechnen
            thumbnail_path = f"thumbnails/{thumbnail.name}"
            image_path = img["path"].name

            item = f"""
                <div class="gallery-item" data-name="{img['name']}"
                    data-date="{img['modified'].isoformat()}"
                    data-size="{img['size']}">
                    <a href="{image_path}" data-lightbox="gallery"
                    data-title="{img['name']}">
                        <img src="{thumbnail_path}" alt="{img['name']}"
                            loading="lazy" width="{img['dimensions'][0]}"
                            height="{img['dimensions'][1]}">
                    </a>
                    <div class="image-info">
                        <div class="image-title">{img['name']}</div>
                        <div class="image-meta">
                            {img['dimensions'][0]}x{img['dimensions'][1]} px
                        </div>
                    </div>
                </div>
            """
            items.append(item)

        return "\n".join(items)

    def _get_optional_scripts(self) -> str:
        """Generiert optionale JavaScript-Funktionen"""
        scripts = ["<script>"]

        if self.config.enable_sorting:
            scripts.append(
                """
                function sortGallery() {
                    const gallery = document.getElementById('gallery');
                    const items = Array.from(gallery.children);
                    const sortBy = document.getElementById('sort-select').value;
                    items.sort((a, b) => {
                        const aValue = a.dataset[sortBy];
                        const bValue = b.dataset[sortBy];
                        return aValue.localeCompare(bValue);
                    });
                    items.forEach(item => gallery.appendChild(item));
                }
            """
            )

        if self.config.enable_filtering:
            scripts.append(
                """
                function filterGallery() {
                    const filter = document.getElementById('filter-input').value.toLowerCase();
                    const items = document.getElementsByClassName('gallery-item');
                    Array.from(items).forEach(item => {
                        const name = item.dataset.name.toLowerCase();
                        item.style.display = name.includes(filter) ? '' : 'none';
                    });
                }
            """
            )

        scripts.append("</script>")
        return "\n".join(scripts)


def main():
    """
    Hauptfunktion zum Erstellen der Galerie
    """
    try:
        # Konfiguration
        config = GalleryConfig(
            title="Audi PPE Technische Illustrationen",
            subtitle="Technische Dokumentation und Visualisierung",
            theme="light",
            columns_desktop=4,
            columns_tablet=3,
            columns_mobile=2,
            thumbnail_size=(300, 300),
            generate_thumbnails=True,
            image_quality=85,
            enable_lazyload=True,
            enable_fullscreen=True,
            enable_sorting=True,
            enable_filtering=True,
        )

        # Generator initialisieren und ausführen
        generator = GalleryGenerator(
            image_dir="images", project_name="audi_ppe", output_dir="gallery", config=config
        )

        # Galerie generieren
        generator.generate_gallery()

        print(
            """
        ✓ Galerie wurde erfolgreich erstellt!
        Nächste Schritte:
        1. Öffne die HTML-Datei im Browser
        2. Überprüfe die generierten Thumbnails
        3. Teste die Sortier- und Filterfunktionen
        """
        )

    except FileNotFoundError as e:
        logging.error(f"Verzeichnis oder Datei nicht gefunden: {e}")
        print(f"\n❌ Fehler: {e}")
    except Exception as e:
        logging.error("Unerwarteter Fehler bei der Galerie-Generierung", exc_info=True)
        print(f"\n❌ Ein unerwarteter Fehler ist aufgetreten: {e}")


if __name__ == "__main__":
    main()
