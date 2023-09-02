import requests
from Workshop.Workshop8.request_authorization import create_auth_header

BASE_URL = "https://api.spotify.com/v1"

#API calls care vor fi testate
def get_album(album_id):
    api_url = f'{BASE_URL}/albums/{album_id}'
    response = requests.get(api_url, headers=create_auth_header())
    return response

def get_album_tacks(album_id):
    api_url = f'{BASE_URL}/albums/{album_id}/tracks'
    response = requests.get(api_url, headers=create_auth_header())
    return response