"""
emissions.py
------------

Author: Ezau Faridh Torres Torres.
Date: April, 2026.
"""
# Necessary imports.
import json
import pandas as pd
from pathlib import Path
from codecarbon import EmissionsTracker

class EmissionsRunner:
    
    DEFAULT_RELEVANT = [
        "duration",
        "emissions",
        "cpu_energy",
        "gpu_energy",
        "ram_energy",
        "energy_consumed",
        "cpu_count",
        "gpu_count",
        "cpu_model",
        "gpu_model",
        "ram_total_size",
        "country_iso_code",
    ]

    def __init__(
        self,
        project_name: str = "codecarbon",
        output_dir: str = ".",
        emissions_file: str = "emissions_example.csv",
    ) -> None:
        
        self.project_name = project_name
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.emissions_path = self.output_dir / emissions_file
        print("\n[INFO]: Emissions tracking started.")
        self.tracker = EmissionsTracker(
            project_name=self.project_name,
            save_to_file=True,
            log_level="info", #"DEBUG",
            tracking_mode="process",
            output_dir=str(self.output_dir),
            output_file=str(emissions_file),
            allow_multiple_runs=True,
        )

    def start(self) -> None:
        """
        Start the emissions tracking.
        """
        self.tracker.start()

    def stop(self) -> None:
        """
        Stop the emissions tracking and save the results.
        """
        self.tracker.stop()
        print("\n[INFO]: Emissions tracking completed.")
        print(f"[INFO]: Emissions tracking saved in {self.emissions_path}.")
        
    def get_last_measurements(self) -> None:
        """
        Extract and display the last measurements from the emissions tracking.
        """
        # Extract the last measurements from the emissions CSV file.
        df = pd.read_csv(self.emissions_path)
        measurements = df.iloc[-1][self.DEFAULT_RELEVANT].to_dict()

        # Save measurements to a JSON file.
        with open(self.output_dir / "last_emissions.json", "w") as f:
            json.dump(measurements, f, indent=4)
        with open(self.output_dir / "last_emissions.txt", "w") as f:
            f.write(str(measurements))

        # Print the measurements.
        print("\n[INFO]: Emissions measurements:")
        max_len = max(len(k) for k in measurements)
        for key, value in measurements.items():
            print(f"    - {key:<{max_len}} : {value}")