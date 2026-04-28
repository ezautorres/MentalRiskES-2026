"""
Author: Ezau Faridh Torres Torres.
Date: April, 2026.
"""
# Necessary imports.
import time
from utils.emissions import EmissionsRunner
from utils.config import (
    load_params,
    LoggerFactory,
)
from data.data import DatasetManager
#from data.manager import DatasetManager

# Load parameters.
params = load_params()
base_url = params["BASE_URL"]
token = params["TOKEN"]

def main() -> None:
    
    # Create logger and initialize the emissions tracker.
    logger = LoggerFactory.create_logger()
    tracker = EmissionsRunner()

    # Parameters.
    logger.info(
        "\n=== Parameters ===\n"
        "    BASE_URL : %s\n"
        "    TOKEN    : %s\n",
        base_url,
        token,
    )

    try:
        
        # Dataset.
        logger.info("Downloading dataset.")
        dataset_manager = DatasetManager(base_url, token)
        dataset_manager.download_dataset()
        logger.info("Loading dataset.")
        #a = dataset_manager.load_dataset()
        logger.info("Dataset loaded successfully.")

        # Inference process.
        logger.info("Running model.")
        tracker.start()

        # Last processing.
        logger.info("Processing final information.")

        # Finally
        logger.info("Process completed successfully.")

        # Stop the emissions tracking and get the last measurements.
        tracker.stop()
        tracker.get_last_measurements()
    
    except Exception as e:
        
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":

    start_time = time.time()
    main()
    end_time = time.time()
    print(f"\n[INFO] Total execution time: {end_time - start_time:.2f} seconds.")