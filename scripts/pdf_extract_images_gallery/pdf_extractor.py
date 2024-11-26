"""
PDF Kapitel Extraktor

Dieses Skript ermöglicht das Extrahieren von Seitenbereichen aus PDF-Dateien.
Es erstellt eine neue PDF-Datei mit den ausgewählten Seiten und bietet
erweiterte Funktionen wie Komprimierung und Metadaten-Übertragung.

Funktionen:
----------
- Extraktion beliebiger Seitenbereiche
- Beibehaltung der Original-Formatierung
- Automatische Verzeichniserstellung
- Umfangreiche Fehlerprüfung
- Fortschrittsanzeige bei großen PDFs
- Optional: PDF-Komprimierung
- Metadaten-Übertragung
- Detailliertes Logging

Installation:
-----------
1. Virtuelle Umgebung erstellen und aktivieren:
   python3 -m venv venv
   source venv/bin/activate
2. Benötigte Pakete installieren:
   pip install --upgrade pip
   pip install pypdf2

Verwendung:
---------
1. Direkter Aufruf:
   python pdf_extraktor.py
2. Als Modul importieren:
   from pdf_extraktor import extrahiere_kapitel
   extrahiere_kapitel("eingabe.pdf", "ausgabe.pdf", 1, 5)

Autor: Jan Unger (verbessert)
Version: 2.0
Datum: 24.11.2024
"""

import logging
import os
from typing import Any, Dict

from PyPDF2 import PdfReader, PdfWriter

# Logging-Konfiguration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def get_pdf_info(pdf_pfad: str) -> Dict[str, Any]:
    """
    Liest grundlegende Informationen aus einer PDF-Datei.

    Args:
        pdf_pfad: Pfad zur PDF-Datei

    Returns:
        Dict mit Metadaten und Seitenanzahl
    """
    with open(pdf_pfad, "rb") as f:
        pdf = PdfReader(f)
        return {"seiten": len(pdf.pages), "metadata": pdf.metadata}


def validiere_eingaben(
    eingangs_pdf: str, startseite: int, endseite: int, max_size_mb: int = 100
) -> bool:
    """
    Erweiterte Prüfung der Benutzereingaben auf Gültigkeit.

    Args:
        eingangs_pdf: Pfad zur PDF-Datei
        startseite: Gewählte Startseite
        endseite: Gewählte Endseite
        max_size_mb: Maximale erlaubte Dateigröße in MB

    Returns:
        True wenn alle Eingaben gültig sind

    Raises:
        ValueError: Bei ungültigen Eingaben
    """
    # Prüfe Dateiexistenz
    if not os.path.exists(eingangs_pdf):
        raise ValueError(f"Die Datei '{eingangs_pdf}' existiert nicht.")

    # Prüfe Dateiendung
    if not eingangs_pdf.lower().endswith(".pdf"):
        raise ValueError(f"Die Datei '{eingangs_pdf}' ist keine PDF-Datei.")

    # Prüfe Dateigröße
    if os.path.getsize(eingangs_pdf) > max_size_mb * 1024 * 1024:
        raise ValueError(f"Die PDF-Datei ist größer als {max_size_mb}MB.")

    # Prüfe Seitenzahlen
    if startseite > endseite:
        raise ValueError("Die Startseite muss kleiner oder gleich der Endseite sein.")

    if startseite < 1:
        raise ValueError("Die Startseite muss mindestens 1 sein.")

    return True


def extrahiere_kapitel(
    eingangs_pdf_pfad: str,
    ausgangs_pdf_pfad: str,
    startseite: int,
    endseite: int,
    komprimieren: bool = False,
    progress_anzeige: bool = True,
) -> None:
    """
    Extrahiert einen Seitenbereich aus einer PDF-Datei und speichert diesen in einer neuen PDF.

    Args:
        eingangs_pdf_pfad: Pfad zur ursprünglichen PDF-Datei
        ausgangs_pdf_pfad: Pfad, unter dem die neue PDF gespeichert werden soll
        startseite: Erste zu extrahierende Seite (beginnend bei 1)
        endseite: Letzte zu extrahierende Seite (beginnend bei 1)
        komprimieren: Optional - PDF-Inhalt komprimieren
        progress_anzeige: Optional - Fortschrittsbalken anzeigen

    Returns:
        None

    Raises:
        FileNotFoundError: Wenn die Eingabe-PDF nicht gefunden wurde
        PermissionError: Wenn keine Schreibrechte für die Ausgabe-PDF vorliegen
        ValueError: Wenn ungültige Seitenzahlen angegeben wurden
    """
    try:
        # Initialisiere PDF Reader und Writer
        reader = PdfReader(eingangs_pdf_pfad)
        writer = PdfWriter()

        # Übertrage Metadaten wenn vorhanden
        if reader.metadata:
            writer.add_metadata(reader.metadata)

        # Konvertiere von menschlicher Seitenzählung (1-basiert)
        # zu Python-Indexierung (0-basiert)
        startseite_index = startseite - 1
        endseite_index = endseite - 1

        # Validiere die Seitenzahlen
        gesamt_seiten = len(reader.pages)
        if startseite_index < 0 or endseite_index >= gesamt_seiten:
            raise ValueError(
                f"Ungültige Seitenzahlen. Die PDF hat {gesamt_seiten} Seiten. "
                f"Bitte Zahlen zwischen 1 und {gesamt_seiten} eingeben."
            )

        # Extrahiere die gewählten Seiten mit Fortschrittsanzeige
        total_seiten = endseite - startseite + 1
        logging.info(f"Beginne Extraktion von {total_seiten} Seiten...")

        for idx, seitennummer in enumerate(range(startseite_index, endseite_index + 1)):
            page = reader.pages[seitennummer]

            # Optional: Komprimiere Seiteninhalt
            if komprimieren:
                page.compress_content_streams()

            writer.add_page(page)

            # Zeige Fortschritt bei größeren PDFs
            if progress_anzeige and total_seiten > 10:
                print(f"\rVerarbeite Seite {idx + 1}/{total_seiten}", end="")

        # Stelle sicher, dass das Ausgabeverzeichnis existiert
        ausgabe_verzeichnis = os.path.dirname(ausgangs_pdf_pfad)
        if ausgabe_verzeichnis and not os.path.exists(ausgabe_verzeichnis):
            os.makedirs(ausgabe_verzeichnis)

        # Speichere die neue PDF
        with open(ausgangs_pdf_pfad, "wb") as ausgabe_pdf:
            writer.write(ausgabe_pdf)

        # Beende Fortschrittsanzeige
        if progress_anzeige and total_seiten > 10:
            print()  # Neue Zeile nach Fortschrittsbalken

        # Erfolgsmeldung mit Details
        logging.info(f"✓ Kapitel erfolgreich extrahiert und gespeichert unter: {ausgangs_pdf_pfad}")
        logging.info(f"  Extrahierte Seiten: {startseite} bis {endseite}")
        logging.info(f"  Anzahl Seiten: {total_seiten}")

        if komprimieren:
            original_size = os.path.getsize(eingangs_pdf_pfad) / 1024 / 1024
            new_size = os.path.getsize(ausgangs_pdf_pfad) / 1024 / 1024
            logging.info(f"  Dateigröße: {new_size:.1f}MB (Original: {original_size:.1f}MB)")

    except FileNotFoundError:
        logging.error(f"❌ Die Eingabe-PDF '{eingangs_pdf_pfad}' wurde nicht gefunden.")
        raise
    except PermissionError:
        logging.error(f"❌ Keine Berechtigung zum Schreiben der Datei '{ausgangs_pdf_pfad}'.")
        raise
    except ValueError as e:
        logging.error(f"❌ {e}")
        raise
    except Exception as e:
        logging.error(f"❌ Unerwarteter Fehler beim Extrahieren des Kapitels: {e}")
        raise


if __name__ == "__main__":
    try:
        # Banner ausgeben
        print("\nPDF Kapitel Extraktor v2.0")
        print("-" * 30)

        # Standard-Konfiguration
        eingangs_pdf = "PDFs/2024_21_unlocked.pdf"
        ausgangs_pdf = "pdf_extraktion.pdf"

        # PDF-Informationen auslesen
        pdf_info = get_pdf_info(eingangs_pdf)
        max_seiten = pdf_info["seiten"]

        # Benutzereingaben mit Standardwerten
        print(f"\nEingabe-PDF: {eingangs_pdf}")
        print(f"Seitenanzahl: {max_seiten}")

        startseite = int(input("\nStartseite eingeben [1]: ") or "1")
        endseite = int(input(f"Endseite eingeben [{max_seiten}]: ") or str(max_seiten))

        komprimieren = input("PDF komprimieren? (j/N): ").lower() == "j"

        # Eingaben validieren
        validiere_eingaben(eingangs_pdf, startseite, endseite)

        # Kapitel extrahieren
        extrahiere_kapitel(
            eingangs_pdf, ausgangs_pdf, startseite, endseite, komprimieren=komprimieren
        )

    except ValueError as e:
        logging.error(f"❌ Fehler: {e}")
    except KeyboardInterrupt:
        print("\n\nProgramm wurde durch Benutzer abgebrochen.")
        logging.warning("Programm durch Benutzer abgebrochen")
    except Exception as e:
        logging.error(f"❌ Unerwarteter Fehler: {e}", exc_info=True)
