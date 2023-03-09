from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

url = "https://quotes.toscrape.com/"
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
# Tag, NavigableString, BeautifulSoup, Comment
# Here is BeautifulSoup
Result = []
message_all = soup.find_all("div", class_="quote")
for message in message_all:
    quote = {}
    quote_text = message.find("span", class_="text").text.strip()
    author = message.find("small", class_="author").text.strip()
    tags = message.find_all("a", class_="tag")
    
    quote['author'] = author
    quote['quote_text'] = quote_text
    tag_all = []  
    for tag in tags:
        tag_all.append(tag.text.strip())
    quote['tags'] = tag_all
    Result.append(quote)
# write result in txt file
with open("quote_text.json", 'w+') as quote_text:
    quote_text.write(str(Result))
    quote_text.close()
    
# import pandas as pd
# df = pd.read_json('quote_text.json')
# print(df.to_string())