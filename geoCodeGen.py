import requests
import pandas as pd
from dotenv import load_dotenv
import os

def get_geocode(address, api_key):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": address, "key": api_key}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        result = response.json()
        if result['status'] == 'OK':
            geometry = result['results'][0]['geometry']['location']
            return geometry['lat'], geometry['lng']
    return None, None

def geoCodeGen():

    # .env 파일에서 key 관리
    load_dotenv()
    api_key = os.environ.get('key') ##################################### API KEY #####################################
    # 엑셀 파일 불러오기
    df = pd.read_excel('Seoul_vet.xlsx')  # 실제 파일 경로로 변경하세요.

    for index, row in df.iterrows():

        #### 테스트시 여기서 횟수 조절
        if index > 10:
            continue
        subAddress = row['도로명주소']
        address = subAddress
        print(address)
        if address is not None:
            latitude, longitude = get_geocode(address, api_key)
            df.at[index, 'latitude'] = latitude
            df.at[index, 'longitude'] = longitude
        else:
            df.at[index, 'latitude'] = None
            df.at[index, 'longitude'] = None
        
    # 변경된 데이터프레임을 엑셀 파일로 저장
    df.to_excel('Seoul_vet_Coor.xlsx', index=False)  # 원하는 파일 경로로 변경하세요.