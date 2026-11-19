# Animal Info Fetcher 🐾

Dieses Projekt ist ein kleines Python-Programm, das Tierinformationen über die [API Ninjas Animals API](https://api-ninjas.com/api/animals) abruft und in einer formatierten **HTML-Seite** darstellt.  

Wenn ein eingegebener Tiername gefunden wird, zeigt die HTML-Ausgabe eine schöne Karte mit Details wie **Name, Diet, Location, Type**.  
Falls kein Tier mit diesem Namen existiert, wird stattdessen eine Fehlermeldung in der HTML-Datei angezeigt:  


<h2>The animal {animal_name} doesn't exist.</h2>


.
├── .gitignore           # Git
├── README.md            # Programm Info
├── animals_web_generator.py # Einstiegspunkt des Programms, baut die HTML-Ausgabe
├── data_fetcher.py      # Holt Tierdaten über die API Ninjas Animals API
├── animals_template.html # HTML-Template mit Platzhalter __REPLACE_ANIMALS_INFO__
├── animals.html         # Generierte Ausgabedatei
├── requirements.txt     # Python-Abhängigkeiten
└── .env                 # Datei für den API-Key (API_KEY=...)


# Voraussetzungen

Python 3.8+

Einen kostenlosen API-Key von API Ninjas


## Installation

Installation

Repository klonen:

git clone https://github.com/DEIN_USERNAME/DEIN_REPO.git
cd DEIN_REPO


Virtuelle Umgebung erstellen (optional, aber empfohlen):

python -m venv venv
source venv/bin/activate   # auf Linux/macOS
venv\Scripts\activate      # auf Windows


Abhängigkeiten installieren:

pip install -r requirements.txt


Erstelle eine .env-Datei im Projektverzeichnis mit deinem API-Key:

API_KEY=dein_api_key_von_api_ninjas

## Usage

Nutzung

Starte das Programm mit:

python main.py


Du wirst nach einem Tiernamen gefragt (z. B. dog, cat, unicorn).

Das Programm erzeugt eine animals.html-Datei mit den Ergebnissen.

Öffne animals.html im Browser, um die Ausgabe anzusehen.

## Contributing

Contributing

Beiträge sind willkommen!
Wenn du neue Features vorschlagen oder Bugs fixen möchtest:

Forke das Repository

Erstelle einen Feature-Branch (git checkout -b feature/neues-feature)

Committe deine Änderungen (git commit -m "Add neues-feature")

Push und Pull Request erstellen

Übungsprojekt AI Studium 2025: Tierinfos über API Ninjas als HTML-Seite ausgeben (Python, requests, dotenv)

```html
