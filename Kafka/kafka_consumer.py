# Import the necessary libraries

from kafka import KafkaConsumer
from json import loads
import json
from s3fs import S3FileSystem

import configparser

# Create an instance of ConfigParser
config = configparser.ConfigParser()

# Read the configuration file 'config.txt'
config.read('config.txt')

# Get the value of 'publicIP' from the 'Config' section in the configuration file
# 'publicIP' now contains the value of 'publicIP' from the configuration file
publicIP = config.get('Config', 'publicIP')
bucketName = config.get('Config', 'bucketName')

consumer = KafkaConsumer(
    'test',
    bootstrap_servers=['{}:9092'.format(publicIP)],
    value_deserializer=lambda x: loads(x.decode('utf-8')))

# Consume messages from the 'test' topic
for out in consumer:
    # Print the value of each message
    print(out.value)

s3 = S3FileSystem()

# Consume messages from the 'test' topic and store them in separate JSON files in S3
for count, i in enumerate(consumer):
    # Open a file in S3 for writing
    with s3.open("s3://{}/stock_market_{}.json".format(bucketName,count), 'w') as file:
        # Write the JSON data to the file
        json.dump(i.value, file)



