## Getting Started with Jetson AGX Xavier

The NVIDIA® Jetson AGX Xavier™ Developer Kit provides a full-featured development platform designed to get you up and running quickly. The included carrier board
exposes many standard hardware interfaces, enabling a highly flexible and extensible platform for rapid prototyping. NVIDIA JetPack SDK supports both your developer kit and host development platform

Jetson AGX Xavier module with thermal solution:

-  Reference carrier board
- 65W power supply with AC cord
- Type C to Type A cable (USB 3.1 Gen2)
- Type C to Type A adapter (USB 3.1 Gen 1)


## Installing Docker

```
xavier@xavier-desktop:~$ sudo docker version
[sudo] password for xavier: 
Client: Docker Engine - Community
 Version:           20.10.8
 API version:       1.41
 Go version:        go1.16.6
 Git commit:        3967b7d
 Built:             Fri Jul 30 19:54:37 2021
 OS/Arch:           linux/arm64
 Context:           default
 Experimental:      true

Server: Docker Engine - Community
 Engine:
  Version:          20.10.8
  API version:      1.41 (minimum version 1.12)
  Go version:       go1.16.6
  Git commit:       75249d8
  Built:            Fri Jul 30 19:52:46 2021
  OS/Arch:          linux/arm64
  Experimental:     false
 containerd:
  Version:          1.4.9
  GitCommit:        e25210fe30a0a703442421b0f60afac609f950a3
 runc:
  Version:          1.0.1
  GitCommit:        v1.0.1-0-g4144b63
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
xavier@xavier-desktop:~$ 
```

