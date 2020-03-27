from bs4 import BeautifulSoup as bs
import requests

url = "https://www.daum.net"
webpage = requests.get(url)
#print(webpage.text)

soup = bs(webpage.content, "html.parser")
print(soup.select(".date_today"))
#print(soup.contents)