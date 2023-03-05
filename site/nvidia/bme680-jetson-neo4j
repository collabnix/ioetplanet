![stars](https://img.shields.io/github/stars/collabnix/bme680-jetson-neo4j)
![forks](https://img.shields.io/github/forks/collabnix/bme680-jetson-neo4j)
![Discord](https://img.shields.io/discord/1020180904129335379)
![issues](https://img.shields.io/github/issues/collabnix/bme680-jetson-neo4j)
![Visitor count](https://shields-io-visitor-counter.herokuapp.com/badge?page=collabnix.bme680-jetson-neo4j)
![Twitter](https://img.shields.io/twitter/follow/collabnix?style=social)



# Storing BME680 Sensor data on Neo4j Graph Database and visualizing it using Docker Extension

<img width="941" alt="image" src="https://user-images.githubusercontent.com/34368930/222442463-c9e4ed08-4554-48d5-96e6-513b2f2d5edd.png">


Graph databases excel at representing complex relationships between data points, which can be useful in sensor data analysis.For example, if you have multiple sensors and want to understand how they are related, a graph database can help you model those relationships and perform queries to find patterns or anomalies in the data. It can also be useful for tracking the history of sensor readings and identifying trends over time.

Here's a project that shows how one can fetch sensor values from BME680, push it to Neo4j Graph database and display it using neo4j Docker Extension.


## Pre-requisite

### Hardware Requirements:

Jetson Nano: 2GB Model ($59)
A 5V 4Amp charger
128GB SD card
BME680 sensors

### Software Requirements:

- Neo4j Cloud Instance
- Neo4j Docker Extension
- Grafana Docker Extension


## Setting up NVIDIA Jetson Nano



- Jetson SD card image from [NVIDIA](https://developer.nvidia.com/embedded/downloads)
- Etcher software installed on your system 
- Preparing Your Jetson Nano for OS Installation 
- Unzip the SD card image downloaded from https://developer.nvidia.com/embedded/downloads. 
- Insert the SD card into your system. 
- Bring up the Etcher tool and select the target SD card to which you want to flash the image.

![image](https://user-images.githubusercontent.com/34368930/222421140-13b8ca21-f1a2-4727-aba6-db29e502f0b6.png)


### Getting Your Sensors Working

Using Grove Hat, you can plugin BME680 sensor to I2C as shown:

![image](https://user-images.githubusercontent.com/34368930/222420031-43909bf3-bf88-460b-a03e-f34f03498ee2.png)


After wiring the sensors, we recommend running I2C detection with i2cdetect to verify that you see the device: in our case it shows 76. Please note that the sensor communicates with a microcontroller using I2C or SPI communication protocols.

```
$ i2cdetect -r -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- 76 --
```


## Bringing up Neo4j Cloud Instance

Visit [this link](https://neo4j.com/cloud/platform/aura-graph-database/) to create a free neo4j hosted graph database


![image](https://user-images.githubusercontent.com/34368930/222420312-f603386a-96c6-4972-b234-39609169360f.png)


## Docker Desktop 


We'll be using [neo4j Docker Extension](https://github.com/collabnix/neo4j-docker-extension) to connect to the remote neo4j Cloud hosted instance.

<img width="1365" alt="image" src="https://user-images.githubusercontent.com/34368930/222422058-452a3464-e5c7-4b42-9943-9ec4f349844b.png">


## Cloning the Repository

```
 git clone https://github.com/collabnix/bme680-jetson-neo4j
 cd bme680-jetson-neo4j
```

## Importing neo4j Python Module

You can install the Neo4j driver for Python using pip:

```
pip install neo4j
```

## A Sample Python Script for Sensors

This creates a new node with the label "SensorReading" and the specified properties. You can then query the database to retrieve sensor data and perform analysis or visualization.




```
from neo4j import GraphDatabase
  
driver = GraphDatabase.driver("neo4j+s://c9fafc6e.databases.neo4j.io", auth=("neo4j", "OgIO99y7E6vxXXXXXXXXXXHrJsTY"))

with driver.session() as session:
    session.run("CREATE (:SensorReading {sensor_id: 'sensor1', timestamp: datetime(), value: 23.4})")
```

## Running the Script

For this demonstration, I shall be using all the sensor values.
This script generates random values for temperature, humidity, pressure, and gas using the random library, and then inserts these values into Neo4j along with a timestamp. You can modify the ranges for the random values by changing the arguments to random.uniform() as needed.

```
python3 sensorloader.py
```

```
Inserted sensor reading - temperature: 26.68, humidity: 41.35, pressure: 1008.6, gas: 3110.63
Inserted sensor reading - temperature: 12.42, humidity: 49.71, pressure: 1149.34, gas: 4815.11
Inserted sensor reading - temperature: 27.73, humidity: 77.2, pressure: 1081.24, gas: 4737.95
Inserted sensor reading - temperature: 19.22, humidity: 50.17, pressure: 958.73, gas: 516.57
```

## Installing and Connecting neo4j Docker Extension to hosted neo4j Auro

```shell
git clone https://github.com/collabnix/neo4j-docker-extension
cd neo4j-docker-extension
make install
```

## Connecting to the remote neo4j instance



<img width="1508" alt="image" src="https://user-images.githubusercontent.com/313480/222407314-1c895e4c-8c27-452f-8ff9-02cc0455c0ab.png">


## Using Neo4j Data Source for Grafana

<img width="1364" alt="image" src="https://user-images.githubusercontent.com/34368930/222455775-c724e8c6-2a0b-4edc-8d16-cfb2252a59ee.png">

<img width="1370" alt="image" src="https://user-images.githubusercontent.com/34368930/222463241-8500a4b4-0d75-4cd3-bce2-83250b360da2.png">


Query:

```
MATCH (sr:SensorReading)
WHERE sr.timestamp >= $timeFrom AND sr.timestamp <= $timeTo
RETURN sr.timestamp as time, sr.temperature as temp, sr.humidity as hum, sr.pressure as press, sr.gas as gas_res
ORDER BY sr.timestamp ASC
```




## Sample Query

### Pressure

```css
MATCH (n) 
WHERE n.pressure IS NOT NULL
RETURN DISTINCT "node" as entity, n.pressure AS pressure LIMIT 25
UNION ALL 
MATCH ()-[r]-() 
WHERE r.pressure IS NOT NULL
RETURN DISTINCT "relationship" AS entity, r.pressure AS pressure LIMIT 25;
```

<img width="1029" alt="image" src="https://user-images.githubusercontent.com/34368930/222948945-63f7ec7d-9e02-48fd-9f9c-bcf0c3af62df.png">


### Explanation:

This is a Neo4j query written in the Cypher query language.

The query consists of two parts, separated by the "UNION ALL" keyword:

The first part of the query selects all nodes in the graph where the "pressure" property is not null, and returns the value of the "pressure" property for each node. The results are labeled with the string "node" as the entity and the "pressure" value.

The second part of the query selects all relationships in the graph where the "pressure" property is not null, and returns the value of the "pressure" property for each relationship. The results are labeled with the string "relationship" as the entity and the "pressure" value.

Both parts of the query use the "DISTINCT" keyword to ensure that only unique values are returned, and the "LIMIT" keyword to limit the number of results to 25.

Overall, the query returns a list of up to 25 pressure values from either nodes or relationships in the graph, along with an indicator of whether each value came from a node or a relationship.


### Temperature

```css
MATCH (n) 
WHERE n.temperature IS NOT NULL
RETURN DISTINCT "node" as entity, n.temperature AS temperature LIMIT 25
UNION ALL 
MATCH ()-[r]-() 
WHERE r.temperature IS NOT NULL
RETURN DISTINCT "relationship" AS entity, r.temperature AS temperature LIMIT 25;
```

<img width="575" alt="image" src="https://user-images.githubusercontent.com/34368930/222948922-1ba55db7-d40e-4b40-9b2b-ed79eb94fdc2.png">


### Explanation

This is a Neo4j query written in the Cypher query language.

The query is similar to the previous one, but instead of selecting nodes and relationships based on the "pressure" property, it selects nodes and relationships based on the "temperature" property.

The first part of the query selects all nodes in the graph where the "temperature" property is not null, and returns the value of the "temperature" property for each node. The results are labeled with the string "node" as the entity and the "temperature" value.

The second part of the query selects all relationships in the graph where the "temperature" property is not null, and returns the value of the "temperature" property for each relationship. The results are labeled with the string "relationship" as the entity and the "temperature" value.

Both parts of the query use the "DISTINCT" keyword to ensure that only unique values are returned, and the "LIMIT" keyword to limit the number of results to 25.

Overall, the query returns a list of up to 25 temperature values from either nodes or relationships in the graph, along with an indicator of whether each value came from a node or a relationship.

## Understanding the Relationship

Sure, here is an example of how you might model a BME680 sensor and its readings in Neo4j:

First, you would create a "Sensor" node to represent your BME680 sensor. This node might have properties like "name" and "manufacturer", as well as any other information you want to store about the sensor.

```css
CREATE (:Sensor {name: 'BME680', manufacturer: 'Bosch'})
```

Next, you would create a "Timestamp" node to represent a particular point in time when a reading was taken. This node might have a "timestamp" property that stores the date and time the reading was taken.

```css
CREATE (:Timestamp {timestamp: datetime()})
```

Then, you would create a "READS" relationship between the Sensor node and the Timestamp node, with properties like "temperature", "pressure", "humidity", etc., representing the values that were read from the sensor at that time. For example, to create a reading where the temperature is 25 degrees Celsius, the pressure is 1000 hPa, and the humidity is 50%, you might use a query like this:

```css
MATCH (s:Sensor {name: 'BME680'}), (t:Timestamp)
CREATE (s)-[:READS {temperature: 37.0, pressure: 1168.83, humidity: 37.23}]->(t)
```

<img width="1505" alt="image" src="https://user-images.githubusercontent.com/34368930/222949941-236cd924-3ac8-4ed8-98a5-9b2a8de795e2.png">


This query creates a "READS" relationship between the Sensor node and the Timestamp node, with properties for temperature, pressure, and humidity set to the values 25, 1000, and 50, respectively.

You can then use Cypher queries to retrieve readings from the database, filter them based on criteria like time range or sensor type, and visualize the data in various ways using tools like Neo4j Bloom or other visualization tools.
