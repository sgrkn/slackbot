# ライブラリの読み込み
import json
import requests
 
# 天気情報を取得するための関数
def get_weather(city_number):
    url = "https://weather.tsukumijima.net/api/forecast/city/%s" % city_number
    # URLアクセスして情報を取得する
    response = requests.get(url)
    response.raise_for_status()
    # 取得したjsonデータを読み込む
    weather_data = json.loads(response.text)
 
    return(weather_data)