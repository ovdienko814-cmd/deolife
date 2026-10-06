import requests
from bs4 import BeautifulSoup
import csv

def parcer(url:str):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    products = soup.find_all('li', class_='l-vacancy')
    for product in products:
        title_element = product.find('a', class_='vt')
        if title_element:
            name = title_element.get_text(strip=True)
            print(name)





def create_csv():
    pass




def write_csv():
    pass



if __name__ == '__main__':
    url = "https://jobs.dou.ua/vacancies/?category=QA"
    parcer(url)