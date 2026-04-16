cd ~/turnierplaner

cat > README.md << 'EOF'
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
2. Trage deine E-Mail-Daten ein (siehe config.py)

## 🎮 Verwendung

```bash
source venv/bin/activate
python3 src/main.py
```

## 📁 Projektstruktur
turnierplaner/
├── src/
│   ├── main.py
│   ├── core/
│   │   ├── email_parser.py
│   │   └── registration.py
│   ├── gui/
│   │   └── app.py
│   └── data/
│       └── database.py
├── config.py
├── requirements.txt
└── README.md
## 🛠️ Technologie

- Python 3.11+
- PyQt6
- SQLite
- openpyxl
- imaplib

## 👤 Author

Henry Sauer - 1. FC Germania 08 Ober-Roden
EOF