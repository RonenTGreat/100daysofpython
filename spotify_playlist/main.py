import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Scraps through billboard charts than creates a list of the titles.
URL = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(url=URL)
playlist_page = response.text
soup = BeautifulSoup(playlist_page, "html.parser")
songs = soup.select("li ul li h3")
song_list = [song.getText().replace("\n", "").replace("\t", "") for song in songs]

# Sets up Spotify Authentication
song_uris = []
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="http://example.com",
    client_id=client_id,
    client_secret=client_secret,
    show_dialog=True,
    cache_path="token.txt"
))

# Searches the songs from the list created then passes it to Spotify then added it to a list
user_id = sp.current_user()["id"]
year = date.split("-")[0]

for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creates Playlist and adds it to your library
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

