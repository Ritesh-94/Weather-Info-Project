import json
import pandas as pd
import requests

city = input()
date = input()
URL = 'https://api.oikolab.com/weather'
OIKO_KEY = 'oiko-lab key here'
resp = requests.get(URL,
                   params = {
                       'param' : ['temperature'],
                       'start' : date,
                       'location' : city,
                       'end' : date,
                       'api-key' : OIKO_KEY,
                       'freq' : 'D'
                   }
)

weather_data = resp.json()['data']
weather_data = json.loads(weather_data)
df = pd.DataFrame(index=pd.to_datetime(weather_data['index'], unit='s'),
                 data=weather_data['data'],
                  columns=weather_data['columns'])
temp=int(df.iloc[0,4])

print(f"Temperature for {city} on {date} = {temp} Degree Celcius")