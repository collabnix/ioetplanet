
Imagine you’re an air-conditioner manufacturing company that sells millions of smart AC units to consumers. You are building a centralized, smart climate control system that collects sensor data about a house’s temperature, pressure, and humidity and sends it to a central location for an efficiency analysis to help end users trim their electricity bills.

This blog post will show a simplified version of such a use case to demonstrate how it all works—so you can understand how to manage a wide variety of real-time IoT sensor data in Redis. 

Here’s what we used: 

- A BME680 environmental sensor to simulate a smart air conditioner and send data to Redis
- The RedisTimeSeries module to add time-series capabilities to Redis and store the data in time-series format
- Grafana with Redis Data Source to create graphs for usage analysis

## Hardware requirements:

- [Jetson Nano](https://developer.nvidia.com/buy-jetson?product=jetson_nano&location=US): 2GB Model ($59)
- A 5V 4Amp charger
- [128GB SD card](https://www.amazon.com/SanDisk-128GB-microSDXC-Memory-Adapter/dp/B073JYC4XM)
- [BME680 sensors](https://cdn-shop.adafruit.com/product-files/3660/BME680.pdf)

## Software requirements:

- Jetson SD card image from [NVIDIA](https://developer.nvidia.com/embedded/downloads)
- Etcher software installed on your system
Preparing Your Jetson Nano for OS Installation
Unzip the SD card image downloaded from  https://developer.nvidia.com/embedded/downloads.
Insert the SD card into your system.
Bring up the Etcher tool and select the target SD card to which you want to flash the image.

![Image1](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/m2ucqh9b9kbzxk3tf2yp.png)
 

Follow this 10-step process to see how it all fits together:

## Step 1: Get your sensors

![Image2](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/g0l6jplaud9zzyrtfs4x.png)
 

There’s a huge variety of sensors on the market, but this demonstration uses a Pimoroni BME680 breakout board. [BME680](https://cdn-shop.adafruit.com/product-files/3660/BME680.pdf) is an integrated environmental sensor developed for mobile applications and wearables, where size and low power consumption are key requirements. It can measure temperature, pressure, humidity, and indoor air quality, and is Raspberry Pi and Arduino-compatible.

## Step 2: Set up your IoT board

![Image3](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/lw2j3pmftpmvmmrqohg3.png)
 

For this demonstration, we’re using an [NVIDIA Jetson Nano board](https://developer.nvidia.com/embedded/jetson-nano), a small, powerful computer for developers to learn, explore, and build AI applications for edge devices. Priced at $59, it’s basically a developer kit that includes a Jetson Nano module with 2GB memory and delivers 472 GFLOPS of compute power. This demonstration should also work with other popular IoT devices, such as the Raspberry Pi, Arduino, Banana Pi, etc.

## Step 3: Wire it up

![Image4](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/doulgz7dtsdtuekuu14k.png)
 
The BME680 plugs directly into a Jetson Nano board without any connecting wires.


## Step 4: Get your sensor working

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

## Step 5: Get ready to Redis

You will need a Redis server up and running, either on your local laptop or in the cloud, and the Redis server must be compiled with the RedisTimeSeries module. In this demonstration, we’re using Redis Enterprise Cloud, a fully managed cloud database service that comes with the RedisTimeSeries module already built in and integrated.

## Step 6: Set up Redis Enterprise Cloud
If you are completely new to RedisTimeSeries, check out our RedisTimeSeries Quick Start tutorial. It explains how to get started with [Redis Enterprise Cloud](https://redis.com/redis-enterprise-cloud/overview/) and how to enable RedisTimeSeries. You will need a few details for this implementation:

- Redis database name
- Redis database endpoint
- Port number
- Default user password

![Image5](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/eo3v7pxt8hmxgp20zfns.png)
 

## Step 7: Clone the project repository

```
$ git clone https://github.com/redis-developer/redis-datasets
$ cd redis-datasets/redistimeseries/realtime-sensor-jetson
```

Reading the sensor values from the BME680 is fairly straightforward, but requires you to set a few configuration values. You can also run the sensor in two different “modes”—with or without gas readings. Just taking temperature, pressure, and humidity readings lets you sample data much faster.

Let’s look first at the library import and the configuration settings. Open a terminal window, create a file, and then type the following:

```
import bme680
import time
import datetime
import csv
import argparse
import redis
```

The first module, bme680, allows you to easily write Python code that reads the humidity, temperature, and pressure from the sensor. Similarly, there are other Python modules, such as time, to handle time-related tasks, redis to import Redis Python modules, and so on. We’re using the time library to introduce a small delay between each reading of the sensor to help ensure consistent results.


```
print("""read-sensor.py - Displays temperature, pressure, humidity, and gas.
Press Ctrl+C to exit!
""")

try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except IOError:
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

# These calibration data can safely be commented
# out, if desired.

print('Calibration data:')
for name in dir(sensor.calibration_data):

    if not name.startswith('_'):
        value = getattr(sensor.calibration_data, name)

        if isinstance(value, int):
            print('{}: {}'.format(name, value))

# These oversampling settings can be tweaked to
# change the balance between accuracy and noise in
# the data.

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)
```

The sensor = bme680.BME680() command creates an instance of the sensor that we’ll use to configure the settings and get the sensor’s readings. The _oversample settings we established for the humidity, pressure, and temperature measurements are designed to strike a balance between accurate readings and minimizing noise. The higher the oversampling, the greater the noise reduction, albeit accompanied by a reduction in accuracy.

The _filter protects sensor readings against transient changes in conditions, e.g. a door slamming that could cause the pressure to change momentarily, and the IIR filter removes these transient spiky values.

Shown in the code below, the gas measurement has a few settings that can be tweaked. It can be enabled or disabled with set_gas_status. Disabling it allows the other readings to be taken more rapidly, as mentioned above. The temperature of the hot plate and how long it’s held at that temperature can also be altered, although we recommend not changing these settings if your gas resistance readings look sensible.

```
print('\n\nInitial reading:')
for name in dir(sensor.data):
    value = getattr(sensor.data, name)

    if not name.startswith('_'):
        print('{}: {}'.format(name, value))

sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)

# Up to 10 heater profiles can be configured, each
# with their own temperature and duration.
# sensor.set_gas_heater_profile(200, 150, nb_profile=1)
# sensor.select_gas_heater_profile(1)


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, help="redis instance port", default=6379)
parser.add_argument(
    "--password", type=int, help="redis instance password", default=None
)
parser.add_argument("--verbose", help="enable verbose output", action="store_true")
parser.add_argument("--host", type=str, help="redis instance host", default="127.0.0.1")


args = parser.parse_args()
```

Next, we define the Redis connector, where we specify the Redis instance host, port, and password. As shown below, the code below defines the various RedisTimeSeries keys, such as a temperature key (TS:TEMPERATURE), pressure key (TS:PRESSURE), and humidity key (TS:HUMIDITY).

```
# redis setup
redis_obj = redis.Redis(host=args.host, port=args.port, password=args.password)
temperature_key = "ts:temperature"
pressure_key = "ts:pressure"
humidity_key = "ts:humidity"
```

The sensor.get_sensor_data() instruction gets the data from the sensor and populates the three variables with temperature, humidity, and pressure.

```
print('\n\nPolling:')
try:
    while True:
        if not sensor.get_sensor_data():
            continue

        output = '{0:.2f} C,{1:.2f} hPa,{2:.2f} %RH'.format(
            sensor.data.temperature,
            sensor.data.pressure,
            sensor.data.humidity)

        if not sensor.data.heat_stable:
            print('Heat unstable: ' + output)
            continue

        print('{0},{1} Ohms'.format(
            output,
            sensor.data.gas_resistance))

        date = datetime.datetime.now()
        timestamp = int(date.timestamp() * 1000)

        # Create pipeline
        pipe = redis_obj.pipeline()

        pipe.execute_command(
            "ts.add", temperature_key, timestamp, sensor.data.temperature
        )

        pipe.execute_command(
            "ts.add", pressure_key, timestamp, sensor.data.pressure
        )

        pipe.execute_command("ts.add", humidity_key,
                             timestamp, sensor.data.humidity)

        # Execute pipeline
        pipe.execute()
        time.sleep(1)

except KeyboardInterrupt:
    pass
```

Next, a “transactional pipeline” is constructed by calling the .pipeline() method on a Redis connection without arguments. Under the covers, the pipeline collects all the commands that are passed until the .execute() method is called. As you can see, we used RedisTimeSeries’ TS.ADD command to populate the sensor data structure. You can access the complete code via this GitHub Repository.

## Step 8: Execute the script

Before you execute the script, you will need to import the bme680 and smbus Python modules, as shown here:

```
$ pip3 install bme680
```

```
$ pip3 install smbus
```
Make sure you supply the right Redis Enterprise Cloud database endpoints, username, and password:

```
$ python3 sensorloader.py --host <Redis Enterprise Cloud host> --port <port>  --password <password> 
```

You can run the monitor command to verify that sensor data is being populated, as shown here:

```
$ redis-cli -h redis-12929.c212.ap-south-1-1.ec2.cloud.redislabs.com -p 12929
redis-12929.c212.ap-south-1-1.ec2.cloud.redislabs.com:12929> auth <password>
OK
redis-12929.c212.ap-south-1-1.ec2.cloud.redislabs.com:12929> monitor
OK
1611046300.446452 [0 122.179.79.106:53715] "info" "server"
1611046300.450452 [0 122.179.79.106:53717] "info" "stats"
1611046300.450452 [0 122.179.79.106:53716] "info" "clients"
1611046300.486452 [0 122.179.79.106:53714] "info" "memory"
1611046300.486452 [0 122.179.79.106:53713] "info" "server"
1611046300.494452 [0 122.179.79.106:53715] "info" "memory"
1611046300.498452 [0 122.179.79.106:53717] "info" "commandstats"
1611046300.522452 [0 122.179.79.106:53716] "dbsize"
1611046301.498452 [0 122.179.79.106:53714] "info" "memory"
1611046301.498452 [0 122.179.79.106:53713] "info" "server"
1611046301.498452 [0 122.179.79.106:53715] "info" "server"
1611046301.498452 [0 122.179.79.106:53716] "info" "clients"
1611046301.498452 [0 122.179.79.106:53717] "info" "stats"
1611046301.554452 [0 122.179.79.106:53714] "info" "memory"
1611046301.562452 [0 122.179.79.106:53717] "info" "commandstats"
```

## Step 9: Deploy Grafana

It’s exciting to see the sensor data plotted in Grafana. To implement this, run the command below:

```
$ docker run -d -e "GF_INSTALL_PLUGINS=redis-app" -p 3000:3000 grafana/grafana
```


Be sure that you have Docker Engine running in your system, either on your desktop system or in the cloud. For this demonstration, I have tested it on Docker Desktop for Mac.

Point your browser to https://<IP_ADDRESS>:3000. Use “admin” as username and password to log in to the Grafana dashboard.

![Image6](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/inlet1a6dw7k7pbi90l3.png)

 
Click the Data Sources option on the left side of the Grafana dashboard to add a data source.

![Image7](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/f9nm4l6s0kpst2u2yg8u.png)

 
Under the Add data source option, search for Redis and the Redis data source will appear as shown below:

![Image8](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/e0p3yhch9djksu982wms.png)
 
![Image9](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/a086m3i1rqdt3stnaaip.png)
 

Supply the name, Redis Enterprise Cloud database endpoint, and password, then click Save & Test.

![Image10](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dsumqkmoliad042xtb19.png)
 

Click Dashboards to import Redis and Redis Streaming. Click Import for both these options.

![Image11](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8x1vutlcoo84fj7a64c0.png)
 

Click on Redis to see a fancy Grafana dashboard that shows the Redis database information:

![Image12](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/novpv15y4db4ajuy3rfl.png)
 
![Image13](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/gun4eimc2mibgnko9vmx.png)
 

## Step 10: Plot RedisTimeSeries sensor data in Grafana

Finally, let’s create a sensor dashboard that shows temperature, pressure, and humidity. To start with temperature,  first click on + on the left navigation window. Under Create option, Select Dashboard and click on the Add new panel button.

![Image14](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6sy2kpee3yqrbwrgf0a7.png)

 
A new window will open showing the Query section. Select SensorT from the drop-down menu, choose RedisTimeSeries as type, TS.GET as command and ts”temperature as key.

![Image15](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qfcdew3loxc4v2et2lnn.png)
 

Choose TS.GET as a command.

![Image16](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/pe9njpyiwjqgoxn9oftp.png)
 

Type ts”temperature as the key.


![Image17](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/r2gu0h1uj8k5puqt3r7t.png)
 
Click Run followed by Save, as shown below:

![Image18](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/47ridm3tn47mpinlvo86.png)
 

Now you can save the dashboard by your preferred name:



Click Save.This will open up a sensor dashboard. You can click on Panel Title and select Edit.

![Image19](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zv2cjiad3ol8w2p03f5m.png)

Type Temperature and choose Gauge under Visualization.

![Image20](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/hqrdkzk9ctjlu36lef5a.png)
 

Click Apply and you should be able to see the temperature dashboard as shown here:

![Image21](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5u51205m4xl37crprckd.png)
 

Follow the same process for pressure (ts:pressure) and humidity (ts:humidity), and add them to the dashboard. You should be able to see the complete dashboard readings for temperature, humidity, and pressure. Looks amazing. Isn’t it?

![Image22](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6iytnsdqsom013d8gqtm.png)
 

Follow us over Twitter: 
- https://twitter.com/collabnix

