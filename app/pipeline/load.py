"""
Functions for loading data from a source.
"""

import pandas as pd
import logging
import os

def load_data(data_path: str) -> pd.DataFrame:
    """
    Loads a dataset from a CSV file.

    This function reads a CSV file and returns a DataFrame.

    Parameters:
    data_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The dataset as a DataFrame.
    """

    logging.basicConfig(filename='loading.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()

    RAW_PATH = r"C:\poke-api-etl\data\raw"
    TRUSTED_PATH = r"C:\poke-api-etl\data\trusted"

    if not os.path.exists(TRUSTED_PATH):
        os.makedirs(TRUSTED_PATH)

    json_file_path = os.path.join(RAW_PATH, data_path)
    csv_file_path = os.path.join(TRUSTED_PATH, os.path.splitext(data_path)[0] + ".csv")

    data = pd.read_json(json_file_path)
    data.to_csv(csv_file_path, index=False)

    logger.info("File loaded and saved as CSV in: %s", csv_file_path)

    return data

if __name__ == "__main__":
    load_data("pokemon_file.json")
