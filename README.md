# JSON Marker Maker (JMM)

리액트 네이티브에서 지도 서비스를 만들 때(react-native-maps), Marker 라는 기능을 쓸 필요가 있었음.  
  
Marker 는 지도에 핀으로 표시를 해주는 기능으로, title, description, latitude, longitude 의 정보가 json 의 표멧으로 필요함.  
  
Marker 정보를 서버에서 처리하든, 디바이스(어플) 에서 처리하든 json 데이터가 필요함.  
  
원하는 데이터 정보는 1. 웹사이트에서만 표시되어 있거나 2. csv 의 파일 과 같은 경우로만 제공이 됨.  
  
많은 양의 데이터를 다루어야 하기 때문에 파이썬을 이용하여 자동화 프로그램을 만들어 문제를 해결 함.  

# Description

## main.py
전체 프로그램을 실행시킬 수 있음. 

## csvConverter.py
<img width="1000" alt="Screenshot 2023-12-10 at 3 08 57 PM" src="https://github.com/habaekk/JSON-Marker-Maker/assets/74465964/44c1f9b4-478c-4203-a82a-5afb3bb750f5">  
제공되는 csv 파일을 편의를 위해 xlsx 파일로 변환시킴. 데이터를 영업중인 병원만 뽑아오도록 필터링함.

## geoCodeGen.py
<img width="1000" alt="Screenshot 2023-12-10 at 3 02 43 PM" src="https://github.com/habaekk/htmlToXlsx/assets/74465964/4237692c-c174-44bc-adbc-5fdd393c3bfa">  
구글 클라우드 콘솔에서 'Geocoding API' 를 이용함. 사용하려면 API 키가 필요. .env 파일에 따로 키를 저장해 놓음.
주소를 api 의 입력값으로 보내면 거기에 맞는 GPS 좌표를 반환해줌. 위도 경도 값을 받아서 엑셀 파일에 추가해 저장함.

## jsonMaker.py
<img width="1000" alt="Screenshot 2023-12-10 at 3 02 52 PM" src="https://github.com/habaekk/htmlToXlsx/assets/74465964/be180333-3097-42e9-aeed-d2ef3be523dd">  
{title: 사업장명, description: 도로명 주소, coordinate: [위도, 경도]} 가 되는 json 파일을 생성.

## htmlTOxlsx.py
<img width="1000" alt="Screenshot 2023-12-10 at 3 02 31 PM" src="https://github.com/habaekk/htmlToXlsx/assets/74465964/2e7da59c-9b18-4dcd-bd10-2b3c6b5af699"> 
데이터를 제공하지 않고 웹 사이트에 게시만 되어 있는 경우. 웹크롤링을 이용해 표 형태의 데이터를 수집하여 엑셀 형태로 저장. find_all 의 태그, all_pages, page_url 등을 수정하여 커스텀 가능.  
데이터를 GPS 좌표로 변환했을 때, 위치가 정확하지 않아 사용하진 않음.

## coord_transfer.py
<img width="1000" alt="Screenshot 2023-12-10 at 3 17 47 PM" src="https://github.com/habaekk/JSON-Marker-Maker/assets/74465964/833b4950-b47b-4b53-a2e4-1d168c33a48a">  
csv 파일에 좌표 정보를 함께 제공해줌. GPS 좌표계가 아닌 중부원점 좌표계를 사용. Marker 에 쓰기 위해 좌표계를 변환하는 프로그램. 변환 결과가 정확하지 않아 사용하진 않음.

# reference
chatGPT4
