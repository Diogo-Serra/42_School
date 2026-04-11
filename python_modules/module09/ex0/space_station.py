#!/usr/bin/env python3
from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime


@model_validator
class SpaceStation(BaseModel):
    station_id: str
    name: str
    crew_size: int
    power_level: float
    oxygen_level: float
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None

    @field_validator('station_id')
    def validator_station_id(self, id_value: str) -> str:
        id_value_len = len(id_value)
        if id_value_len < 3 or id_value_len > 10:
            return ("Too many characters. Make it shorter")
        else:
            return id_value

    @field_validator('name')
    def validator_name(self, name_value: str):
        name_value_len = len(name_value)
        if name_value_len < 1 or name_value_len > 50:
            return ("Input shouldn't be less than 1 nor bigger than 50")
        else:
            return name_value

    @field_validator('crew_size')
    def validator_crew_size(self, crew_size_value: int):
        try:
            int(crew_size_value)
            if crew_size_value < 1 or crew_size_value > 20:
                return ("Input shouldn't be less than 1 nor bigger than 20")
            else:
                return crew_size_value
        except ValueError as e:
            return f"Error: {e}"

    @field_validator('power_level', 'oxygen_level')
    def power_oxygen_validator(self, power_level_value):
        try:
            float(power_level_value)
            if power_level_value < 0.0 or power_level_value > 100.0:
                return "Not valid power level"
        except ValueError as e:
            return e

    @field_validator('notes')
    def notes_validator(self, notes):
        if len(notes) > 200:
            return "Notes need to be smaller"

    @model_validator(mode='after')
    def model_validator(self):
        pass

    def __str__(self):
        return f"{self.station_id}: Name: {self.name}, Size: {self.crew_size}"


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")

    netz = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=42,
        power_level=85.5,
        oxygen_level=92.3,
        is_operational="Operational")

    print("Valid station created:")
    print(f"ID: {netz.station_id}")
    print(f"Name: {netz.name}")
    print(f"Crew: {netz.crew_size}")
    print(f"Power: {netz.power_level}%")
    print(f"Oxygen: {netz.oxygen_level}%")
    print(f"Status: {netz.notes}")

    print("========================================")
    print("Expected validation error:")
    print("")
    print(netz)


if __name__ == "__main__":
    main()
