import pandas as pd

# CSV 파일 불러오기, 인코딩을 'CP949'로 지정
try:
    df = pd.read_csv('Seoul_vet.csv', encoding='CP949')
except UnicodeDecodeError:
    # CP949로도 열리지 않을 경우, 다른 인코딩을 시도
    df = pd.read_csv('Seoul_vet.csv', encoding='EUC-KR')

# '상세영업상태코드'가 '0000'인 행만 추출
filtered_df = df[df['상세영업상태코드'] == 0000]

# 결과를 엑셀 파일로 저장
filtered_df.to_excel('Seoul_vet.xlsx', index=False)
