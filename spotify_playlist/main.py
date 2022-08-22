import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{year}"
response = requests.get(url=URL)
playlist_page = response.text
soup = BeautifulSoup(playlist_page, "html.parser")
songs = soup.select("li ul li h3")
song_list = [song.getText().replace("\n", "").replace("\t", "") for song in songs]
