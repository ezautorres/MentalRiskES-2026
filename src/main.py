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
from dataset.data import get_dataset

# Load parameters.
params = load_params()
caguama = params["caguama"]

def main() -> None:
    
    # Create logger and initialize the emissions tracker.
    logger = LoggerFactory.create_logger()
    tracker = EmissionsRunner()

    # Parameters.
    logger.info(
        "\n=== Parameters ===\n"
        "    Table out : %s\n"
        "    Table out : %s\n"
        "    Table out : %s\n"
        "    Table out : %s\n",
        caguama,
        caguama,
        caguama,
        caguama,
    )

    try:
        
        # Dataset.
        logger.info("Loading dataset.")
        a = get_dataset()
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