#!/usr/bin/env python3
from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from enum import Enum


class Rank(Enum):
    cadet = 0
    officer = 1
    lieutenant = 2
    captain = 3
    commander = 4


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default='planned')
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission(self):
        if self.mission_id.startswith('M') is False:
            raise ValueError('Mission ID must start with "M"')
        comm: int = 0
        capt: int = 0
        for member in self.crew:
            if member.rank.name == "captain":
                capt += 1
            if member.rank.name == "commander":
                comm += 1
        if capt < 1 and comm < 1:
            raise ValueError('Must have at least one Commander or Captain')
        return self


"""
Mission ID must start with "M"
Must have at least one Commander or Captain
Long missions (> 365 days) need 50% experienced crew (5+ years)
All crew members must be active
"""
