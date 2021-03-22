import requests
import os
from lxml import etree
from io import StringIO


def parse(url):
    resp = requests.get(url, headers={'Content-Type': 'text/html'})
    return resp.text


SITE_URL = "https://www.wildberries.ru"
BOOKS = SITE_URL + "/catalog/knigi/detyam-i-roditelyam"
ENCODING = "utf-8"
html = parse(BOOKS)
htmlparser = etree.HTMLParser()
tree = etree.parse(StringIO(html), htmlparser)
links = tree.xpath('//a[@class="ref_goods_n_p j-open-full-product-card"]/@href')

os.makedirs("data", exist_ok=True)
index = open("data/index.txt", "w+", encoding=ENCODING)
pages = 3

for i, link in enumerate(links):
    link = SITE_URL + link
    html_source = parse(link)
    with open("data/" + str.format("{}.html".format(i)), 'w', encoding=ENCODING) as file:
        file.write(html_source)
    index.write("{} - {}\n".format(i, link))

index.close()
