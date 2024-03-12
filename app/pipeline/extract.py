"""
Function to extract data from the API and save in a json file.
"""

import requests
import logging
import json

def extract_from_api(url: str) -> json:
    """
    Extracts data from the given API URL, retrieves information about Pokemon, and saves the data into JSON files.

    Parameters:
    url (str): The base URL of the API to extract data from.

    Returns:
    json: The extracted data in JSON format.

    Example:
    extract_from_api("https://pokeapi.co/api/v2/pokemon/")
    """

    logging.basicConfig(filename='extract.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()

    url = "https://pokeapi.co/api/v2/pokemon/"

    pokemon_list = list()

    counter = 1

    while url != None:
        payload={}
        headers = {}
        response = json.loads(requests.request("GET", url, headers=headers, data=payload).text)
        url = response["next"]

        for item in response["results"]:
            pokemon_name = item["name"]
            url_pokemon = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
            response_pokemon = json.loads(requests.request("GET", url_pokemon, headers=headers, data=payload).text)

            infos = {
                "name": pokemon_name,
                "id": response_pokemon["id"],
                "height": response_pokemon["height"],
                "weight": response_pokemon["weight"],
                "is_default": response_pokemon["is_default"]
            }

            pokemon_list.append(infos)
            logger.info(response_pokemon["id"])

        file_path = fr"C:\poke-api-etl\data\transient\pokemon_file_{counter}.json"

        with open(file_path, 'w') as outfile:
            logger.info("Saving file in: %s", file_path)
            json.dump(pokemon_list, outfile)

        outfile.close()
        counter = counter + 1
        pokemon_list = list()

    logger.info(pokemon_list)

if __name__ == '__main__':
    extract_from_api("https://pokeapi.co/api/v2/pokemon/")