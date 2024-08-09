# Webbasierte Quiz-Anwendung

Diese Anwendung ist eine einfache, webbasierte Quiz-App, die mit Python und Flask entwickelt wurde. Die Fragen werden aus einer CSV-Datei geladen, zufällig ausgewählt und dem Benutzer in einem Browser präsentiert. Am Ende wird die Punktzahl berechnet und angezeigt, ob die Prüfung bestanden wurde.

## Voraussetzungen

- Python 3.x
- Flask (Python-Web-Framework)

## Installation

1. **Projekt herunterladen**:
   - Lade die Projektdateien in ein Verzeichnis auf deinem Computer herunter.

2. **Flask installieren**:
   - Installiere Flask, indem du folgenden Befehl in deinem Terminal ausführst:

   ```bash
   pip install Flask

Führe das folgende Python-Skript aus, um den Flask-Server zu starten:
   ```bash
   python app.py

Öffne einen Webbrowser und gehe zu http://127.0.0.1:5000, um das Quiz zu starten.

Projektstruktur
Das Projekt hat die folgende Struktur:

quiz-app/
│
├── app.py                 # Flask-Server und Hauptanwendung
├── questions.csv          # CSV-Datei mit den Fragen
├── static/
│   └── styles.css         # CSS-Dateien für die Gestaltung
└── templates/
    ├── index.html         # Startseite des Quiz
    └── quiz.html          # Quiz-Seite mit den Fragen
    └── result.html        # Seite für das Ergebnis

Nutzung
Startseite:

Die Anwendung startet mit einer Startseite, auf der du das Quiz beginnen kannst.
Fragen beantworten:

Jede Frage wird auf einer neuen Seite angezeigt, und du kannst eine Antwort auswählen.
Ergebnis anzeigen:

Nach Beantwortung aller Fragen zeigt die Anwendung deine Punktzahl und ob du bestanden hast.
Bewertung
Eine Übung besteht aus 40 Fragen.
Jede richtige Antwort ergibt 1 Punkt.
Bei mindestens 60% richtigen Antworten gilt die Prüfung als bestanden.
Anpassungen
Du kannst die Fragen und Antworten einfach durch Bearbeiten der questions.csv-Datei anpassen. Das Design der Anwendung kann in der styles.css-Datei geändert werden.

Lizenz
Dieses Projekt steht unter keiner speziellen Lizenz. Du kannst den Code frei verwenden, ändern und weitergeben.
   
