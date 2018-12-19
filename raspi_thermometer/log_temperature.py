import aws_utils
import datetime
import Adafruit_DHT

def log_temperature(to_database=True):
    # Type of sensor, can be Adafruit_DHT.DHT11, Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
    DHT_TYPE = Adafruit_DHT.DHT11

    # Example of sensor connected to Raspberry Pi pin 23
    DHT_PIN  = 4

    humidity, temperature = Adafruit_DHT.read_retry(DHT_TYPE,DHT_PIN)
    print('current temperature = {} F'.format(temperature))
    print('current humidity = {}%'.format(humidity))
    print('current timestamp = {}'.format(datetime.datetime.now()))
    if to_database:
        aws_utils.add_item(
            timestamp=datetime.datetime.now(),
            temperature=temperature,
            humidity=humidity,
        )

if __name__ == '__main__':
    log_temperature()