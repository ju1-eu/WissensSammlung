"""
PDF Bilder Extraktor

Dieses Skript extrahiert alle Bilder aus einer PDF-Datei und speichert sie
im gewünschten Format. Es bietet erweiterte Funktionen wie Qualitätskontrolle,
Größenfilterung und detailliertes Logging.

Funktionen:
----------
- Extraktion aller Bildtypen (JPEG, PNG, etc.)
- Qualitätsfilterung nach Auflösung
- Fortschrittsanzeige
- Automatische Bildoptimierung
- Detaillierte Metadaten-Erfassung
- Umfangreiche Fehlerprotokollierung

Installation:
-----------
pip install --upgrade pip
pip install PyMuPDF Pillow rich tqdm

Autor: Jan Unger
Version: 2.0
Datum: 24.11.2024
"""

import io
import logging
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional, Tuple, Union

import fitz  # type: ignore
from PIL import Image
from rich.console import Console
from rich.progress import track

# Console für formatierte Ausgabe
console = Console()

# Logging-Konfiguration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("pdf_image_extraction.log"), logging.StreamHandler(sys.stdout)],
)


@dataclass
class ImageConfig:
    """Konfigurationsdaten für die Bildextraktion"""

    min_width: int = 100  # Minimale Bildbreite in Pixeln
    min_height: int = 100  # Minimale Bildhöhe in Pixeln
    max_size_mb: float = 20.0  # Maximale Bildgröße in MB
    quality: int = 90  # JPEG Qualität
    optimize: bool = True  # Bildoptimierung aktivieren


class PDFImageExtractor:
    """Klasse zur Handhabung der PDF-Bildextraktion"""

    def __init__(
        self,
        pdf_path: str,
        output_dir: str = "images",
        image_prefix: str = "image",
        project_name: str = "project",
        image_format: str = "png",
        config: Optional[ImageConfig] = None,
    ):
        self.pdf_path = Path(pdf_path)
        self.output_dir = Path(output_dir)
        self.image_prefix = image_prefix
        self.project_name = project_name
        self.image_format = image_format.lower()
        self.config = config or ImageConfig()
        self.stats: Dict[str, Union[int, datetime]] = {
            "total_images": 0,
            "successful": 0,
            "failed": 0,
            "skipped": 0,
            "start_time": datetime.now(),
        }

        # Validiere Eingaben
        self._validate_inputs()

    def _validate_inputs(self) -> None:
        """Überprüft die Gültigkeit der Eingabeparameter"""
        if not self.pdf_path.exists():
            raise FileNotFoundError(f"PDF-Datei nicht gefunden: {self.pdf_path}")

        if self.image_format not in ["png", "jpg", "jpeg", "webp"]:
            raise ValueError(f"Nicht unterstütztes Bildformat: {self.image_format}")

        # Erstelle Ausgabeverzeichnis
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def _get_filename(self, counter: int) -> Path:
        """Generiert einen formatierten Dateinamen"""
        return (
            self.output_dir
            / f"{counter:04d}_{self.image_prefix}_{self.project_name}.{self.image_format}"
        )

    def _is_valid_image(self, image: Image.Image) -> bool:
        """Prüft ob ein Bild den Qualitätskriterien entspricht"""
        width, height = image.size
        return width >= self.config.min_width and height >= self.config.min_height

    def _optimize_image(self, image: Image.Image) -> Image.Image:
        """Optimiert ein Bild für die Speicherung"""
        if self.config.optimize:
            # Konvertiere zu RGB wenn RGBA
            if image.mode == "RGBA":
                background = Image.new("RGB", image.size, (255, 255, 255))
                background.paste(image, mask=image.split()[3])
                image = background

            # Optimiere Bildgröße wenn nötig
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format=self.image_format.upper())
            size_mb = len(img_byte_arr.getvalue()) / (1024 * 1024)

            if size_mb > self.config.max_size_mb:
                quality = int(self.config.quality * (self.config.max_size_mb / size_mb))
                image_io = io.BytesIO()
                image.save(
                    image_io, format=self.image_format.upper(), quality=quality, optimize=True
                )
                return Image.open(image_io)

        return image

    def _extract_image_info(self, image_data: Dict[str, Any]) -> Tuple[Image.Image, Dict[str, Any]]:
        """Extrahiert Bilddaten und Metadaten"""
        image_bytes = image_data["image"]
        image = Image.open(io.BytesIO(image_bytes))

        metadata = {
            "size": len(image_bytes),
            "width": image.width,
            "height": image.height,
            "format": image.format,
            "mode": image.mode,
            "dpi": image.info.get("dpi", (72, 72)),
        }

        return image, metadata

    def extract_images(self) -> Dict[str, Any]:
        """Hauptmethode zur Extraktion aller Bilder aus der PDF"""
        try:
            pdf_document = fitz.open(self.pdf_path)
            total_pages = len(pdf_document)

            console.rule(f"[bold green]Extrahiere Bilder aus {self.pdf_path.name}")
            console.print(f"Gefundene Seiten: {total_pages}")

            for page_num in track(range(total_pages), description="Verarbeite Seiten..."):
                page = pdf_document[page_num]

                try:
                    image_list = page.get_images()

                    for image_index, image_info in enumerate(image_list):
                        # Prüfe den Typ vor der Addition
                        if isinstance(self.stats["total_images"], int):
                            self.stats["total_images"] += 1
                        else:
                            raise TypeError(
                                f"Unerwarteter Typ für 'total_images': {type(self.stats['total_images'])}"
                            )

                        try:
                            # Bild extrahieren
                            base_image = pdf_document.extract_image(image_info[0])
                            image, metadata = self._extract_image_info(base_image)

                            # Bild validieren
                            if not self._is_valid_image(image):
                                if isinstance(self.stats["skipped"], int):
                                    self.stats["skipped"] += 1
                                else:
                                    raise TypeError(
                                        f"Unerwarteter Typ für 'skipped': {type(self.stats['skipped'])}"
                                    )
                                logging.warning(
                                    f"Bild übersprungen (Seite {page_num + 1}, "
                                    f"Index {image_index}): Zu kleine Auflösung "
                                    f"({image.width}x{image.height}px)"
                                )
                                continue

                            # Bild optimieren
                            image = self._optimize_image(image)

                            # Bild speichern
                            if isinstance(self.stats["successful"], int):
                                filename = self._get_filename(self.stats["successful"] + 1)
                                image.save(
                                    filename,
                                    format=self.image_format.upper(),
                                    quality=(
                                        self.config.quality
                                        if self.image_format in ["jpg", "jpeg"]
                                        else None
                                    ),
                                    optimize=self.config.optimize,
                                )

                                self.stats["successful"] += 1
                                logging.info(
                                    f"Bild gespeichert: {filename.name} "
                                    f"({metadata['width']}x{metadata['height']}px)"
                                )
                            else:
                                raise TypeError(
                                    f"Unerwarteter Typ für 'successful': {type(self.stats['successful'])}"
                                )

                        except Exception as e:
                            if isinstance(self.stats["failed"], int):
                                self.stats["failed"] += 1
                            else:
                                raise TypeError(
                                    f"Unerwarteter Typ für 'failed': {type(self.stats['failed'])}"
                                )
                            logging.error(
                                f"Fehler bei Bild {image_index} auf Seite {page_num + 1}: {str(e)}"
                            )
                            continue

                except Exception as e:
                    logging.error(f"Fehler bei Seite {page_num + 1}: {str(e)}")
                    continue

            pdf_document.close()
            self._print_summary()
            return self.stats

        except Exception as e:
            logging.error(f"Kritischer Fehler: {str(e)}")
            raise

    def _print_summary(self) -> None:
        """Gibt eine Zusammenfassung der Extraktion aus"""
        if isinstance(self.stats["start_time"], datetime):
            duration = datetime.now() - self.stats["start_time"]

            console.rule("[bold green]Zusammenfassung")
            console.print(f"Verarbeitungszeit: {duration.total_seconds():.1f} Sekunden")
            console.print(f"Gefundene Bilder: {self.stats['total_images']}")
            console.print(f"Erfolgreich extrahiert: {self.stats['successful']}")
            console.print(f"Übersprungen: {self.stats['skipped']}")
            console.print(f"Fehlgeschlagen: {self.stats['failed']}")


if __name__ == "__main__":
    try:
        # Konfiguration
        PDF_FILE = "audi_ppe.pdf"
        OUTPUT_DIR = "images"
        PROJECT_NAME = "audi_ppe"

        # Benutzerdefinierte Konfiguration
        config = ImageConfig(
            min_width=200,  # Minimale Breite
            min_height=200,  # Minimale Höhe
            max_size_mb=10.0,  # Maximale Bildgröße
            quality=90,  # JPEG Qualität
            optimize=True,  # Bildoptimierung
        )

        # Extraktor initialisieren und ausführen
        extractor = PDFImageExtractor(
            pdf_path=PDF_FILE,
            output_dir=OUTPUT_DIR,
            project_name=PROJECT_NAME,
            image_format="png",
            config=config,
        )

        stats = extractor.extract_images()

    except KeyboardInterrupt:
        console.print("\n[yellow]Programm durch Benutzer abgebrochen[/yellow]")
        sys.exit(1)
    except Exception as e:
        console.print(f"\n[red]Kritischer Fehler: {str(e)}[/red]")
        logging.error("Kritischer Fehler", exc_info=True)
        sys.exit(1)
