# Get weather data
curl -o $WS_HOME/web_data/weather.json -X GET --compressed 'https://devapi.qweather.com/v7/weather/3d?location=your_location_id&key=your_key'
# get context data
curl -o $WS_HOME/web_data/context.json -X GET 'https://v1.hitokoto.cn' 