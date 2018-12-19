from __future__ import print_function  # Python 2/3 compatibility
import boto3
import json
import decimal


def create_table():
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2',
                              endpoint_url="http://dynamodb.us-west-2.amazonaws.com")
    table = dynamodb.create_table(
        TableName='temperature_monitor_1_pi',
        KeySchema=[
            {
                "AttributeName": "timestamp",
                "KeyType": 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'timestamp',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    print("Table status:", table.table_status)


def add_item(timestamp, temperature, humidity=None, table='temperature_monitor_2'):

    dynamodb = boto3.resource('dynamodb', region_name='us-west-2',
                              endpoint_url="http://dynamodb.us-west-2.amazonaws.com")

    table = dynamodb.Table(table)

    print("Adding timestamp = {}, temperature = {}, humidity = {} to table {}".format(
        str(timestamp), temperature, humidity, table))

    return_statement = table.put_item(
        Item={
            'timestamp': str(timestamp),
            'temperature': decimal.Decimal(str(temperature)),
            'humidity': decimal.Decimal(str(humidity)),
        }
    )
    print('return statement = \n{}'.format(return_statement))


def scan(table='temperature_monitor_2'):
    # Helper class to convert a DynamoDB item to JSON.
    class DecimalEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, decimal.Decimal):
                if o % 1 > 0:
                    return float(o)
                else:
                    return int(o)
            return super(DecimalEncoder, self).default(o)

    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

    table = dynamodb.Table(table)

    response = table.scan()

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])

    return response
