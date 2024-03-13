"""
This code is used to test the API.
"""

import unittest
import requests

class TestAPI(unittest.TestCase):
    def test_api(self):
        url = "https://pokeapi.co/api/v2/pokemon/"
        response = requests.get(url)
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["count"] > 0)
        self.assertTrue(data["results"] != None)
        self.assertTrue(data["next"] != None)
        self.assertTrue(data["previous"] == None)
        self.assertTrue(data["results"][0]["name"] != None)
        self.assertTrue(data["results"][0]["url"] != None)

if __name__ == '__main__':
    unittest.main()