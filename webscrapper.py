import requests
from bs4 import BeautifulSoup
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

item = input("Enter the item to be searched for ")
item = item.replace(" ","+")
url = "https://www.amazon.in/s?k="+item

source = requests.get(url,headers = headers).text
soup = BeautifulSoup(source,'lxml')

for article in soup.find_all(class_='a-size-medium a-color-base a-text-normal'):
    print(article.text)
    print()