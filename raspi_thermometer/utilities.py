import json
import time
import readadc
import datetime
import numpy as np

class Thermometer(object):

    def __init__(self):
        self.sensor_pin = 0
        readadc.initialize()

    def read(self,n_counts=2000):

        self.temp_C_arr = np.zeros(n_counts)
        self.temp_F_arr = np.zeros(n_counts)

        for n in range(n_counts):

            sensor_data = readadc.readadc(self.sensor_pin,
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
            # add to array for averaging
            self.temp_C_arr[n] = temp_C
            self.temp_F_arr[n] = temp_F
            time.sleep(0.001)
 

        self.temp_F = np.mean(self.temp_F_arr)
        self.temp_C = np.mean(self.temp_C_arr)

if __name__ == '__main__':
    thermometer = Thermometer()
    while True:
        thermometer.read()
        temp_F = thermometer.temp_F
        print('temperature = {} F'.format(temp_F))
        # print('temp_array = {}'.format(thermometer.temp_F_arr))
        # print(' ')
        # time.sleep(0.25)