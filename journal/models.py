from dataclasses import dataclass
from datetime import date


@dataclass
class Entry:
    """A single day's journal entry across four life areas."""
    entry_date: date
    relationships_note: str
    relationships_rating: int
    learning_note: str
    learning_minutes: int
    money_note: str
    money_spent: float
    health_note: str
    sleep_hours: float
    exercised: bool
