"""
Function to concat the json files in a unic file.
"""

import json
import os
from typing import List

def concat_json_files(file_paths: List[str]) -> json:

    """
    Concatenates multiple JSON files into a single file.

    This function searches for JSON files in a specified directory, reads each file, and appends their content to a list.
    Finally, it writes the combined content into a new JSON file.

    Parameters:
    None

    Returns:
    None

    Example:
    concat_json_files()
    """

    INITIAL_PATH = fr"C:\poke-api-etl\data\transient"
    FINAL_PATH = fr"C:\poke-api-etl\data\raw"

    files = os.listdir(INITIAL_PATH)
    pokemon_list = list()

    for file in files:
        if file.endswith(".json"):
            with open(f"{INITIAL_PATH}/{file}") as json_file:
                data = json.load(json_file)
                pokemon_list.extend(data)

    with open(f"{FINAL_PATH}/pokemon_file.json", 'w') as outfile:
        json.dump(pokemon_list, outfile)

    outfile.close()

    print("File concatenated in: ", f"{FINAL_PATH}/pokemon_file.json")

    # Delete JSON files from the transiente layer
    INITIAL_PATH = fr"C:\poke-api-etl\data\transient"
    transient_files = os.listdir(INITIAL_PATH)

    for file in transient_files:
        if file.endswith(".json"):
            os.remove(os.path.join(INITIAL_PATH, file))
            print("Deleted file:", os.path.join(INITIAL_PATH, file))

if __name__ == "__main__":
    concat_json_files("C:\poke-api-etl\data\raw")