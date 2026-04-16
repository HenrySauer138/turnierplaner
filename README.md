# 🏆 Turnierplaner

Desktop-Anwendung zur Automatisierung der Turnierplanung für Fußball.

## 📋 Problem gelöst

Automatisiert den manuellen Workflow:
- ✅ E-Mails von Anmeldungsformular auslesen
- ✅ Nach Jahrgang automatisch sortieren
- ✅ GUI zum Verwalten (Zusagen/Absagen)
- ✅ Excel-Export
- ✅ Automatische Turnierplan-Generierung

## 🚀 Installation

```bash
git clone https://github.com/HenrySauerBuP/turnierplaner.git
cd turnierplaner
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## ⚙️ Konfiguration

1. Kopiere `config.py.example` zu `config.py`
2. Trage deine E-Mail-Daten ein:
   - Email: turniere@germania-ober-roden.de
   - IMAP Server: imap.your-server.de
   - App-Passwort: (siehe config.py)

## 🎮 Verwendung

```bash
source venv/bin/activate
python3 src/main.py
```

Dann öffnet sich die GUI zum:
1. E-Mails abrufen
2. Anmeldungen überprüfen
3. Zusagen/Absagen markieren
4. Turnierplan generieren
5. Excel exportieren

## 📁 Projektstruktur

turnierplaner/
├── src/
│   ├── main.py              # GUI Einstiegspunkt
│   ├── core/
│   │   ├── email_parser.py  # Mail auslesen
│   │   └── registration.py  # Datenmodelle
│   ├── gui/
│   │   └── app.py           # PyQt6 GUI
│   └── data/
│       └── database.py      # SQLite
├── config.py                # Konfiguration (nicht in Git!)
├── requirements.txt
└── README.md
## 🛠️ Technologie

- **Python 3.11+**
- **PyQt6** - GUI
- **SQLite** - Datenbank
- **openpyxl** - Excel
- **imaplib** - E-Mail (IMAP)

## 👤 Author

Henry Sauer - 1. FC Germania 08 Ober-Roden

## 📄 Lizenz

MIT License
