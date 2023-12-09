import pandas as pd

# 엑셀 파일 불러오기
df = pd.read_excel('vets_list.xlsx')  # '파일경로.xlsx'를 실제 파일 경로로 변경하세요.

# 'address' 열에 있는 주소 순회
for address in df['address']:
    print(address)
