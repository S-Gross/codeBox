__author__ = 'sgr'

from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

import logging
import requests


import sys


# This is the method which is schedulered
def tick():
    print('Updateing the weather forcast! The time is: %s' % datetime.now())

    #res = requests.get("http://api.openweathermap.org/data/2.5/forecast?q=Aachen,de&mode=json")
    #res = res.json()

    res = {"city":{"id":3247449,"name":"Aachen","coord":{"lon":6.08342,"lat":50.776642},"country":"DE","population":0,"sys":{"population":0}},"cod":"200","message":0.0122,"cnt":37,"list":[{"dt":1443182400,"main":{"temp":288.53,"temp_min":286.437,"temp_max":288.53,"pressure":985.28,"sea_level":1035.88,"grnd_level":985.28,"humidity":90,"temp_kf":2.09},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":64},"wind":{"speed":2.12,"deg":290.506},"rain":{},"sys":{"pod":"d"},"dt_txt":"2015-09-25 12:00:00"},{"dt":1443193200,"main":{"temp":288.88,"temp_min":286.897,"temp_max":288.88,"pressure":985.14,"sea_level":1035.69,"grnd_level":985.14,"humidity":83,"temp_kf":1.98},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":56},"wind":{"speed":2.01,"deg":311.503},"rain":{"3h":0.02},"sys":{"pod":"d"},"dt_txt":"2015-09-25 15:00:00"},{"dt":1443204000,"main":{"temp":285.98,"temp_min":284.105,"temp_max":285.98,"pressure":986.04,"sea_level":1036.75,"grnd_level":986.04,"humidity":87,"temp_kf":1.87},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"clouds":{"all":36},"wind":{"speed":1.21,"deg":327.5},"rain":{},"sys":{"pod":"n"},"dt_txt":"2015-09-25 18:00:00"},{"dt":1443214800,"main":{"temp":281.47,"temp_min":279.707,"temp_max":281.47,"pressure":986.86,"sea_level":1038.11,"grnd_level":986.86,"humidity":91,"temp_kf":1.76},"weather":[{"id":800,"main":"Clear","description":"sky is clear","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":1.22,"deg":26.5056},"rain":{},"sys":{"pod":"n"},"dt_txt":"2015-09-25 21:00:00"},{"dt":1443225600,"main":{"temp":280.51,"temp_min":278.858,"temp_max":280.51,"pressure":987.44,"sea_level":1038.85,"grnd_level":987.44,"humidity":88,"temp_kf":1.65},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":80},"wind":{"speed":1.42,"deg":15.0014},"rain":{"3h":0.06},"sys":{"pod":"n"},"dt_txt":"2015-09-26 00:00:00"},{"dt":1443236400,"main":{"temp":283.06,"temp_min":281.519,"temp_max":283.06,"pressure":987.66,"sea_level":1039.24,"grnd_level":987.66,"humidity":96,"temp_kf":1.54},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":92},"wind":{"speed":1.87,"deg":24.004},"rain":{"3h":0.45},"sys":{"pod":"n"},"dt_txt":"2015-09-26 03:00:00"},{"dt":1443247200,"main":{"temp":283.62,"temp_min":282.19,"temp_max":283.62,"pressure":988.21,"sea_level":1040.07,"grnd_level":988.21,"humidity":98,"temp_kf":1.43},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":88},"wind":{"speed":2.42,"deg":39.5014},"rain":{"3h":0.17},"sys":{"pod":"d"},"dt_txt":"2015-09-26 06:00:00"},{"dt":1443258000,"main":{"temp":285.79,"temp_min":284.466,"temp_max":285.79,"pressure":989.27,"sea_level":1040.64,"grnd_level":989.27,"humidity":93,"temp_kf":1.32},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":68},"wind":{"speed":3.46,"deg":53.0013},"rain":{"3h":0.09},"sys":{"pod":"d"},"dt_txt":"2015-09-26 09:00:00"},{"dt":1443268800,"main":{"temp":286.78,"temp_min":285.572,"temp_max":286.78,"pressure":989.16,"sea_level":1040.2,"grnd_level":989.16,"humidity":83,"temp_kf":1.21},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":{"all":48},"wind":{"speed":3.61,"deg":48.5041},"rain":{"3h":0.03},"sys":{"pod":"d"},"dt_txt":"2015-09-26 12:00:00"},{"dt":1443279600,"main":{"temp":286.95,"temp_min":285.851,"temp_max":286.95,"pressure":989.09,"sea_level":1039.92,"grnd_level":989.09,"humidity":75,"temp_kf":1.1},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":64},"wind":{"speed":4.11,"deg":44.0056},"rain":{},"sys":{"pod":"d"},"dt_txt":"2015-09-26 15:00:00"},{"dt":1443290400,"main":{"temp":284.95,"temp_min":283.961,"temp_max":284.95,"pressure":989.98,"sea_level":1041.09,"grnd_level":989.98,"humidity":75,"temp_kf":0.99},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":56},"wind":{"speed":4.12,"deg":50.0002},"rain":{"3h":0.04},"sys":{"pod":"n"},"dt_txt":"2015-09-26 18:00:00"},{"dt":1443301200,"main":{"temp":283.75,"temp_min":282.87,"temp_max":283.75,"pressure":990.7,"sea_level":1042.23,"grnd_level":990.7,"humidity":81,"temp_kf":0.88},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":24},"wind":{"speed":3.76,"deg":63.001},"rain":{"3h":0.01},"sys":{"pod":"n"},"dt_txt":"2015-09-26 21:00:00"},{"dt":1443312000,"main":{"temp":283.07,"temp_min":282.297,"temp_max":283.07,"pressure":991.05,"sea_level":1042.85,"grnd_level":991.05,"humidity":84,"temp_kf":0.77},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"clouds":{"all":44},"wind":{"speed":3.66,"deg":69.5034},"rain":{},"sys":{"pod":"n"},"dt_txt":"2015-09-27 00:00:00"},{"dt":1443322800,"main":{"temp":281.71,"temp_min":281.052,"temp_max":281.71,"pressure":991.43,"sea_level":1043.43,"grnd_level":991.43,"humidity":89,"temp_kf":0.66},"weather":[{"id":800,"main":"Clear","description":"sky is clear","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":3.56,"deg":77.5081},"rain":{},"sys":{"pod":"n"},"dt_txt":"2015-09-27 03:00:00"},{"dt":1443333600,"main":{"temp":280.05,"temp_min":279.496,"temp_max":280.05,"pressure":992.48,"sea_level":1044.5,"grnd_level":992.48,"humidity":92,"temp_kf":0.55},"weather":[{"id":800,"main":"Clear","description":"sky is clear","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":3.41,"deg":75.5003},"rain":{},"sys":{"pod":"d"},"dt_txt":"2015-09-27 06:00:00"},{"dt":1443344400,"main":{"temp":285.26,"temp_min":284.821,"temp_max":285.26,"pressure":993.46,"sea_level":1044.94,"grnd_level":993.46,"humidity":77,"temp_kf":0.44},"weather":[{"id":800,"main":"Clear","description":"sky is clear","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":4.66,"deg":77.5014},"rain":{},"sys":{"pod":"d"},"dt_txt":"2015-09-27 09:00:00"},{"dt":1443355200,"main":{"temp":287.36,"temp_min":287.03,"temp_max":287.36,"pressure":993.26,"sea_level":1044.61,"grnd_level":993.26,"humidity":68,"temp_kf":0.33},"weather":[{"id":800,"main":"Clear","description":"sky is clear","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":5.27,"deg":71.5016},"rain":{},"sys":{"pod":"d"},"dt_txt":"2015-09-27 12:00:00"},{"dt":1443366000,"main":{"temp":287.42,"temp_min":287.197,"temp_max":287.42,"pressure":993.15,"sea_level":1044.24,"grnd_level":993.15,"humidity":65,"temp_kf":0.22},"weather":[{"id":800,"main":"Clear","description":"sky is clear","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":5.21,"deg":66.5},"rain":{},"sys":{"pod":"d"},"dt_txt":"2015-09-27 15:00:00"},{"dt":1443376800,"main":{"temp":284.06,"temp_min":283.954,"temp_max":284.06,"pressure":993.93,"sea_level":1045.38,"grnd_level":993.93,"humidity":68,"temp_kf":0.11},"weather":[{"id":800,"main":"Clear","description":"sky is clear","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":4.47,"deg":65.0067},"rain":{},"sys":{"pod":"n"},"dt_txt":"2015-09-27 18:00:00"},{"dt":1443387600,"main":{"temp":281.248,"temp_min":281.248,"temp_max":281.248,"pressure":994.87,"sea_level":1046.73,"grnd_level":994.87,"humidity":81,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"sky is clear","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":3.91,"deg":85.502},"rain":{},"sys":{"pod":"n"},"dt_txt":"2015-09-27 21:00:00"},{"dt":1443398400,"main":{"temp":279.107,"temp_min":279.107,"temp_max":279.107,"pressure":995.23,"sea_level":1047.64,"grnd_level":995.23,"humidity":94,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"sky is clear","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":3.77,"deg":90.5016},"rain":{},"sys":{"pod":"n"},"dt_txt":"2015-09-28 00:00:00"},{"dt":1443409200,"main":{"temp":278.005,"temp_min":278.005,"temp_max":278.005,"pressure":995.62,"sea_level":1047.99,"grnd_level":995.62,"humidity":92,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"sky is clear","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":3.51,"deg":89},"rain":{},"sys":{"pod":"n"},"dt_txt":"2015-09-28 03:00:00"},{"dt":1443420000,"main":{"temp":277.45,"temp_min":277.45,"temp_max":277.45,"pressure":996.25,"sea_level":1048.77,"grnd_level":996.25,"humidity":92,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"sky is clear","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":3.32,"deg":85.5008},"rain":{},"sys":{"pod":"d"},"dt_txt":"2015-09-28 06:00:00"},{"dt":1443430800,"main":{"temp":284.239,"temp_min":284.239,"temp_max":284.239,"pressure":997.33,"sea_level":1049.18,"grnd_level":997.33,"humidity":72,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"sky is clear","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":4.38,"deg":87.5008},"rain":{},"sys":{"pod":"d"},"dt_txt":"2015-09-28 09:00:00"},{"dt":1443441600,"main":{"temp":287.267,"temp_min":287.267,"temp_max":287.267,"pressure":996.94,"sea_level":1048.26,"grnd_level":996.94,"humidity":66,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"sky is clear","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":4.82,"deg":78.5027},"rain":{},"sys":{"pod":"d"},"dt_txt":"2015-09-28 12:00:00"},{"dt":1443452400,"main":{"temp":287.602,"temp_min":287.602,"temp_max":287.602,"pressure":996.07,"sea_level":1047.19,"grnd_level":996.07,"humidity":64,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"sky is clear","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":4.57,"deg":67.5},"rain":{},"sys":{"pod":"d"},"dt_txt":"2015-09-28 15:00:00"},{"dt":1443463200,"main":{"temp":283.925,"temp_min":283.925,"temp_max":283.925,"pressure":996.28,"sea_level":1047.57,"grnd_level":996.28,"humidity":72,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"sky is clear","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":3.77,"deg":56.5084},"rain":{},"sys":{"pod":"n"},"dt_txt":"2015-09-28 18:00:00"},{"dt":1443474000,"main":{"temp":281.016,"temp_min":281.016,"temp_max":281.016,"pressure":996.34,"sea_level":1048.22,"grnd_level":996.34,"humidity":91,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":0},"wind":{"speed":3.31,"deg":57.5021},"rain":{"3h":0.01},"sys":{"pod":"n"},"dt_txt":"2015-09-28 21:00:00"},{"dt":1443484800,"main":{"temp":278.731,"temp_min":278.731,"temp_max":278.731,"pressure":996,"sea_level":1048.31,"grnd_level":996,"humidity":91,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"sky is clear","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":2.65,"deg":68.0026},"rain":{},"sys":{"pod":"n"},"dt_txt":"2015-09-29 00:00:00"},{"dt":1443495600,"main":{"temp":277.013,"temp_min":277.013,"temp_max":277.013,"pressure":995.65,"sea_level":1047.94,"grnd_level":995.65,"humidity":89,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"sky is clear","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":2.66,"deg":67.0046},"rain":{},"sys":{"pod":"n"},"dt_txt":"2015-09-29 03:00:00"},{"dt":1443506400,"main":{"temp":276.613,"temp_min":276.613,"temp_max":276.613,"pressure":995.49,"sea_level":1048.03,"grnd_level":995.49,"humidity":87,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"clouds":{"all":24},"wind":{"speed":2.81,"deg":69.5034},"rain":{},"sys":{"pod":"d"},"dt_txt":"2015-09-29 06:00:00"},{"dt":1443517200,"main":{"temp":283.999,"temp_min":283.999,"temp_max":283.999,"pressure":995.92,"sea_level":1047.84,"grnd_level":995.92,"humidity":79,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"clouds":{"all":32},"wind":{"speed":4.15,"deg":83.002},"rain":{},"sys":{"pod":"d"},"dt_txt":"2015-09-29 09:00:00"},{"dt":1443528000,"main":{"temp":286.572,"temp_min":286.572,"temp_max":286.572,"pressure":995.19,"sea_level":1046.54,"grnd_level":995.19,"humidity":67,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"sky is clear","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":5.21,"deg":76.5013},"rain":{},"sys":{"pod":"d"},"dt_txt":"2015-09-29 12:00:00"},{"dt":1443538800,"main":{"temp":286.691,"temp_min":286.691,"temp_max":286.691,"pressure":994.09,"sea_level":1045.35,"grnd_level":994.09,"humidity":63,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"sky is clear","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":5.46,"deg":69.0034},"rain":{},"sys":{"pod":"d"},"dt_txt":"2015-09-29 15:00:00"},{"dt":1443549600,"main":{"temp":283.709,"temp_min":283.709,"temp_max":283.709,"pressure":994.19,"sea_level":1045.57,"grnd_level":994.19,"humidity":67,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"sky is clear","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":5.26,"deg":68.005},"rain":{},"sys":{"pod":"n"},"dt_txt":"2015-09-29 18:00:00"},{"dt":1443560400,"main":{"temp":281.793,"temp_min":281.793,"temp_max":281.793,"pressure":994.22,"sea_level":1045.97,"grnd_level":994.22,"humidity":79,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"sky is clear","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":5.27,"deg":82.0018},"rain":{},"sys":{"pod":"n"},"dt_txt":"2015-09-29 21:00:00"},{"dt":1443571200,"main":{"temp":280.51,"temp_min":280.51,"temp_max":280.51,"pressure":993.47,"sea_level":1045.42,"grnd_level":993.47,"humidity":86,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"sky is clear","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":5.33,"deg":83.5009},"rain":{},"sys":{"pod":"n"},"dt_txt":"2015-09-30 00:00:00"}]}

    asd = 0

    sys.exit(0)
    # Creates weather Entity
    entityJSON = {"contextElements": [
        {
            "type": "weather",
            "isPattern": "false",
            "id": "weather",
            "attributes": [
                {
                    "name": "StartTime",
                    "type": "string",
                    "value": str(datetime.now())
                }
            ]
        }
    ],
        "updateAction": "APPEND"
    }
    #Debug
    #print(entityJSON)
    # Sends the entity element to the CB
    requests.post(url=urlCB + "updateContext", headers=CBheader, json=entityJSON)

    # Add attributes to  weather entity
    for i in range(0, len(header)):
        #print("Attribute = " + str(i))
        appendAttrJSON =    {"contextElements": [
                                {
                                    "type": "weather",
                                    "isPattern": "false",
                                    "id": "weather",
                                    "attributes": [
                                    {   "name": header[i],
                                        "type": "string",
                                        "value": str(res01[0][i])
                                    } ]
                                } ],
                            "updateAction": "APPEND"
                            }
        # post json to create further attribute
        # Debug
        #print(appendAttrJSON)
        requests.post(url = urlCB + "updateContext", headers = CBheader, json = appendAttrJSON)





if __name__ == '__main__':
    tick()

    # Init the logger instance
    logging.basicConfig()
    print("The weather service is started")
    # The official Advanced Python Scheduler doc: http://apscheduler.readthedocs.org/en/3.0/index.html
    scheduler = BlockingScheduler()
    #scheduler.add_job(lambda: tick(), 'interval', minutes=5)
    scheduler.add_job(lambda: tick(), 'interval', seconds=5)

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

    finally:
        scheduler.shutdown()
