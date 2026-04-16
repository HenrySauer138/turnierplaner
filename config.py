# Konfiguration für Turnierplaner
# WARNUNG: Diese Datei enthält sensible Daten!
# Nicht in Git committen - siehe .gitignore

# E-Mail Einstellungen (Your-Server Webmail)
EMAIL_CONFIG = {
    'imap_server': 'imap.your-server.de',
    'smtp_server': 'smtp.your-server.de',
    'email_address': 'turniere@germania-ober-roden.de',
    'password': 'afF41qhCxK3VWqxE',
    'inbox': 'INBOX',
    'port': 993,  # IMAP SSL
}

# Datenbank
DATABASE_PATH = 'turnierplaner.db'

# Turniereinstellungen
TOURNAMENT_CONFIG = {
    'age_groups': ['U11', 'U12', 'U13', 'U14', 'U15', 'U16', 'U17', 'U18', 'U19'],
    'default_location': 'Ober-Roden',
    'club_name': '1. FC Germania 08 Ober-Roden',
}

# Logging
LOG_LEVEL = 'INFO'
LOG_FILE = 'turnierplaner.log'

# GUI Einstellungen
GUI_CONFIG = {
    'window_width': 1200,
    'window_height': 800,
    'theme': 'light',
}
