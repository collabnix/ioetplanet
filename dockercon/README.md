# Demo for Dockercon

- Verifying if Docker 20.10.3 is installed 
- Verifying if Sensor is detected
- Building Docker Image for RedisTimeSeries
- Running RedisTimeseries Docker image on Jetson Nano
- Clone the Repository
- Running Sensorloader script and pushing it to the local RedisTimeSeries database
- Running Grafana 
- Ploting Temperature, Humidity and Pressure onto the Grafana dashboard


## Verifying Docker version

SSH to 70.167.220.160 and install Docker

```
pico@pico1:~$ docker version
Client: Docker Engine - Community
 Version:           20.10.3
 API version:       1.41
 Go version:        go1.13.15
 Git commit:        48d30b5
 Built:             Fri Jan 29 14:33:34 2021
 OS/Arch:           linux/arm64
 Context:           default
 Experimental:      true

Server: Docker Engine - Community
 Engine:
  Version:          20.10.6
  API version:      1.41 (minimum version 1.12)
  Go version:       go1.13.15
  Git commit:       8728dd2
  Built:            Fri Apr  9 22:43:42 2021
  OS/Arch:          linux/arm64
  Experimental:     false
 containerd:
  Version:          1.4.3
  GitCommit:        269548fa27e0089a8b8278fc4fc781d7f65a939b
 nvidia:
  Version:          1.0.0-rc92
  GitCommit:        ff819c7e9184c13b7c2607fe6c30ae19403a7aff
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
 ```
 

## Verifying if Sensor is detected

```
 i2cdetect -r -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- --
```


## Building Docker Image for RedisTimeSeries for Jetson Nano

```
git clone --recursive https://github.com/RedisTimeSeries/RedisTimeSeries.git
cd RedisTimeSeries.git
```

```
docker build -t ajeetraina/redistimeseries-jetson . -f Dockerfile.jetson.edge
```

## Running RedisTimeSeries 


```
docker run -dit -p 6379:6379 ajeetraina/redistimeseries-jetson
```

## Verifying if RedisTimeSeries Module is loaded

```
redis-cli
127.0.0.1:6379> info modules
# Modules
module:name=timeseries,ver=999999,api=1,filters=0,usedby=[],using=[],options=[]
127.0.0.1:6379>
```

## Clone the repository

```
$ git clone https://github.com/redis-developer/redis-datasets
$ cd redis-datasets/redistimeseries/realtime-sensor-jetson
```

## Running Sensorload Script

```
sudo python3 sensorloader2.py --host localhost --port 6379
```


## Running Grafana on Jetson Nano


```
docker run -d -e "GF_INSTALL_PLUGINS=redis-app" -p 3000:3000 grafana/grafana
```

Try to add data source "redis://70.167.220.160:6379"


