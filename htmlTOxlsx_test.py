import requests
from bs4 import BeautifulSoup

page_url = f'https://www.animal.go.kr/front/awtis/shop/hospitalList.do?totalCount=5289&pageSize=10&menuNo=6000000002&&page=1'

response = requests.get(page_url)
soup = BeautifulSoup(response.text, 'html.parser')
informations = soup.find_all('td')

data = []

print(len(informations))

for i in range(0, len(informations), 5):
    data.append([item.text for item in informations[i:i+5]])

print(data)