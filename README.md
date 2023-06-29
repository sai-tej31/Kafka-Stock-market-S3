# Kafka-to-S3 Data Pipeline with Amazon Glue, Crawler, and Athena 


This project is designed to showcase a simple implementation of Kafka producers and consumers for stock market data. It includes files for producing and consuming data using Kafka, and store data in S3.

## Table of Contents

- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Next - Steps](#next-Steps)
- [Pre-requisites](#pre-requisites)


## Project Structure

The project has the following file structure:


- `Kafka/`: This directory contains the source code files for Kafka producers and consumers.
    - `kafka_producer.py`: This file contains the implementation of a Kafka producer for stock market data.
    - `kafka_consumer.py`: This file contains the implementation of a Kafka consumer for processing stock market data.
- `requirements.txt`: This file lists all the Python dependencies required by the project.
- `stock_market_data.csv`: This file contains sample stock market data for testing and demonstration purposes.

## Setup and Installation

To set up and install the project, follow these steps:

1. Clone the repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd <project-directory>`
3. Install the required dependencies using pip: `pip install -r requirements.txt`
4. Configure the necessary settings in `config.txt` if needed.

## Usage

To use the project, follow these instructions:

1. **Producer Script**
   - Open the `config.txt` file and set the `publicIP` value to the public IP address of your Kafka server.
   - Run the Kafka producer script `kafka_producer.py` to start producing stock market data. The script will continuously send random stock values from the `stock_market_data.csv` file to the Kafka topic named `test`.
   
2. **Consumer Script**
   - Open the `config.txt` file and set the `publicIP` value to the public IP address of your Kafka server.
   - Run the Kafka consumer script `kafka_consumer.py` to consume and process the stock market data. The script will print the received data and store each message as a separate JSON file in an S3 bucket. Make sure to provide the `bucketName` value in the `config.txt` file.



## Next Steps

### Analyzing Data with Amazon Glue and Amazon Athena

### Set up AWS Glue Crawler:

1. Go to AWS Glue service.
2. Create a new Glue Crawler and provide details such as name, data store (S3), and S3 bucket path.
3. Configure the crawler to use the JSON classifier.
4. Run the crawler to scan and catalog the JSON files, which creates a table in the AWS Glue Data Catalog.

### Query Data with Amazon Athena:

1. Go to Amazon Athena service.
2. Select the database associated with the Glue Crawler's table.
3. Write SQL queries in the Query Editor to analyze and explore the data.
4. Execute queries and view results in the Results pane.
5. Save queries, export results, or integrate Athena with other AWS services for further analysis.


**Note:** Before running the scripts, ensure that the Kafka server, ZooKeeper, and S3 bucket are properly configured.

## Pre-requisites
Follow these steps to start zookeeper and kafka server:


###### Step 1: Install Kafka and Java OpenJDK

1. Install Java OpenJDK on your EC2 instance. You can use the following command for EC2-linux:

   ```bash
   sudo yum install java-1.8.0

2. Install kafka on your EC2 instance. You can use the following command for EC2-linux:
   
   ```bash
   wget https://downloads.apache.org/kafka/3.3.1/kafka_2.12-3.3.1.tgz
   tar -xvf kafka_2.12-3.3.1.tgz



###### Step 2: Start ZooKeeper and Kafka Server

Start the ZooKeeper service by executing the following command in a terminal:


   ```bash
   cd kafka_2.12-3.3.1

   bin/zookeeper-server-start.sh config/zookeeper.properties

   bin/kafka-server-start.sh config/server.properties

###### Step 3: Create a kafka topic

   cd kafka
   bin/kafka-topics.sh --create --topic <topic_name> --bootstrap-server <public-ip>:9092 --replication-factor 1 --partitions 1



