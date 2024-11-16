"""
PDF Kapitel Extraktor

Dieses Skript ermöglicht das Extrahieren von Seitenbereichen aus PDF-Dateien.
Es erstellt eine neue PDF-Datei mit den ausgewählten Seiten.

Funktionen:
----------
- Extraktion beliebiger Seitenbereiche
- Beibehaltung der Original-Formatierung
- Automatische Verzeichniserstellung
- Umfangreiche Fehlerprüfung

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

Autor: Jan Unger
Version: 1.0
Datum: 09.11.2024
"""

import os
from PyPDF2 import PdfReader, PdfWriter

def extrahiere_kapitel(eingangs_pdf_pfad, ausgangs_pdf_pfad, startseite, endseite):
    """
    Extrahiert einen Seitenbereich aus einer PDF-Datei und speichert diesen in einer neuen PDF.
    
    Args:
    -----
        eingangs_pdf_pfad (str): 
            Pfad zur ursprünglichen PDF-Datei
        ausgangs_pdf_pfad (str): 
            Pfad, unter dem die neue PDF gespeichert werden soll
        startseite (int): 
            Erste zu extrahierende Seite (beginnend bei 1)
        endseite (int): 
            Letzte zu extrahierende Seite (beginnend bei 1)
            
    Returns:
    --------
        None
            
    Raises:
    -------
        FileNotFoundError: 
            Wenn die Eingabe-PDF nicht gefunden wurde
        PermissionError: 
            Wenn keine Schreibrechte für die Ausgabe-PDF vorliegen
        ValueError: 
            Wenn ungültige Seitenzahlen angegeben wurden
    """
    try:
        # Initialisiere PDF Reader und Writer
        reader = PdfReader(eingangs_pdf_pfad)
        writer = PdfWriter()

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

        # Extrahiere die gewählten Seiten
        for seitennummer in range(startseite_index, endseite_index + 1):
            writer.add_page(reader.pages[seitennummer])

        # Stelle sicher, dass das Ausgabeverzeichnis existiert
        ausgabe_verzeichnis = os.path.dirname(ausgangs_pdf_pfad)
        if ausgabe_verzeichnis and not os.path.exists(ausgabe_verzeichnis):
            os.makedirs(ausgabe_verzeichnis)

        # Speichere die neue PDF
        with open(ausgangs_pdf_pfad, 'wb') as ausgabe_pdf:
            writer.write(ausgabe_pdf)

        # Erfolgsmeldung mit Details
        print(f"✓ Kapitel erfolgreich extrahiert und gespeichert unter: {ausgangs_pdf_pfad}")
        print(f"  Extrahierte Seiten: {startseite} bis {endseite}")
        print(f"  Anzahl Seiten: {endseite - startseite + 1}")
        
    except FileNotFoundError:
        print(f"❌ Fehler: Die Eingabe-PDF '{eingangs_pdf_pfad}' wurde nicht gefunden.")
    except PermissionError:
        print(f"❌ Fehler: Keine Berechtigung zum Schreiben der Datei '{ausgangs_pdf_pfad}'.")
    except ValueError as e:
        print(f"❌ Fehler: {e}")
    except Exception as e:
        print(f"❌ Unerwarteter Fehler beim Extrahieren des Kapitels: {e}")

def validiere_eingaben(eingangs_pdf, startseite, endseite):
    """
    Prüft die Benutzereingaben auf Gültigkeit.
    
    Args:
    -----
        eingangs_pdf (str): Pfad zur PDF-Datei
        startseite (int): Gewählte Startseite
        endseite (int): Gewählte Endseite
        
    Returns:
    --------
        bool: True wenn alle Eingaben gültig sind
        
    Raises:
    -------
        ValueError: Bei ungültigen Eingaben
    """
    # Prüfe Dateiexistenz
    if not os.path.exists(eingangs_pdf):
        raise ValueError(f"Die Datei '{eingangs_pdf}' existiert nicht.")
        
    # Prüfe Seitenzahlen
    if startseite > endseite:
        raise ValueError("Die Startseite muss kleiner oder gleich der Endseite sein.")
        
    if startseite < 1:
        raise ValueError("Die Startseite muss mindestens 1 sein.")
        
    return True

if __name__ == "__main__":
    # Konfiguration
    eingangs_pdf = "Tipler-Physik-Arbeitsbuch.pdf"  # Pfad zur Original-PDF
    ausgangs_pdf = "pdf_extraktion.pdf"             # Pfad zur neuen PDF
    
    try:
        # Banner ausgeben
        print("\nPDF Kapitel Extraktor")
        print("-" * 30)
        
        # Benutzereingaben einlesen
        print(f"\nEingabe-PDF: {eingangs_pdf}")
        startseite = int(input("Startseite eingeben (z.B. 1): "))
        endseite = int(input("Endseite eingeben: "))
        
        # Eingaben validieren
        validiere_eingaben(eingangs_pdf, startseite, endseite)
            
        # Kapitel extrahieren
        extrahiere_kapitel(eingangs_pdf, ausgangs_pdf, startseite, endseite)
        
    except ValueError as e:
        print(f"❌ Fehler: {e}")
    except KeyboardInterrupt:
        print("\n\nProgramm wurde durch Benutzer abgebrochen.")
    except Exception as e:
        print(f"❌ Unerwarteter Fehler: {e}")