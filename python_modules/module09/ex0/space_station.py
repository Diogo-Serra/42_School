#!/usr/bin/env python3
from pydantic import BaseModel, field_validator, Field
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int
    power_level: float
    oxygen_level: float
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(max_length=200)

    @field_validator('crew_size')
    def validator_crew_size(cls, crew_size_value: int):
        try:
            int(crew_size_value)
            if crew_size_value < 1:
                print("Input should be more than or equal to 1")
            elif crew_size_value > 20:
                print("Input should be less than or equal to 20")
            return crew_size_value
        except ValueError as e:
            print(e)

    @field_validator('power_level', 'oxygen_level')
    def power_oxygen_validator(cls, power_level_value: float):
        try:
            float(power_level_value)
            if power_level_value < 0.0:
                print("Input should be more than or equal to 0.0")
            elif power_level_value > 100.0:
                print("Input should be less than or equal to 100.0")
            return power_level_value
        except ValueError as e:
            print(e)


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
