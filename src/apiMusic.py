import requests
import json


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
        'x-rapidapi-host': "shazam.p.rapidapi.com",
        'x-rapidapi-key': "f60c19b24cmsh994842bff7b8d81p1ed4b9jsn1842f67fb6ee"
    }
    get_content(['IAM'])
