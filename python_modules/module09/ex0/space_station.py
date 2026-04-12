#!/usr/bin/env python3
from pydantic import BaseModel, field_validator, Field, ValidationError
from datetime import datetime

from generated_data.alien_contacts import ALIEN_CONTACTS as ac


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)

    @field_validator('crew_size', mode='after')
    def validator_crew_size(cls, crew_size_value: int):
        if crew_size_value < 1:
            raise ValueError("Input should be more than or equal to 1")
        elif crew_size_value > 20:
            raise ValueError("Input should be less than or equal to 20")
        return crew_size_value

    def __str__(self):
        return (f"ID: {self.station_id}\n"
                f"Name: {self.name}\n"
                f"Crew: {self.crew_size} people\n"
                f"Power: {self.power_level}%\n"
                f"Oxygen: {self.oxygen_level}%\n")


def main() -> None:

    print("Space Station Data Validation")
    print("========================================")
    try:
        netz = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2009, 7, 23),
            is_operational="True",
            notes="")
    except ValidationError as e:
        print(e)

    print("Valid station created:")
    print(netz)
    if netz.is_operational is True:
        print("Status: Operational")
    else:
        print("Status: Not operational")

    print("\n========================================")
    print("Expected validation error:")
    try:
        netz1 = SpaceStation( # noqa
            station_id="ISS001",
            name="International Space Station",
            crew_size=42,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2009, 7, 23),
            is_operational="True",
            notes="")
    except ValidationError as e:
        errors_dict: list[dict] = e.errors()
        print(errors_dict[0]["msg"].split(', ')[1])

    print()
    from generated_data.i import i as ss
    stations = [SpaceStation(**data) for data in ss]
    try:
        for station in stations:
            print(station)
    except ValidationError as ve:
        print(ve)


if __name__ == "__main__":
    main()
