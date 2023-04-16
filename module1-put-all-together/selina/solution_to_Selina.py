# find a singer's first album
import sys
from json.decoder import JSONDecodeError

import requests
from requests.exceptions import HTTPError

ITUNES_SEARCH_URL = "https://itunes.apple.com/search"

def command_first_album():
    if len(sys.argv) < 3:
        print("Usage: python3 solution_to_Selina.py first_album <artist_name>")
        return
    artist_name = sys.argv[2]
    print("Artist name: {}".format(artist_name))
    try:
        response = requests.get(ITUNES_SEARCH_URL, params={
            "term": artist_name,
            "entity": "album",
            "limit": 1
        })
        response.raise_for_status()
        response_json = response.json()
        if response_json['resultCount'] == 0:
            print("No album found")
        else:
            print("First album: {}".format(response_json['results'][0]['collectionName']))
    except HTTPError as http_err:
        print("HTTP error occurred: {}".format(http_err))
    except JSONDecodeError as json_err:
        print("JSON decode error occurred: {}".format(json_err))
    except Exception as err:
        print("Other error occurred: {}".format(err))