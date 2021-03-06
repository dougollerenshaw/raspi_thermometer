import plotly.plotly as py
import json
import time
import readadc
import datetime

# with open('./config.json') as config_file:
#     plotly_user_config = json.load(config_file)

# py.sign_in(plotly_user_config["plotly_username"], plotly_user_config["plotly_api_key"])

# url = py.plot([
#     {
#         'x': [], 'y': [], 'type': 'scatter',
#         'stream': {
#             'token': plotly_user_config['plotly_streaming_tokens'][0],
#             'maxpoints': 200
#         }
#     }], filename='Raspberry Pi Streaming Example Values')

# print "View your streaming graph here: ", url

# temperature sensor middle pin connected channel 0 of mcp3008
sensor_pin = 0
readadc.initialize()

# stream = py.Stream(plotly_user_config['plotly_streaming_tokens'][0])
# stream.open()

#the main sensor reading and plotting loop
while True:
    sensor_data = readadc.readadc(sensor_pin,
                                  readadc.PINS.SPICLK,
                                  readadc.PINS.SPIMOSI,
                                  readadc.PINS.SPIMISO,
                                  readadc.PINS.SPICS)

    millivolts = sensor_data * (3300.0 / 1024.0)
    # 10 mv per degree
    temp_C = ((millivolts - 100.0) / 10.0) - 40.0
    # convert celsius to fahrenheit
    temp_F = (temp_C * 9.0 / 5.0) + 32
    # remove decimal point from millivolts
    millivolts = "%d" % millivolts
    # show only one decimal place for temprature and voltage readings
    temp_C = "%.1f" % temp_C
    temp_F = "%.1f" % temp_F

    print('millivolts = {}'.format(millivolts))
    print('temprature (F) = {}'.format(temp_F))

    # # write the data to plotly
    # stream.write({'x': datetime.datetime.now(), 'y': temp_C})

    # delay between stream posts
    time.sleep(0.25)
