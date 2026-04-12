#!/usr/bin/env python3
from pydantic import BaseModel, Field, model_validator, ValidationError # noqa
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

    def __str__(self):
        return f"{self.name} ({self.rank.name}) - {self.specialization}"


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
        exp_member: int = 0
        for member in self.crew:
            if member.years_experience > 5:
                exp_member += 1
        if exp_member < 1:
            raise ValueError("Long missions (> 365 days) need 50%\\ "
                             "experienced crew (5+ years)")
        active_members = 0
        for member in self.crew:
            if member.is_active is True:
                active_members += 1
        if active_members != len(self.crew):
            raise ValueError("All crew members must be active")
        return self

    def __str__(self):
        return (f"Mission: {self.mission_name}\n"
                f"ID: {self.mission_id}\n"
                f"Destination: {self.destination}\n"
                f"Duration: {self.duration_days}\n"
                f"Budget: {self.budget_millions}\n"
                f"Crew size: {len(self.crew)}\n")


def main():

    sarah_connor = CrewMember(
        member_id="sarah1",
        name="Sarah Connor",
        rank=Rank.commander,
        age="35",
        specialization="Mission Command",
        years_experience="15",
        is_active=True,
    )

    john_smith = CrewMember(
        member_id="john2",
        name="John Smith",
        rank=Rank.lieutenant,
        age="28",
        specialization="Navigation",
        years_experience="10",
        is_active=True,
    )

    alice_johnson = CrewMember(
        member_id="alice3",
        name="Alice Johnson",
        rank=Rank.officer,
        age="24",
        specialization="Engineering",
        years_experience="5",
        is_active=True,
    )

    print("Space Mission Crew Validation")
    print("=========================================")

    mission1 = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2024, 5, 1, 2, 42, 42),
        duration_days="900",
        crew=[sarah_connor, john_smith, alice_johnson],
        mission_status="",
        budget_millions="2500.0"
    )

    print(mission1, end="")
    print("Crew members:")
    for member in mission1.crew:
        print(f" - {member}")

    print("\n=========================================")
    print("Expected validation error:")
    try:
        mission2 = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 5, 1, 2, 42, 42),
            duration_days="900",
            crew=[sarah_connor, john_smith, alice_johnson],
            mission_status="",
            budget_millions="2500.0")
        print(mission2, end="")
        print("Crew members:")
        for member in mission2.crew:
            print(f" - {member}")
    except ValidationError as ve:
        print(ve)


main()
