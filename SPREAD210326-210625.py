# THE SPREAD RATE BETWEEN BTUUSD210326 AND BTCUSD 210625 FUTURES

import requests
import json
from datetime import datetime
import matplotlib.pyplot as plt


start_day = datetime(2021, 3, 1, 00, 00).timestamp() * 1000
end_day = datetime(2021, 3, 12, 00, 00).timestamp() * 1000   

endPoint = 'https://dapi.binance.com'
path     = '/dapi/v1/klines'

limit = 916
response0326 = requests.get(endPoint + path,
    params = {
        'symbol':'BTCUSD_210326',
        'interval':'2h',
        # 'startTime':int(start_day),
        'endtime':int(end_day),
        'limit':limit
})
data0326 = response0326.json()

response0625 = requests.get(endPoint + path,
    params = {
        'symbol':'BTCUSD_210625',
        'interval':'2h',
        # 'startTime':int(start_day),
        'endtime':int(end_day),
        'limit':limit
})
data0625 = response0625.json()

listrate=[]
listtime=[]

for i in range(limit):
    listtime.append(datetime.fromtimestamp(float(data0625[i][0]/1000)))
    listrate.append(round(100*(float(data0625[i][4])-float(data0326[i][4]))/(float(data0326[i][4])),2))
plt.plot(listtime,listrate)
plt.show()

