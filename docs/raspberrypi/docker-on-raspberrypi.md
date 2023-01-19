# Install Docker on Rasperry Pi


Raspberry Pi boards today are not just limited to hobbyists and makers. It is heavily used in the IoT industry as a preferable solution for Linux Edge computing. The Raspberry Pi is a tiny computer about the size of a deck of cards. It uses what’s called a system on a chip, which integrates the CPU and GPU in a single integrated circuit, with the RAM, USB ports, and other components soldered onto the board for an all-in-one package. One can use Raspberry Pi to learn programming skills, build hardware projects, do home automation, implement Kubernetes clusters and Edge computing, and even use them in industrial applications. 

Docker support for Raspberry Pi was introduced for the first time in 2016 with v1.12 release. At the same time, Rancher community introduced a lightweight Kubernetes distribution(a.k.a. K3s) for Pi box. K3s is a brand new distribution of Kubernetes that is designed for teams that need to deploy applications quickly and reliably to resource-constrained environments. K3s is a Certified Kubernetes distribution designed for production workloads in unattended, resource-constrained, remote locations or inside IoT appliances.


## Why Docker & Kubernetes on IoT devices?

Today many organizations are going through a digital transformation process. Digital transformation is the integration of digital technology into almost all areas of a business, fundamentally changing how you operate and deliver value to customers. It’s basically a cultural change.  The common goal for all these organization is to change how they connect with their customers, suppliers and partners. These organizations are taking advantage of innovations offered by technologies such as IoT platforms, big data analytics, or machine learning to modernize their enterprise IT and OT systems. They realize that the complexity of development and deployment of new digital products require new development processes. Consequently, they turn to agile development and infrastructure tools such as Kubernetes.


Docker containers & Kubernetes are an excellent choice for deploying complex software to the Edge. The reasons are listed below:

- Containers are awesome
- Consistent across a wide variety of Infrastructure
- Capable of standalone or clustered operations
- Easy to upgrade and/or replace containers
- Support for different infrastructure configs(storage,CPU etc.)
- Strong Ecosystem(Monitoring, logging, CI, management etc.)
 

In the first part of this blog post, I will show you how to install the latest version of Docker on the Raspberry Pi board in 5 Minutes.

## Hardware:

- Raspberry Pi 4 ( You can order it from Amazon in case you are in India for $35)
- Micro-SD card reader ( I got it from here )
- Any Windows or Linux Desktop or Laptop
- HDMI cable ( I used the HDMI cable of my plasma TV)
- Internet Connectivity(Wifi/Broadband/Tethering using Mobile) – to download Docker 1.12.1 package
- Keyboard & mouse connected to Pi’s USB ports
- Raspberry Pi OS (previously called Raspbian) is an official operating system for all models of the Raspberry Pi. We will be using Raspberry Pi Imager for an easy way to install Raspberry Pi OS on top of Raspberry Pi:

Visit https://www.raspberrypi.org/downloads/raspberry-pi-os/ and download Raspberry Pi OS by running the below CLI:


In case you are in hurry, just run the below command and you should be good to go:

```
wget https://downloads.raspberrypi.org/raspios_full_armhf_latest﻿
```

## Using Raspberry Pi Imager

Next, we will be installing Raspberry Pi Imager. You can download via https://www.raspberrypi.org/blog/raspberry-pi-imager-imaging-utility/


All you need to do is choose the right operating system and SD card, and it should be able to flash OS on your SD card.


Click “Write” and it’s time to grab a coffee.


Once the write is successful, you can remove the SD card from card reader and then insert it into Raspberry Pi SD card slot.


SSH to Raspberry Pi nodes

```
$ssh pi@192.168.1.7$ssh pi @192.168.1.4
pi@raspberrypi:~ $ uname -arn
Linux raspberrypi 4.19.118-v7+ #1311 SMP Mon Apr 27 14:21:24 BST 2022 armv7l GNU/Linuxpi@raspberrypi:~ $
```

## Step #2: Installing Docker 20.10.20 on each Pi nodes

```
sudo curl -sSL https://get.docker.com/ | sh
pi@raspi2:~ $ docker version
Client: Docker Engine - Community 
Version:           20.10.20 
API version:       1.41 
Go version:        go1.12.10 
Git commit:        baeda1f 
Built:             Tue Oct 25 18:01:18 2022 
OS/Arch:           linux/arm 
Experimental:      false

Server: Docker Engine - Community Engine:  
Version:          20.10.20  
API version:      1.41 (minimum version 1.12)  
Go version:       go1.18.7  
Git commit:       3056208  
Built:            Tue Oct 25 18:01:18 2022  
OS/Arch:          linux/arm  
Experimental:     false 
containerd:
  Version:          1.6.9
  GitCommit:        1c90a442489720eec95342e1789ee8a5e1b9536f
 runc:
  Version:          1.1.4
  GitCommit:        v1.1.4-0-g5fd4c4d
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
```

## Running Nginx Docker container

```
pi@raspi2:~ $ docker run -d -p 80:80 nginx
pi@raspi2:~ $ docker psCONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                NAMESd7055f45bf23        nginx               "/docker-entrypoint.…"   2 minutes ago       Up About a minute   0.0.0.0:80->80/tcp   silly_maxwellpi@raspi2:~ $
```

