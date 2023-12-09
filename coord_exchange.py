# 라이브러리 가져오기
from pyproj import Proj, transform
import pandas as pd

# Projection 정의
# 중부원점(Bessel): 서울 등 중부지역 EPSG:2097
proj_1 = Proj(init='epsg:2097')

# WGS84 경위도: GPS가 사용하는 좌표계 EPSG:4326
proj_2 = Proj(init='epsg:4326')

# DataFrame = df.copy()

# x_list = []
# y_list = []

# for idx, row in DataFrame.iterrows():
#     x, y = row['x'], row['y']
#     x_, y_ = transform(proj_1, proj_2, x, y)
#     x_list.append(x_)
#     y_list.append(y_)
    
# df['lon'] = x_list
# df['lat'] = y_list

x, y = 185521.368171349, 450368.363433796
x_, y_ = transform(proj_1, proj_2, x, y)

print(x_, y_)