# Demo for Dockercon

- Verifying if Docker 20.10.3 is installed 
- Building Docker Image for RedisTimeSeries
- Running Sensorloader script and pushing it to the local RedisTimeSeries database
- Running Grafana 
- Ploting Temperature, Humidity and Pressure onto the Grafana dashboard


## Building Docker Image for RedisTimeSeries for Jetson Nano

```
git clone --recursive https://github.com/RedisTimeSeries/RedisTimeSeries.git
cd RedisTimeSeries.git
```

```
docker build -t ajeetraina/redistimeseries-jetson . -f Dockerfile.jetson.edge
```

## Verifying if RedisTimeSeries Module is loaded

```
redis-cli
127.0.0.1:6379> info modules
# Modules
module:name=timeseries,ver=999999,api=1,filters=0,usedby=[],using=[],options=[]
127.0.0.1:6379>
```

## Running Sensorload Script

```
sudo python3 sensorloader2.py --host localhost --port 6379
```


## Running Grafana on Jetson Nano


```
docker run -d -e "GF_INSTALL_PLUGINS=redis-app" -p 3000:3000 grafana/grafana
```


