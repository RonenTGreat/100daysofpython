import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
movie_page = response.text
soup = BeautifulSoup(movie_page, "html.parser")
movies_list = []
movies = soup.find_all(name='h3', class_='title')
for movie in movies[::-1]:
    text = movie.getText()
    movies_list.append(text)
with open('movies.txt', 'a', encoding="utf8") as file:
    for movie_list in movies_list:
        file.write(movie_list + "\n")



