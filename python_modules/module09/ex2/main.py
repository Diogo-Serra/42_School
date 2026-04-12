#!/usr/bin/env python3
from space_crew import SpaceMission
from datetime import datetime


def main():
    from crew import sarah_connor, john_smith, alice_johnson

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
    print(f"{mission1.launch_date}")


main()
