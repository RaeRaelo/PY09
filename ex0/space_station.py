from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=0, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("====================================")
    try:
        valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=(datetime.fromisoformat
                              ("2024-05-12T10:00:00+00:00")),
            is_operational=True
        )
        print("Valid station created:")
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        status = ('Operational' if valid_station.is_operational
                  else 'Offline')
        print(f"Status: {status}")
    except ValidationError as e:
        print(f"Unexpected validation error: {e}")
    print("====================================")
    try:
        invalid_station = SpaceStation(
            station_id="ALPHA02",
            name="Alpha Station",
            crew_size=25,
            power_level=50.0,
            oxygen_level=40.0,
            last_maintenance=datetime.fromisoformat("2024-05-12T10:00:00")
        )
        print(invalid_station)
    except ValidationError as e:
        print("\nExpected validation error:")
        for error in e.errors():
            print(f"- {error['loc'][0]}: {error['msg']}")


if __name__ == "__main__":
    main()
