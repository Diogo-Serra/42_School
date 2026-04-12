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
    crew: list[CrewMember] = Field(ge=1, le=12)
    mission_status: str = Field(default='planned')
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission(self):
        if self.mission_id.startswith('M') is False:
            raise ValueError('Mission ID must start with "M"')
        comm: int = 0
        capt: int = 0
        for crew in self.crew:
            for rank in self.crew.rank:
                if rank.name.name('captain') is True:
                    capt += 1
                if rank.name.name('commander') is True:
                    comm += 1
        if capt < 1 or comm < 1:
            raise ValueError('Must have at least one Commander or Captain')
        return self


def main():
    from crew import sarah_connor, john_smith, alice_johnson
    crew1 = [sarah_connor, john_smith, alice_johnson]

    mission1 = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2024, 4, 1),
        duration_days="900",
        crew=[[sarah_connor, john_smith, alice_johnson]],
        mission_status="",
        budget_millions="2500.0"
    )
    print(mission1)


if __name__ == "__main__":
    main()


"""
Mission ID must start with "M"
Must have at least one Commander or Captain
Long missions (> 365 days) need 50% experienced crew (5+ years)
All crew members must be active
"""
