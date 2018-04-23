import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Gossiping/index.html"

payload = {
	'from':'/bbs/Gossiping/index.html',
	'yes':'yes'
}

rs = requests.session()
url_post = "https://www.ptt.cc/ask/over18"
res = rs.post(url_post , verify=False , data=payload)
res = rs.get(url , verify=False)
# print(res.text)

soup = BeautifulSoup(res.text)
print soup
# for entry in soup.select('.r-ent'):
# 	print entry.select('.date')[0].text , entry.select('.author')[0].text , entry.select('.title')[0].text

