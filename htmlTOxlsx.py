import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import time

## 전국 동물 병원 자료를 웹 페이지에서 읽어서 엑셀 파일로 저장하는 기능
## 따로 데이터 파일을 제공해 주지 않아 크롤링을 이용하여 데이터를 저장함.
## 데이터가 도로명 주소를 제공해 주지는 않아 GPS 좌표 변환시 정확도가 떨어져 사용하지 않음.

# 웹사이트에 요청을 보내고 HTML을 파싱하는 함수
def get_page_data(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    informations = soup.find_all('td')

    data = []
    for i in range(0, len(informations), 5):
        data.append([item.text for item in informations[i:i+5]])

    return data

# 전체 페이지에 대한 데이터를 추출
def htmlToxlsx():
    all_data = []
    total_pages = 529

    # 테스트시에는 range 를 적게 설정.
    # for page in tqdm(range(1, 11)):

    for page in tqdm(range(1, total_pages + 1)):
        page_url = f'https://www.animal.go.kr/front/awtis/shop/hospitalList.do?totalCount=5289&pageSize=10&menuNo=6000000002&&page={page}'
        page_data = get_page_data(page_url)
        all_data.extend(page_data)

        time.sleep(0.01)

    # 데이터를 데이터프레임으로 변환하고 엑셀 파일로 저장
    df = pd.DataFrame(all_data, columns=['index', 'hospital_name', 'telephone', 'address', 'registration_number'])
    df.to_excel('vets_list.xlsx', index=False)
