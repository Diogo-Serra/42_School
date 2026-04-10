#!/usr/bin/env python3
from pydantic import BaseModel, field_validator, model_validator


class SpaceStation(BaseModel):
    station_id: str
    name: str
    crew_size: int

    @field_validator('station_id')
    def validator_station_id(cls, id_value: str) -> str:
        id_value_len = len(id_value)
        if id_value_len < 3 or id_value_len > 10:
            return ("Too many characters. Make it shorter")
        else:
            return id_value

    @field_validator('name')
    def validator_name(cls, name_value: str):
        name_value_len = len(name_value)
        if name_value_len < 1 or name_value_len > 50:
            return ("Too many characters. Make it shorter")
        else:
            return name_value

    @field_validator('crew_size')
    def validator_crew_size(cls, crew_size_value: int):
        try:
            int(crew_size_value)
            if crew_size_value < 1:
                return ("Need a bigger crew")
            elif crew_size_value > 20:
                return ("Need to decrease the crew")
            else:
                return crew_size_value
        except ValueError as e:
            return f"Error: {e}"

    def __str__(cls):
        return f"{cls.station_id}: Name: {cls.name}, Size: {cls.crew_size}"


netz = SpaceStation(station_id="Home", name="testship", crew_size=42)
print(netz)
