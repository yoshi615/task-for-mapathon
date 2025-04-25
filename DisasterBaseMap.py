pip install geopandas folium geopy

import folium
from geopy.geocoders import Nominatim

# 国名のリスト
countries = ["Japan", "France", "Brazil", "Australia", "India"]

# 地図の初期設定
m = folium.Map(location=[20, 0], zoom_start=2)

# ジオコーダーの設定
geolocator = Nominatim(user_agent="geoapi")

# 各国を地図上にプロット
for country in countries:
    location = geolocator.geocode(country)  # 国名を座標に変換
    if location:
        folium.Marker(
            location=[location.latitude, location.longitude],
            popup=country,
        ).add_to(m)

# 地図を表示
m.save("map_with_countries.html")
print("地図が 'map_with_countries.html' に保存されました。ブラウザで開いて確認してください。")