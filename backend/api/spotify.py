# Funktions for seraching and request music from Spotify!
# The Spotify's credencials are saved at .env for security and available as env variable from settings.py
# the function are used at index.py as javascript function searchSpotify()


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
        'limit': 10, # number of music checked at Spotify, but only filter music (below) are going to be add at playlist.
    })
    results = response.json()
    
    # Filtering music with valid urls. 
    # Otherwise, SearchSpotify() at index.html would add some songs on the play list without urls!
    # 
    filtered_tracks = [
        item for item in results['tracks']['items']
        if item['preview_url'] is not None
    ]
    
    # only filtred musics!...only with url!
    results['tracks']['items'] = filtered_tracks
    return results