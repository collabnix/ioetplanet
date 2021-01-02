# Getting Started with BME680 Sensor on Jetson Nano

## Pre-requisite:

- BME680 sensor
- Jetson Nano

## Installing software

- Use i2cdetect command to detect the sensor

```
pico@pico1:~$ i2cdetect -r -y 1
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

- Install python modules

```
sudo pip3 install bme680
```

```
sudo pip3 install smbus
```


## Cloning this repository

```
git clone https://github.com/collabnix/ioetplanet
cd ioetplanet/nvidia/jetsonnano/sensors
```

## Running the Script

```
 sudo python3 read-sensor.py 
read-all.py - Displays temperature, pressure, humidity, and gas.

Press Ctrl+C to exit!


Calibration data:
par_gh1: -28
par_gh2: -11838
par_gh3: 18
par_h1: 708
par_h2: 1023
par_h3: 0
par_h4: 45
par_h5: 20
par_h6: 120
par_h7: -100
par_p1: 35680
par_p10: 30
par_p2: -10322
par_p3: 88
par_p4: 7420
par_p5: -83
par_p6: 30
par_p7: 22
par_p8: -214
par_p9: -3593
par_t1: 26242
par_t2: 26396
par_t3: 3
range_sw_err: 14
res_heat_range: 1
res_heat_val: 40
t_fine: 148732


Initial reading:
gas_index: 0
gas_resistance: 12561247.871044775
heat_stable: False
humidity: 16.973
meas_index: 0
pressure: 965.64
status: 32
temperature: 29.05


Polling:
29.05 C,965.65 hPa,16.98 %RH
29.06 C,965.63 hPa,16.97 %RH,3110.845596017859 Ohms
29.09 C,965.63 hPa,16.96 %RH,3862.703345199333 Ohms
29.13 C,965.61 hPa,16.93 %RH,4644.9963354335405 Ohms
```
