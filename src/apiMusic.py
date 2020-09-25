import requests
import json
import os
from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only

env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)


def get_content(list_data):
    for data in list_data:
        response = requests.request("GET", "https://shazam.p.rapidapi.com/search", headers=headers,
                                    params={"locale": "fr-FR", "offset": "0", "limit": "1", "term": data})
        data_json = json.loads(response.text)
        if data_json['tracks']:
            key = data_json['tracks']['hits'][0]['track']['key']
            response = requests.request("GET", "https://shazam.p.rapidapi.com/songs/get-details", headers=headers,
                                        params={"locale": "fr-FR", "key": key})
            song = json.loads(response.text)
            genre = song['genres']['primary']
            year = song['sections'][0]['metadata'][2]['text']
            print(genre + ' ' + year)


if __name__ == "__main__":
    headers = {
        'x-rapidapi-host': os.getenv("RAPIDAPI_HOST"),
        'x-rapidapi-key': os.getenv("RAPIDAPI_KEY")
    }
    get_content(['IAM'])
