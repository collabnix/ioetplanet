# Control DJI Tello Drone using Python

There are 2 ways you can control your DJI Tello. The first one is using your mobile device, you will need to download Tello or Tello EDU App first. You can also control your Tello via Python or Scratch programming. In this blog, we will see how to control Tello using Python.

## Pre-requisite:

- Linux System( Desktop or Edge device)
- Python3
- Tello Mobile app


Press the “Power” button of Tello once. Once it start blinking, open up Tello Android app to discover Tello drone. Open settings and configure WiFi settings like username and password. Connect your laptop to the Tello WiFI network. Follow the below steps to connect via Python script.

## Install using pip

```
pip install djitellopy
```
For Linux distributions with both python2 and python3 (e.g. Debian, Ubuntu, …) you need to run

```
pip3 install djitellopy
```

## API Reference

See djitellopy.readthedocs.io for a full reference of all classes and methods available.

## Step 1. Connect, TakeOff, Move and Land

The below Python script allows you to connect to the drone, take off, make some movement – Left and Right and then Land smoothly.

```
from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_left(100)
tello.rotate_counter_clockwise(90)
tello.move_forward(100)

tello.land()
```

## Step 2. Take a Picture


```
import cv2
from djitellopy import Tello

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()
cv2.imwrite("picture.png", frame_read.frame)

tello.land()
``

## Step 3. Recording a Video

```
# source https://github.com/damiafuentes/DJITelloPy
import time, cv2
from threading import Thread
from djitellopy import Tello

tello = Tello()

tello.connect()

keepRecording = True
tello.streamon()
frame_read = tello.get_frame_read()

def videoRecorder():
    # create a VideoWrite object, recoring to ./video.avi
   
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1 / 30)

    video.release()

# we need to run the recorder in a seperate thread, otherwise blocking options
#  would prevent frames from getting added to the video
recorder = Thread(target=videoRecorder)
recorder.start()

tello.takeoff()
tello.move_up(100)
tello.rotate_counter_clockwise(360)
tello.land()

keepRecording = False
recorder.join()
```

## Step 4. Control the drone using Keyboard

```
# source https://github.com/damiafuentes/DJITelloPy
from djitellopy import Tello
import cv2, math, time

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()

while True:
    # In reality you want to display frames in a seperate thread. Otherwise
    #  they will freeze while the drone moves.
   
    img = frame_read.frame
    cv2.imshow("drone", img)

    key = cv2.waitKey(1) & 0xff
    if key == 27: # ESC
        break
    elif key == ord('w'):
        tello.move_forward(30)
    elif key == ord('s'):
        tello.move_back(30)
    elif key == ord('a'):
        tello.move_left(30)
    elif key == ord('d'):
        tello.move_right(30)
    elif key == ord('e'):
        tello.rotate_clockwise(30)
    elif key == ord('q'):
        tello.rotate_counter_clockwise(30)
    elif key == ord('r'):
        tello.move_up(30)
    elif key == ord('f'):
        tello.move_down(30)

tello.land()
```

