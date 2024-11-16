"""
YouTube Text Extraktor

Dieses Skript ermöglicht das Extrahieren von Text aus YouTube-Videos durch:
1. Abrufen vorhandener Untertitel
2. Falls keine Untertitel verfügbar sind: Download und Transkription der Audiospur

Voraussetzungen:
---------------
pip install youtube-transcript-api pytube whisper

Verwendung:
----------
1. Skript direkt ausführen:
   python youtube_extraktor.py

2. Als Modul importieren:
   from youtube_extraktor import extrahiere_text_aus_video
   text = extrahiere_text_aus_video("VIDEO_URL")

Autor: Jan Unger
Version: 1.0
Datum: 09.11.2024
"""

from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
import whisper
import os
import re

def prüfe_url(url):
    """
    Überprüft die Gültigkeit einer YouTube-URL.
    
    Args:
        url (str): Zu prüfende YouTube-URL
        
    Returns:
        bool: True wenn URL gültig
        
    Raises:
        ValueError: Wenn URL ungültig
    """
    youtube_regex = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'
    if not re.match(youtube_regex, url):
        raise ValueError("Die eingegebene URL ist keine gültige YouTube-URL")
    return True

def hole_video_id(url):
    """
    Extrahiert die Video-ID aus verschiedenen YouTube-URL-Formaten.
    Unterstützt: 
    - Standard-URLs (watch?v=...)
    - Kurzlinks (youtu.be/...)
    - Eingebettete URLs
    
    Args:
        url (str): YouTube-URL in beliebigem Format
        
    Returns:
        str: Extrahierte Video-ID
        
    Raises:
        ValueError: Wenn keine Video-ID gefunden wurde
    """
    try:
        if 'watch?v=' in url:
            return url.split('watch?v=')[1].split('&')[0]
        elif 'youtu.be/' in url:
            return url.split('youtu.be/')[1]
        else:
            return url.split('/')[-1]
    except Exception as e:
        raise ValueError(f"Konnte Video-ID nicht aus URL extrahieren: {e}")

def hole_untertitel(video_id):
    """
    Versucht die Untertitel eines Videos zu extrahieren.
    Probiert zunächst manuell erstellte deutsche Untertitel,
    danach automatisch generierte.
    
    Args:
        video_id (str): YouTube Video-ID
        
    Returns:
        str: Extrahierter Text aus den Untertiteln oder None wenn keine verfügbar
        
    Hinweise:
        - Versucht zuerst manuell erstellte deutsche Untertitel
        - Falls nicht verfügbar, werden automatisch generierte Untertitel probiert
        - Gibt None zurück, wenn gar keine Untertitel verfügbar sind
    """
    try:
        # Versuche zuerst manuell erstellte deutsche Untertitel
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['de'])
        return ' '.join([eintrag['text'] for eintrag in transcript])
    except Exception as e:
        print(f"Keine manuellen deutschen Untertitel gefunden: {e}")
        try:
            # Versuche als Fallback automatisch generierte Untertitel
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['de-generated'])
            return ' '.join([eintrag['text'] for eintrag in transcript])
        except:
            return None

def extrahiere_audio(url, ausgabepfad='audio.mp3'):
    """
    Lädt die Audiospur eines YouTube-Videos in bestmöglicher Qualität herunter.
    
    Args:
        url (str): YouTube-URL
        ausgabepfad (str): Pfad zum Speichern der Audiodatei
        
    Returns:
        str: Pfad zur heruntergeladenen Audiodatei oder None bei Fehler
        
    Hinweise:
        - Verwendet den Audio-Stream mit der höchsten Bitrate
        - Löscht bereits existierende Dateien am Ausgabepfad
        - Zeigt Fortschritt des Downloads an
    """
    try:
        # Erstelle YouTube-Objekt und hole Video-Informationen
        yt = YouTube(url)
        print(f"Verarbeite Video: {yt.title}")
        
        # Wähle den Audio-Stream mit der höchsten Qualität
        video = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        
        if not video:
            raise Exception("Kein Audio-Stream gefunden")
            
        # Lösche existierende Datei falls vorhanden
        if os.path.exists(ausgabepfad):
            os.remove(ausgabepfad)
            
        print("Lade Audio herunter...")
        video.download(filename=ausgabepfad)
        return ausgabepfad
        
    except Exception as e:
        print(f"Fehler beim Herunterladen des Audios: {e}")
        return None

def transkribiere_audio(audio_pfad):
    """
    Transkribiert eine Audiodatei mithilfe des Whisper Models.
    
    Args:
        audio_pfad (str): Pfad zur zu transkribierenden Audiodatei
        
    Returns:
        str: Transkribierter Text oder None bei Fehler
        
    Hinweise:
        - Verwendet das Whisper "base" Modell
        - Sprache ist auf Deutsch eingestellt
        - Kann je nach Länge der Audiodatei einige Zeit in Anspruch nehmen
    """
    try:
        print("Lade Whisper Modell...")
        model = whisper.load_model("base")
        
        print("Transkribiere Audio...")
        ergebnis = model.transcribe(audio_pfad, language="de")
        return ergebnis["text"]
        
    except Exception as e:
        print(f"Fehler bei der Transkription: {e}")
        return None

def extrahiere_text_aus_video(url):
    """
    Hauptfunktion zum Extrahieren des Textes aus einem YouTube-Video.
    Versucht zunächst Untertitel zu laden, falls nicht verfügbar wird
    die Audiospur heruntergeladen und transkribiert.
    
    Args:
        url (str): YouTube-URL des zu verarbeitenden Videos
        
    Returns:
        str: Extrahierter Text oder Fehlermeldung
        
    Ablauf:
        1. URL-Validierung
        2. Extraktion der Video-ID
        3. Versuch Untertitel zu laden
        4. Falls keine Untertitel: Audio-Download und Transkription
        5. Aufräumen temporärer Dateien
    """
    try:
        # Prüfe zuerst die URL
        prüfe_url(url)
        
        # Hole Video-ID
        video_id = hole_video_id(url)
        print(f"Video-ID: {video_id}")
        
        # Versuche zuerst vorhandene Untertitel zu bekommen
        print("Suche nach vorhandenen Untertiteln...")
        text = hole_untertitel(video_id)
        
        if text:
            print("✓ Untertitel erfolgreich geladen!")
            return text
            
        # Wenn keine Untertitel verfügbar, lade Audio herunter und transkribiere
        print("Keine Untertitel gefunden. Starte Audio-Download...")
        audio_pfad = extrahiere_audio(url)
        
        if not audio_pfad:
            raise Exception("Audio konnte nicht heruntergeladen werden")
        
        # Transkribiere Audio
        text = transkribiere_audio(audio_pfad)
        
        # Räume auf
        if os.path.exists(audio_pfad):
            os.remove(audio_pfad)
            print("✓ Audio-Datei aufgeräumt")
            
        if not text:
            raise Exception("Transkription fehlgeschlagen")
            
        return text
        
    except Exception as e:
        return f"Fehler bei der Textextraktion: {e}"

def speichere_text(text, ausgabedatei="youtube_transkript.txt"):
    """
    Speichert den extrahierten Text in eine UTF-8 kodierte Textdatei.
    
    Args:
        text (str): Zu speichernder Text
        ausgabedatei (str): Name/Pfad der Ausgabedatei
        
    Hinweise:
        - Überschreibt existierende Dateien
        - Verwendet UTF-8 Kodierung für Umlaute/Sonderzeichen
        - Erstellt Verzeichnisse falls notwendig
    """
    try:
        # Erstelle Verzeichnis falls es nicht existiert
        ausgabe_verzeichnis = os.path.dirname(ausgabedatei)
        if ausgabe_verzeichnis and not os.path.exists(ausgabe_verzeichnis):
            os.makedirs(ausgabe_verzeichnis)
            
        # Schreibe Text in Datei
        with open(ausgabedatei, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"✓ Text wurde in {ausgabedatei} gespeichert")
        
    except Exception as e:
        print(f"Fehler beim Speichern: {e}")

if __name__ == "__main__":
    try:
        # YouTube-URL des Videos
        url = "http://youtu.be/GRKYOWYs1gM"
        
        print("\nYouTube Text Extraktor")
        print("-" * 50)
        
        print("\nStarte Textextraktion...")
        text = extrahiere_text_aus_video(url)
        
        if text and not text.startswith("Fehler"):
            print("\nExtrahierter Text:")
            print("-" * 50)
            print(text)
            print("-" * 50)
            
            # Speichere den Text in eine Datei
            speichere_text(text)
        else:
            print("\nFehler:")
            print("-" * 50)
            print(text)
            
    except KeyboardInterrupt:
        print("\n\nProgramm wurde durch Benutzer abgebrochen.")
    except Exception as e:
        print(f"\nUnerwarteter Fehler: {e}")