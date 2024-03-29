# Getting Started with Rasperry Pi


The Raspberry Pi is a small, low-cost computer developed by the Raspberry Pi Foundation in the United Kingdom. It is intended to promote the teaching of basic computer science in schools and developing countries. The Raspberry Pi is about the size of a credit card and can be used for a variety of tasks including programming, web browsing, and playing videos. It runs on a Linux-based operating system and can be connected to a monitor, keyboard, and mouse to use as a desktop computer, or it can be used with a variety of accessories to control hardware or interact with the internet.


![image](https://user-images.githubusercontent.com/34368930/213512727-55a6c943-b272-4ed8-a105-42ae3cb212ae.png)


The Raspberry Pi is a low-cost, credit-card sized computer that plugs into a computer monitor or TV, and uses a standard keyboard and mouse. It is a capable little device that enables people of all ages to explore computing, and to learn how to program in languages like Scratch and Python. It's also used for a variety of DIY projects and as a media center, retro gaming console, and general-purpose computer. Additionally, it can be used for various purposes such as Robotics, home automation, and IoT projects, etc.

## Hardware:

- Raspberry Pi 4 ( You can order it from Amazon in case you are in India for $35)
- Micro-SD card reader ( I got it from here )
- Any Windows or Linux Desktop or Laptop
- HDMI cable ( I used the HDMI cable of my plasma TV)
- Internet Connectivity(Wifi/Broadband/Tethering using Mobile) – to download Docker 1.12.1 package
- Keyboard & mouse connected to Pi’s USB ports
- Raspberry Pi OS (previously called Raspbian) is an official operating system for all models of the Raspberry Pi. We will be using Raspberry Pi Imager for an easy way to install Raspberry Pi OS on top of Raspberry Pi:


Insert the microSD card into your Pi box. Now connect the HDMI cable  from one end of Pi’s HDMI slot to your TV or display unit and mobile charger(recommended 5.1V@1.5A) as shown:

![image](https://user-images.githubusercontent.com/34368930/213512832-43cf2b50-4616-459a-bf07-25f8ce8ca131.png)


Visit https://www.raspberrypi.org/downloads/raspberry-pi-os/ and download Raspberry Pi OS by running the below CLI:

![image](https://user-images.githubusercontent.com/34368930/213496059-42b7a361-4d3e-4cad-a9a5-0d40355bd305.png)

Visit https://www.raspberrypi.org/downloads/raspberry-pi-os/ and download Raspberry Pi OS by running the below CLI:


In case you are in hurry, just run the below command and you should be good to go:

```
wget https://downloads.raspberrypi.org/raspios_full_armhf_latest﻿
```

## Using Raspberry Pi Imager

Next, we will be installing Raspberry Pi Imager. You can download via https://www.raspberrypi.org/blog/raspberry-pi-imager-imaging-utility/

![image](https://user-images.githubusercontent.com/34368930/213496144-ab75ac09-9825-4c0f-ba9b-362b421107bb.png)



All you need to do is choose the right operating system and SD card, and it should be able to flash OS on your SD card.

![image](https://user-images.githubusercontent.com/34368930/213496175-1769771c-21e2-47d8-9dfb-e2f0930bac90.png)


Click “Write” and it’s time to grab a coffee.

![image](https://user-images.githubusercontent.com/34368930/213496214-9e30a0d3-a081-490f-baa5-ae620cf3539e.png)



Once the write is successful, you can remove the SD card from card reader and then insert it into Raspberry Pi SD card slot.

![image](https://user-images.githubusercontent.com/34368930/213496254-bad1b6d7-41af-4852-896d-ef2334136bff.png)


SSH to Raspberry Pi nodes

```
$ssh pi @192.168.1.4
pi@raspberrypi:~ $ uname -arn
Linux raspberrypi 4.19.118-v7+ #1311 SMP Mon Apr 27 14:21:24 BST 2022 armv7l GNU/Linuxpi@raspberrypi:~ $
```
