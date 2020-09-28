# Getting Started with NVIDIA Jetson Nano




## Table of Contents

1. [Intent](#Intent)
2. [Hardware](#hardware)
3. [Software](#Software)
4. [Preparing Your Jetson Nano](#preparing-your-jetson-nano)
   - [Flashing SD card image](#1-flashing-sd-card-image)
   - [Vefifying Docker Binaries](#2-verifying-if-it-is-shipped-with-docker-binaries)


## Intent

Everything and anything you want to know about NVIDIA Jetson Nano, Docker & K3s support

## Hardware

- Jetson Nano
- A Camera Module
- A 5V 4Ampere Charger
- 64GB SD card

## Software

- Jetson SD card image from https://developer.nvidia.com/embedded/downloads
- Etcher software installed on your system

## Preparing Your Jetson Nano

### 1. Preparing Your Raspberry Pi Flashing Jetson SD Card Image

 - Unzip the SD card image
 - Insert SD card into your system. 
 - Bring up Etcher tool and select the target SD card to which you want to flash the image.

![My Image](https://github.com/collabnix/ioetplanet/blob/master/nvidia/jetsonnano/Screenshot%202020-09-16%20at%2010.29.02%20AM.png)

### 2. Verifying if it is shipped with Docker Binaries

```
ajeetraina@ajeetraina-desktop:~$ sudo docker version
[sudo] password for ajeetraina: 
Client:
 Version:           19.03.6
 API version:       1.40
 Go version:        go1.12.17
 Git commit:        369ce74a3c
 Built:             Fri Feb 28 23:47:53 2020
 OS/Arch:           linux/arm64
 Experimental:      false

Server:
 Engine:
  Version:          19.03.6
  API version:      1.40 (minimum version 1.12)
  Go version:       go1.12.17
  Git commit:       369ce74a3c
  Built:            Wed Feb 19 01:06:16 2020
  OS/Arch:          linux/arm64
  Experimental:     false
 containerd:
  Version:          1.3.3-0ubuntu1~18.04.2
  GitCommit:        
 runc:
  Version:          spec: 1.0.1-dev
  GitCommit:        
 docker-init:
  Version:          0.18.0
  GitCommit:       
```

### 3. Checking Docker runtime 

Starting with JetPack 4.2, NVIDIA has introduced a container runtime with Docker integration. This custom runtime enables Docker containers to access the underlying GPUs available in the Jetson family.

```
pico@pico1:/tmp/docker-build$ sudo nvidia-docker version
NVIDIA Docker: 2.0.3
Client:
 Version:           19.03.6
 API version:       1.40
 Go version:        go1.12.17
 Git commit:        369ce74a3c
 Built:             Fri Feb 28 23:47:53 2020
 OS/Arch:           linux/arm64
 Experimental:      false

Server:
 Engine:
  Version:          19.03.6
  API version:      1.40 (minimum version 1.12)
  Go version:       go1.12.17
  Git commit:       369ce74a3c
  Built:            Wed Feb 19 01:06:16 2020
  OS/Arch:          linux/arm64
  Experimental:     false
 containerd:
  Version:          1.3.3-0ubuntu1~18.04.2
  GitCommit:        
 runc:
  Version:          spec: 1.0.1-dev
  GitCommit:        
 docker-init:
  Version:          0.18.0
  GitCommit:
```

## Installing Docker Compose on NVIDIA Jetson Nano

Jetson Nano doesnt come with Docker Compose installed by default. You will need to install it first:

```
export DOCKER_COMPOSE_VERSION=1.27.4
sudo apt-get install libhdf5-dev
sudo apt-get install libssl-dev
sudo pip3 install docker-compose=="${DOCKER_COMPOSE_VERSION}"
apt install python3
apt install python3-pip
pip install docker-compose
```

```
docker-compose version
docker-compose version 1.26.2, build unknown
docker-py version: 4.3.1
CPython version: 3.6.9
OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
```




Next, add default runtime for NVIDIA:

Edit /etc/docker/daemon.json

```
{
    "runtimes": {
        "nvidia": {
            "path": "/usr/bin/nvidia-container-runtime",
            "runtimeArgs": []
        }
    },

    "default-runtime": "nvidia",
    "node-generic-resources": [ "NVIDIA-GPU=0" ]
}

```

Restart the Docker Daemon

```
systemctl restart docker
```

