import requests
from bs4 import BeautifulSoup
print("aaaaaa")
req = requests.get(
	'http://movie.daum.net/moviedb/main?movieId=93697')
html = req.text
soup=BeautifulSoup(html, 'html.parser')
story = soup.select(
	'div.desc_movie')

print(story[0].text)