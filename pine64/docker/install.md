# Installing Docker on Manjaro-ARM OS running on Pine64 

```
ssh ajeetraina@192.168.1.8
ajeetraina@192.168.1.8's password: 
Welcome to Manjaro-ARM
~~Website: https://manjaro.org
~~Forum:   https://forum.manjaro.org/c/manjaro-arm
~~IRC:     #manjaro-arm on irc.freenode.net
~~Matrix:  #manjaro-arm-public:matrix.org
Last login: Mon Oct  5 09:17:42 2020
[ajeetraina@pine64 ~]$ 

```

## Keeping Manjaro ARM Repository up-to-date

```
 sudo pacman -Syu
```
 
 ## Installing Docker 19.03.12
 
 ```
 pacman -S docker
 ```
 
 ## Initialising Docker
 
 You might have to reboot your system for Docker to get initialise properly
 
 ## Running Docker Service
 
 ```
 systemctl start docker.service
 systemctl enable docker.service
 ```
 
 ## Verifying Docker
 
 ```
 [ajeetraina@pine64 ~]$ sudo docker version
[sudo] password for ajeetraina: 
Client:
 Version:           19.03.12-ce
 API version:       1.40
 Go version:        go1.14.5
 Git commit:        48a66213fe
 Built:             Sat Jul 18 02:40:17 2020
 OS/Arch:           linux/arm64
 Experimental:      false

Server:
 Engine:
  Version:          19.03.12-ce
  API version:      1.40 (minimum version 1.12)
  Go version:       go1.14.5
  Git commit:       48a66213fe
  Built:            Sat Jul 18 02:39:40 2020
  OS/Arch:          linux/arm64
  Experimental:     false
 containerd:
  Version:          v1.4.1.m
  GitCommit:        c623d1b36f09f8ef6536a057bd658b3aa8632828.m
 runc:
  Version:          1.0.0-rc92
  GitCommit:        ff819c7e9184c13b7c2607fe6c30ae19403a7aff
 docker-init:
  Version:          0.18.0
  GitCommit:        fec3683
```


## Installing Docker Compose

```
sudo pacman -S docker-compose
```

```
[ajeetraina@pine64 ~]$ sudo docker-compose version
docker-compose version 1.27.3, build unknown
docker-py version: 4.3.1
CPython version: 3.8.5
OpenSSL version: OpenSSL 1.1.1g  21 Apr 2020
[ajeetraina@pine64 ~]$ 
```


 
