#!/usr/bin/env python3
from pydantic import BaseModel, model_validator, Field
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    radio = 0
    visual = 1
    physical = 2
    telepathic = 3


@model_validator
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
