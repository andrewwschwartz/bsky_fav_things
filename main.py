import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random

# Spotify API credentials
SPOTIPY_CLIENT_ID = 'YOUR_CLIENT_ID'
SPOTIPY_CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
SPOTIPY_REDIRECT_URI = 'YOUR_REDIRECT_URI'

# Create a Spotify client with OAuth authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope='user-library-read'))

# Get user's liked songs playlist
def get_liked_songs():
    playlists = sp.current_user_playlists()
    for playlist in playlists['items']:
        if playlist['name'] == 'Liked Songs':
            return playlist['id']
    return None

# Get a random song from the liked songs playlist
def get_random_song(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    random_track = random.choice(results['items'])
    return random_track['track']['name'], random_track['track']['artists'][0]['name']

if __name__ == '__main__':
    liked_songs_playlist_id = get_liked_songs()
    
    if liked_songs_playlist_id:
        random_song = get_random_song(liked_songs_playlist_id)
        print(f"Random Song: {random_song[0]} by {random_song[1]}")
    else:
        print("Liked Songs playlist not found.")