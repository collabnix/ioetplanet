NEO-6M GPS Module with EPROM is a complete GPS module that is based on the NEO 6M GPS. This unit uses the latest technology to give the best possible positioning information and includes a larger built-in 25 x 25mm active GPS antenna with a UART TTL socket. A battery is also included so that you can obtain a GPS lock faster. This is an updated GPS module that can be used with ardupilot mega v2. This GPS module gives the best possible position information, allowing for better performance with your Ardupilot or other Multirotor control platform.

The GPS module has serial TTL output, it has four pins: TX, RX, VCC, and GND. You can download the u-centre software for configuring the GPS and changing the settings and much more. It is really good software (see link below).


## Table of Contents

1. [Intent](#Intent)
2. [Hardware](#hardware)
3. [Software](#software)
4. [Connect GPS Module to Rasberry Pi](#connect-the-gps-module-to-raspberry-pi)
5. [Ploting the GPS Values over Google Map](#ploting-the-gps-values-over-google-map)
6. [Stream Data Over PubNub](#stream-data-over-pubnub)

## Intent

How to connect GPS to Raspberry Pi or Arduino, fetch the latitude and longitude values and plot it over Google Map

## Hardware 

- Raspberry Pi/Arduino
- NEO-6M GPS Module with EPROM

![image](gps1.jpeg)

## Software

- Flash Rapsberry Pi SD card with OS using Etcher

## Connect the GPS module to the Raspberry PI. 

There are only 4 wires (F to F), so it's a simple connection.

![image](gpspins.png)

- Neo-6M RPI

- VCC to Pin 1, which is 3.3v

- TX to Pin 10, which is RX (GPIO15)

- RX to Pin 8, Which is TX (GPIO14)

- Gnd to Pin 6, which is Gnd

![image](gps2.jpeg)

###  Turn Off the Serial Console

By default, the Raspberry Pi uses the UART as a serial console. We need to turn off that functionality so that we can use the UART for our own application. Open a terminal session on the Raspberry Pi.

### Step 1. Backup the file cmdline.txt 

```
sudo cp /boot/cmdline.txt /boot/cmdline_backup.txt 
```



### Step 2. Edit cmdlint.txt and remove the serial interface

```
sudo nano /boot/cmdline.txt
```


### Step 3. Delete console=ttyAMA0,115200 

Once you delete it, save the file by pressing Ctrl X, Y, and Enter.

### Step 4. Edit /etc/inittab

```
sudo nano /etc/inittab 
```



### Step 5. Find ttyAMA0 

You can find ttyAMA0 by pressing Ctrl W and typing ttyAMA0 on the search line

Press Home > insert a # symbol to comment out that line and Ctrl X, Y, Enter to save.

```
sudo reboot
```


### Step 6. Test the GPS

Open a terminal session and type 

```
sudo apt-get install gpsd gpsd-clients
```


### Step 7. Start the serial port:

```
stty -F /dev/ttyAMA0 9600
```

Now start GPSD:

```
sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock
```

### Step 8. Final Results

```
cgps -s
```

### Fetching the Values

### Clone the repository

```
git clone https://github.com/collabnix/cherrybot
cd cherrybot/pubnub/
```

### Fetching the GPS values

```
python3 gps.py
```

```
Latitude=12.9814865and Longitude=77.6683425
Latitude=12.9814848333and Longitude=77.6683436667
Latitude=12.9814841667and Longitude=77.6683451667
Latitude=12.9814818333and Longitude=77.6683461667
Latitude=12.9814853333and Longitude=77.6683491667
Latitude=12.9814783333and Longitude=77.6683485
Latitude=12.9814701667and Longitude=77.6683466667
Latitude=12.981464and Longitude=77.668345
Latitude=12.9814586667and Longitude=77.6683438333
Latitude=12.9814525and Longitude=77.6683428333
Latitude=12.9814458333and Longitude=77.6683421667
Latitude=12.9814395and Longitude=77.6683421667
Latitude=12.9814331667and Longitude=77.668342
Latitude=12.981428and Longitude=77.6683425
Latitude=12.981423and Longitude=77.6683428333
Latitude=12.9814185and Longitude=77.6683431667
Latitude=12.9814146667and Longitude=77.6683436667
Latitude=12.9814095and Longitude=77.6683443333
Latitude=12.9814056667and Longitude=77.6683456667
Latitude=12.981401and Longitude=77.668346
Latitude=12.9813966667and Longitude=77.66834
```

## Ploting the GPS Values over Google Map

## Stream Data Over PubNub

If you haven’t already done so, [sign up for a free PubNub account](https://admin.pubnub.com/) before you begin this step.



## Change directory 

Change directory into the examples directory containing the gps_simpletest.py file and install the PubNub Python SDK.

```
pip3 install pubnub
```

## Import PubNub Package

```
import pubnub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNOperationType, PNStatusCategory
```

## Configure a PubNub instance with your publish/subscribe Keys

```
pnconfig = PNConfiguration()
pnconfig.subscribe_key = "YOUR SUBSCRIBE KEY"
pnconfig.publish_key = "YOUR PUBLISH KEY"
pnconfig.ssl = False
pubnub = PubNub(pnconfig)
```

Then to publish, place a publishing callback somewhere near the beginning of your code. You can write whatever you want for the callback, but we’ll leave it blank as we don’t really need it for now.

```
def publish_callback(result, status):
    pass
    # Handle PNPublishResult and PNStatus
```


Here is where you decide what data you want to publish. Since we are building just a simple GPS tracking device, we’re just going to be dealing with the latitude and longitude coordinates.

When you want to publish multiple variables in one JSON, you must create a dictionary like so:

```
dictionary = {"DATA 1 NAME": gps.DATA1, "DATA 2 NAME": gps.DATA2}
```

So in our case we would write:

```
dictionary = {"latitude": gps.latitude, "longitude": gps.longitude}
```
And then to publish that data, you would format the dictionary like this:

```
pubnub.publish().channel("CHANNEL").message(dictionary).pn_async(publish_callback)
```

It is best to place the dictionary and publishing lines within the “if gps.DATA is not none” to avoid any program failures.


## Visualize your GPS Data with Google Maps

It's time to visualize our GPS data in a way that humans can understand.

We’re just going to create a small HTML page that will grab GPS data from our PubNub channel and graph the data with a geolocation API.

## Google Maps API

The Google Maps API is a universal tool that is not only one of the cheaper APIs for a greater amount of API calls but also has a rich and expansive toolset for developers. The GPS data is not only more accurate than most other APIs, but also has extensive tools such as “ETA” that uses Google’s geographical terrain data.

So if you ever want to build a serious GPS tracking app with PubNub, Google Maps is the way to go.

Image result for google maps api with marker

You’ll first need to get a Google Maps API Key

Once that’s done, create an .html file and copy-paste the code below (explanation of the code is below as well).

```
<!DOCTYPE html>
<html>
  <head>
    <title>Simple Map</title>
    <meta name="viewport" content="initial-scale=1.0">
    <meta charset="utf-8">
    <style>
      /* Always set the map height explicitly to define the size of the div
       * element that contains the map. */
      #map {
        height: 100%;
      }
      /* Optional: Makes the sample page fill the window. */
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
    </style>
    <script src="https://cdn.pubnub.com/sdk/javascript/pubnub.4.23.0.js"></script>
  </head>
  <body>
    <div id="map"></div>
    <script>
  // the smooth zoom function
  function smoothZoom (map, max, cnt) {
      if (cnt >= max) {
          return;
      }
      else {
          z = google.maps.event.addListener(map, 'zoom_changed', function(event){
              google.maps.event.removeListener(z);
              smoothZoom(map, max, cnt + 1);
          });
          setTimeout(function(){map.setZoom(cnt)}, 80); // 80ms is what I found to work well on my system -- it might not work well on all systems
      }
  } 
    var pubnub = new PubNub({
    subscribeKey: "YOUR SUBSCRIBE KEY",
    ssl: true
  });  
  var longitude = 30.5;
  var latitude = 50.5;
  pubnub.addListener({
      message: function(m) {
          // handle message
          var channelName = m.channel; // The channel for which the message belongs
          var channelGroup = m.subscription; // The channel group or wildcard subscription match (if exists)
          var pubTT = m.timetoken; // Publish timetoken
          var msg = m.message; // The Payload
          longitude = msg.longitude;
          latitude = msg.latitude;
          var publisher = m.publisher; //The Publisher
    var myLatlng = new google.maps.LatLng(latitude, longitude);
    var marker = new google.maps.Marker({
        position: myLatlng,
        title:"PubNub GPS"
    });
    // To add the marker to the map, call setMap();
    map.setCenter(marker.position);
    smoothZoom(map, 14, map.getZoom());
    marker.setMap(map);
      },
      presence: function(p) {
          // handle presence
          var action = p.action; // Can be join, leave, state-change or timeout
          var channelName = p.channel; // The channel for which the message belongs
          var occupancy = p.occupancy; // No. of users connected with the channel
          var state = p.state; // User State
          var channelGroup = p.subscription; //  The channel group or wildcard subscription match (if exists)
          var publishTime = p.timestamp; // Publish timetoken
          var timetoken = p.timetoken;  // Current timetoken
          var uuid = p.uuid; // UUIDs of users who are connected with the channel
      },
      status: function(s) {
          var affectedChannelGroups = s.affectedChannelGroups;
          var affectedChannels = s.affectedChannels;
          var category = s.category;
          var operation = s.operation;
      }
  });
  pubnub.subscribe({
      channels: ['ch1'],
  });
      var map;
      function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: latitude, lng: longitude},
          zoom: 8
        });
      }
    </script>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBLuWQHjBa9SMVVDyyqxqTpR2ZwnxwcbGE&callback=initMap"
    async defer></script>
  </body>
</html>
```

This part of the code is responsible for rendering our map on the HTML page.

```
<style>
  /* Always set the map height explicitly to define the size of the div
   * element that contains the map. */
  #map {
    height: 100%;
  }
  /* Optional: Makes the sample page fill the window. */
  html, body {
    height: 100%;
    margin: 0;
    padding: 0;
  }
</style>
```

Just a little below it, we enter a div id tag to tell where we want the map to render:

  //div tag for map[] id
     <div id="map"></div>

Here we simply import the PubNub JS SDK to enable PubNub data streaming for our GPS data:

```
<script src="https://cdn.pubnub.com/sdk/javascript/pubnub.4.23.0.js"></script>
```

We must also import the Google Maps API with this script tag:

```
<script src="https://maps.googleapis.com/maps/api/js?key=YOURAPIKEY&callback=initMap"async defer></script>
```

NOTE: The rest of the code is encapsulated within one script tag, so don’t be alarmed if we jump around in explaining this final part of the code.

In order to stream our data, instantiate a PubNub instance:

```
var pubnub = new PubNub({
    subscribeKey: "YOUR SUBSCRIBE KEY",
    ssl: true
  });
```

Then we instantiate a PubNub listener with the following code.

```
pubnub.addListener({
      message: function(m) {
          // handle message
          var channelName = m.channel; // The channel for which the message belongs
          var channelGroup = m.subscription; // The channel group or wildcard subscription match (if exists)
          var pubTT = m.timetoken; // Publish timetoken
          var publisher = m.publisher; //The Publisher
          
          var msg = m.message; // The Payload
          //extract and save the longitude and latitude data from your incomming PubNub message
          longitude = msg.longitude;
          latitude = msg.latitude;
          
        //Create a new Google Maps instance with updated GPS coordinates
      var myLatlng = new google.maps.LatLng(latitude, longitude);
      //Create a marker instance with the coordinates
      var marker = new google.maps.Marker({
          position: myLatlng,
          title:"PubNub GPS"
      });
      
      //center the map with the maker position
      map.setCenter(marker.position);
      //Optional: create a zooming annimation when the gps changes coordinates
      smoothZoom(map, 14, map.getZoom());
      // To add the marker to the map, call setMap();
      marker.setMap(map);
      },
      presence: function(p) {
          // handle presence
          var action = p.action; // Can be join, leave, state-change or timeout
          var channelName = p.channel; // The channel for which the message belongs
          var occupancy = p.occupancy; // No. of users connected with the channel
          var state = p.state; // User State
          var channelGroup = p.subscription; //  The channel group or wildcard subscription match (if exists)
          var publishTime = p.timestamp; // Publish timetoken
          var timetoken = p.timetoken;  // Current timetoken
          var uuid = p.uuid; // UUIDs of users who are connected with the channel
      },
      status: function(s) {
          var affectedChannelGroups = s.affectedChannelGroups;
          var affectedChannels = s.affectedChannels;
          var category = s.category;
          var operation = s.operation;
      }
  });
```

In order to avoid syntax errors, place a subscriber instance right below the listener.

```
pubnub.subscribe({
      channels: ['YOUR CHANNEL NAME'],
  });
```

As you can see, we open up incoming messages with the following line of code.

```
var msg = m.message; // The Payload
```

And then extract the variables we desire based on the sent JSON.

```
longitude = msg.longitude;
latitude = msg.latitude;
```

We then format the data variables in accordance to a Google Maps object.

```
var myLatlng = new google.maps.LatLng(latitude, longitude);
```
To set a Google marker on our GPS coordinates we create a Google Maps marker object.

```
var marker = new google.maps.Marker({
          position: myLatlng,
          title:"Title of Marker"
      });
```

Then add the marker to your Google Maps object by calling setMap().

```
marker.setMap(map);
```

Of course, it would be nice to center our map on the marker so we can actually see it so we center it on the markers position.

```
map.setCenter(marker.position);
```

This is optional, but if you want to add a smooth zooming animation every time you locate a marker, call a smoothZoom function like so.

```
smoothZoom(map, 14, map.getZoom());
```

And implement the smoothZoom function somewhere.

```
function smoothZoom (map, max, cnt) {
      if (cnt >= max) {
          return;
      }
      else {
          z = google.maps.event.addListener(map, 'zoom_changed', function(event){
              google.maps.event.removeListener(z);
              smoothZoom(map, max, cnt + 1);
          });
          setTimeout(function(){map.setZoom(cnt)}, 80); // 80ms is what I found to work well on my system -- it might not work well on all systems
      }
  } 
```

Lastly we’ll need to initialize the map so we write:

```
var map;
     function initMap() {
       map = new google.maps.Map(document.getElementById('map'), {
         center: {lat: latitude, lng: longitude},
         zoom: 8
       });
     }
```
And set the initial values of your latitude and longitude variables to wherever you want.

```
var longitude = 30.5;
var latitude = 50.5;
```

And that’s it! 

### Fetch the values over Google Map

```
open frontend.html
```

![image](googlemap.png)
