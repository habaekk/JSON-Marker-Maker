import pandas as pd
import json

def jsonMaker():

    # 엑셀 파일 불러오기
    df = pd.read_excel('Seoul_vet_Coor.xlsx')  # 실제 파일 경로로 변경하세요.

    # JSON 형식으로 변환
    data = []
    for index, row in df.iterrows():
        if index == 100:
            break;
        entry = {
            "id": index + 1,
            "coordinate": {
                "latitude": row['latitude'],
                "longitude": row['longitude']
            },
            "title": row['사업장명'],
            "description": row['도로명주소']
        }
        data.append(entry)

    # JSON 파일로 저장
    with open('Markers.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Completed saving JSON file.")
