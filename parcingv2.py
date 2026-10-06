import requests
from bs4 import BeautifulSoup
def parse_dou_vacancies(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://jobs.dou.ua/vacancies/?category=QA'
    }

# Параметры запроса (категория и смещение)
    data = {'category': 'QA','count': 0}

response = requests.post(url, headers=headers, data=data)

if response.status_code == 200:
     # API возвращает JSON с ключом 'html'
    json_data = response.json()
    html_content = json_data.get('html', '')
    
    soup = BeautifulSoup(html_content, 'lxml')
    vacancies = soup.find_all('a', class_='vt')
    
    for vacancy in vacancies:
        print(vacancy.get_text(strip=True))
else:
    print(f"Ошибка: статус {response.status_code}")
parse_dou_vacancies(url="https://jobs.dou.ua/vacancies/?category=QA")