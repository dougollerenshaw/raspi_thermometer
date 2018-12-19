#!/usr/bin/python
import sys
import Adafruit_DHT

# Type of sensor, can be Adafruit_DHT.DHT11, Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
DHT_TYPE = Adafruit_DHT.DHT11

# Example of sensor connected to Raspberry Pi pin 23
DHT_PIN  = 4

while True:

    humidity, temperature = Adafruit_DHT.read_retry(DHT_TYPE,DHT_PIN)

    print 'Temp: {0:0.2f} C  Humidity: {1:0.2f} %'.format(temperature, humidity)
