#!/usr/bin/env python3
from pydantic import BaseModel, field_validator
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str
    name: str
    crew_size: int
    power_level: float
    oxygen_level: float
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = None

    @field_validator('station_id')
    def validator_station_id(cls, id_value: str) -> str:
        id_value_len = len(id_value)
        if id_value_len < 3:
            print("Input should be more than or equal to 3")
        elif id_value_len > 10:
            print("Input should be less than or equal to 10")
        return id_value

    @field_validator('name')
    def validator_name(cls, name_value: str):
        name_value_len = len(name_value)
        if name_value_len < 1:
            print("Input should be more than or equal to 1")
        elif name_value_len > 50:
            print("Input should be less than or equal to 50")
        return name_value

    @field_validator('crew_size')
    def validator_crew_size(cls, crew_size_value: int):
        if crew_size_value < 1:
            print("Input should be more than or equal to 1")
        elif crew_size_value > 20:
            print("Input should be less than or equal to 20")
        return crew_size_value

    @field_validator('power_level', 'oxygen_level')
    def power_oxygen_validator(cls, power_level_value):
        if power_level_value < 0.0:
            print("Input should be more than or equal to 0.0")
        elif power_level_value > 100.0:
            print("Input should be less than or equal to 100.0")
        return power_level_value

    @field_validator('notes', mode='before')
    def notes_validator(cls, notes):
        if notes is None:
            return notes
        if len(notes) > 200:
            print("Input should be less than or equal to 200")
        return notes

    def __str__(self):
        return f"{self.station_id}: Name: {self.name}, Size: {self.crew_size}"


def main() -> None:

    print("Space Station Data Validation")
    print("========================================")

    netz = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2009, 7, 23),
        is_operational="True",
        notes="")

    print("Valid station created:")
    print(f"ID: {netz.station_id}")
    print(f"Name: {netz.name}")
    print(f"Crew: {netz.crew_size} people")
    print(f"Power: {netz.power_level}%")
    print(f"Oxygen: {netz.oxygen_level}%")
    if netz.is_operational is True:
        print("Status: Operational")
    else:
        print("Status: Not operational")

    print("\n========================================")
    print("Expected validation error:")
    try:
        netz1 = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=42,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2009, 7, 23),
            is_operational="True",
            notes="")
    except Exception:
        pass


if __name__ == "__main__":
    main()
