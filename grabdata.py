import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from collections import defaultdict

with open('api_key.json', 'r') as f:
    api_keys = json.load(f)

client_id = api_keys['client_id']
client_secret = api_keys['client_secret']
redirect_uri = api_keys['redirect_uri']
scope = api_keys['scope']

def search_track(sp):
    top_artists = sp.current_user_top_artists(limit=20, time_range='medium_term')  # Adjust limit/time_range as needed
    artist_names = [artist['name'] for artist in top_artists['items']]
    print(artist_names)
    return artist_names

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

search_track(sp)