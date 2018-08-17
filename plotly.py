import plotly.plotly as py
import json
import sqlite3
dbname='sensehat.db'

from sense_hat import SenseHat
sense = SenseHat()

with open('./config.json') as config_file:
    plotly_user_config = json.load(config_file)

    py.sign_in(plotly_user_config["plotly_username"], plotly_user_config["plotly_api_key"])

    url=py.plot([
        {
            'x': [], 'y': [], 'type': 'scatter',
            'stream': {
                'token': plotly_user_config['plotly_streaming_tokens'][0],
                'maxpoints': 200
                }
            }], filename='Raspberry Pi Streaming Example Values')
    print "view your streaming graph here: ", url

stream = py.Stream(plotly_user_config['plotly_streaming_tokens'][0])
stream.open()

while True:
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    for temp in curs.execute("SELECT temp FROM SenseHat_data"):
        temperatures = temp
	for time in curs.execute("SELECT datetime FROM SenseHat_data"):
        times = time
    conn.close()

    stream.write({'x': times, 'y': temperatures})

    time.sleep(0.25)