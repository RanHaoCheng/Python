import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/ask/over18?from=%2Fbbs%2Fgossiping%2Findex.html"

res = requests.get(url)
soup = BeautifulSoup(res.text)

for me in soup.select('meta'):
	print me

# for iteraion in soup.select('a'):
	# print iteraion.text
