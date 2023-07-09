from bs4 import BeautifulSoup
import requests
import datetime as dt

user_date = input('Which year, month and day do you want to travel to? Type the date in this format YYYY-MM-DD:\n')

billboard_url = 'https://www.billboard.com/charts/hot-100/' + user_date
response = requests.get(billboard_url)
billboard_website = response.text

soup = BeautifulSoup(billboard_website, 'html.parser')
song_tags = soup.select('.o-chart-results-list__item h3#title-of-a-story.c-title')
song_titles = [tag.text.replace('\n', '').replace('\t', '') for tag in song_tags]
print(song_titles)


# Spotify API
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

SPOTIFY_ID = os.environ.get('SPOTIFY_ID')
SPOTIFY_SECRET = os.environ.get('SPOTIFY_SECRET')
SPOTIPY_REDIRECT_URI='http://example.com'
OAUTH_AUTHORIZE_URL= 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL= 'https://accounts.spotify.com/api/token'
scope = 'playlist-modify-private'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username='jaguat', 
    )
)

song_names = song_titles[:10]
user_id = sp.current_user()["id"]
print(user_id)

song_uris = []
year = user_date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
