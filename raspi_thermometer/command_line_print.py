#!/usr/bin/python
import sys
import Adafruit_DHT

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    print 'Temp: {0:0.2f} C  Humidity: {1:0.2f} %'.format(temperature, humidity)