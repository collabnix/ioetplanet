# Support for GPU under Docker Compose 


## Pre-requisite:

- Install Docker 20.x

```
sudo curl -sSL https://get.docker.com/ | sh
```


```
sudo docker version
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
  Version:          20.10.3
  API version:      1.41 (minimum version 1.12)
  Go version:       go1.13.15
  Git commit:       46229ca
  Built:            Fri Jan 29 14:31:49 2021
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
pico@pico1:~$ 
```

## Installing Docker Compose 1.28.2

```
#!/bin/bash
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install curl python3-pip libffi-dev python-openssl libssl-dev zlib1g-dev gcc g++ make -y
curl -sSL https://get.docker.com/ | sh
sudo snap install rustup --classic
sudo apt install rustc
sudo pip3 install docker-compose
sudo docker-compose --version
```


```
sudo docker-compose version
docker-compose version 1.28.2, build unknown
docker-py version: 4.4.2
CPython version: 3.6.9
OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
```


