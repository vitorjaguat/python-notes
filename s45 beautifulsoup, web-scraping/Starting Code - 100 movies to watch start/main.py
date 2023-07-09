import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')
movie_tags = soup.select('.article-title-description__text .title')
movie_titles = [tag.text + '\n' for tag in movie_tags][::-1]
# print(movie_titles)

with open('100_best_movies.txt', 'a') as file:
    file.writelines(movie_titles)