# -*- coding: utf-8 -*-
# 参考, http://tech.innovation.co.jp/2017/07/28/mecab.html

import re
import bs4
import sys
import MeCab
import urllib.request
from pprint import pprint

url = "http://www.sanspo.com/baseball/news/20180407/mlb18040711000002-n1.html"

soup = bs4.BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")

contents = soup.find(attrs={"name": re.compile(r'Description', re.I)}).attrs['content']
output_words = []

m = MeCab.Tagger()
keywords = m.parse(contents)

for row in keywords.split("\n"):
    word = row.split("\t")[0]
    if word == "EOS":
        break
    else:
        pos = row.split("\t")[1].split(",")[0]
        if pos == "名詞":
            output_words.append(word)

print(output_words)
