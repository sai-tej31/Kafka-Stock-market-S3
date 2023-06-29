# Import the necessary libraries

import pandas as pd
from kafka import KafkaProducer
from json import dumps
import configparser

# Create an instance of ConfigParser
config = configparser.ConfigParser()

# Read the configuration file 'config.txt'
config.read('config.txt')

# Get the value of 'publicIP' from the 'Config' section in the configuration file
publicIP = config.get('Config', 'publicIP')

# 'publicIP' now contains the value of 'publicIP' from the configuration file


# Specify the producer with the public IP address of the EC2 Instance
# NOTE: Run the ZooKeeper and Kafka servers.

# Create a KafkaProducer with the specified bootstrap servers and value serializer
producer = KafkaProducer(bootstrap_servers=['{}:9092'.format(publicIP)],
                         value_serializer=lambda x: dumps(x).encode('utf-8'))


# Data Processing and Analysis

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('stock_market_data.csv')


# Continuously send random stock values from the DataFrame to the 'test' topic
while True:
    # Sample a random row from the DataFrame and convert it to a dictionary
    stock_val = data.sample(1).to_dict(orient="records")[0]

    # Send the stock value to the 'test' topic
    producer.send('test', value=stock_val)

# Flush any remaining messages in the producer
producer.flush()
