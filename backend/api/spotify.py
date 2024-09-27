import requests
from django.conf import settings

def get_spotify_token():
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': settings.SPOTIFY_CLIENT_ID,
        'client_secret': settings.SPOTIFY_CLIENT_SECRET,
    })
    auth_response_data = auth_response.json()
    return auth_response_data['access_token']

def search_spotify(query):
    token = get_spotify_token()
    headers = {
        'Authorization': f'Bearer {token}',
    }
    search_url = 'https://api.spotify.com/v1/search'
    response = requests.get(search_url, headers=headers, params={
        'q': query,
        'type': 'track',
        'limit': 10,
    })
    return response.json()