"""
Turnierplaner - Hauptprogramm
"""

import sys
from pathlib import Path

# Füge src-Verzeichnis zum Path hinzu
sys.path.insert(0, str(Path(__file__).parent))

from core.email_parser import EmailParser
from data.database import TournamentDatabase
from config import EMAIL_CONFIG, DATABASE_PATH


def main():
    """Hauptfunktion"""
    print("=" * 60)
    print("🏆 TURNIERPLANER - Systemstart")
    print("=" * 60)
    
    # Datenbank initialisieren
    db = TournamentDatabase(DATABASE_PATH)
    db.init_database()
    print("✓ Datenbank initialisiert")
    
    # Email Parser initialisieren
    parser = EmailParser(
        imap_server=EMAIL_CONFIG['imap_server'],
        email_address=EMAIL_CONFIG['email_address'],
        password=EMAIL_CONFIG['password']
    )
    print("✓ Email Parser initialisiert")
    print("\nWarte auf Node.js Installation... oder starten Sie manuell:")
    print("  claude 'generate email_parser'")


if __name__ == '__main__':
    main()
