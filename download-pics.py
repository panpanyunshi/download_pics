import os
os.makedirs('./img/', exist_ok=True)

# example :download pics
from bs4 import BeautifulSoup
import requests

URL_org = "http://photo.chinamil.com.cn/bqtk/"
URL = "http://photo.chinamil.com.cn/bqtk/hkht.htm"

html = requests.get(URL).text
# print(html)
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
img_ul = soup.find_all('p', {"class": "image"})

for ul in img_ul:
    url_attachment = ul.next_element['src']
    name = url_attachment.split('/')[-1]
    photo_url = URL_org + url_attachment
    print(photo_url)
    import requests

    r = requests.get(photo_url)
    with open('./img/' + name + 'image2.png', 'wb') as f:
        f.write(r.content)  # whole document
