"""
Main file from pipeline.
"""

from pipeline.extract import extract_from_api
from pipeline.transform import concat_json_files
from pipeline.load import load_data

if __name__ == "__main__":
    extract_from_api("https://pokeapi.co/api/v2/pokemon/")
    concat_json_files("C:\poke-api-etl\data\raw")
    load_data("pokemon_file.json")
    