"""
Author: Ezau Faridh Torres Torres.
Date: April 5, 2026.
"""
# Necessary imports and seeds.
from utils.emissions import EmissionsRunner

if __name__ == "__main__":

    # Initialize the emissions tracker.
    runner = EmissionsRunner(
        project_name="Test1",
        output_dir="../logs/emissions",
        emissions_file="emissions.csv"
    )
    runner.start()

    # -------------------------------------------------------------------------
    def addition(a: float, b: float) -> None:
        print(f"The addition of {a} and {b} is: {a + b}")
    addition(5.0, 3.0)
    # -------------------------------------------------------------------------

    # Stop the emissions tracking and get the last measurements.
    runner.stop()
    runner.get_last_measurements()