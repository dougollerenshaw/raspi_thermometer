import aws_utils
import utilities
import datetime

def log_temperature(to_database=True):
    thermometer = utilities.Thermometer()
    thermometer.read()
    temp_F = thermometer.temp_F
    print('current temperature = {} F'.format(temp_F))
    print('current timestamp = {}'.format(datetime.datetime.now()))
    if to_database:
        aws_utils.add_item(
            timestamp=datetime.datetime.now(),
            temperature=temp_F
        )

if __name__ == '__main__':
    log_temperature()