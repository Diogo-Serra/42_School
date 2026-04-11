#!/usr/bin/env python3
from pydantic import BaseModel, model_validator, Field, ValidationError
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    radio = 0
    visual = 1
    physical = 2
    telepathic = 3


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def alien_contact_validator(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Needs to start with AC")
        if self.contact_type.name == "physical" and self.is_verified is False:
            raise ValueError("Physical contact type requires verification")
        if self.contact_type.name == "telepathic" and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 "
                             "witnesses")
        if self.signal_strength > 7 and self.message_received is None:
            raise ValueError("Strong signals (> 7.0) should include "
                             "received messages")
        return self


def main():
    print("Alien Contact Log Validation")
    print("======================================")
    alien_contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(2024, 1, 1),
        location="Area 51, Nevada",
        contact_type=0,
        signal_strength=8.5,
        duration_minutes=42,
        witness_count=5,
        message_received='Greetings from Zeta Reticuli',
        is_verified=True,
    )
    print("Valid contact report:")
    print(f"ID: {alien_contact.contact_id}")
    print(f"Type: {alien_contact.contact_type.name}")
    print(f"Location: {alien_contact.location}")
    print(f"Signal: {alien_contact.signal_strength}")
    print(f"Duration: {alien_contact.duration_minutes}")
    print(f"Witnesses: {alien_contact.witness_count}")
    print(f"Message: {alien_contact.message_received}")

    print("\n======================================")
    print("Expected validation error:")

    try:
        alien_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 1, 1),
            location="Area 51, Nevada",
            contact_type=3,
            signal_strength=8.5,
            duration_minutes=42,
            witness_count=2,
            message_received='Greetings from Zeta Reticuli',
            is_verified=True,
        )
    except ValidationError as v:
        validation_error = v.errors()
        print(validation_error[0]['msg'].split(", ")[1])


if __name__ == "__main__":
    main()
