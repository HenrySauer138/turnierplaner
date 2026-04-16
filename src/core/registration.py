"""
Datenmodelle für Turnieranmeldungen
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from enum import Enum


class RegistrationStatus(Enum):
    """Status einer Anmeldung"""
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    WAITLIST = "waitlist"


@dataclass
class Registration:
    """Einzelne Turnieranmeldung"""
    
    id: Optional[int] = None
    email_message_id: Optional[str] = None
    trainer_name: str = ""
    email: str = ""
    phone: str = ""
    verein: str = ""
    team: str = ""
    jahrgang: str = ""
    status: RegistrationStatus = RegistrationStatus.PENDING
    comment: str = ""
    internal_notes: str = ""
    date_received: Optional[datetime] = None
    date_processed: Optional[datetime] = None
    processed_by: Optional[str] = None
    
    def __post_init__(self):
        if isinstance(self.status, str):
            self.status = RegistrationStatus(self.status)
    
    def approve(self, processed_by: str = "admin"):
        self.status = RegistrationStatus.APPROVED
        self.date_processed = datetime.now()
        self.processed_by = processed_by
    
    def reject(self, reason: str = "", processed_by: str = "admin"):
        self.status = RegistrationStatus.REJECTED
        self.internal_notes = reason
        self.date_processed = datetime.now()
        self.processed_by = processed_by
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'trainer_name': self.trainer_name,
            'email': self.email,
            'phone': self.phone,
            'verein': self.verein,
            'team': self.team,
            'jahrgang': self.jahrgang,
            'status': self.status.value,
            'comment': self.comment,
            'date_received': self.date_received.isoformat() if self.date_received else None,
        }
    
    def __str__(self) -> str:
        return f"{self.trainer_name} ({self.jahrgang}) - {self.status.value}"


@dataclass
class AgeGroup:
    """Altersgruppe/Jahrgang"""
    
    name: str
    year_of_birth: int
    registrations: list = None
    
    def __post_init__(self):
        if self.registrations is None:
            self.registrations = []
    
    def add_registration(self, registration: Registration):
        self.registrations.append(registration)
    
    def count_approved(self) -> int:
        return sum(1 for r in self.registrations if r.status == RegistrationStatus.APPROVED)
    
    def count_pending(self) -> int:
        return sum(1 for r in self.registrations if r.status == RegistrationStatus.PENDING)
    
    def __str__(self) -> str:
        return f"{self.name}-{self.year_of_birth} ({len(self.registrations)} Anmeldungen)"
