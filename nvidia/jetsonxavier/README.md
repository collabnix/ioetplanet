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

## Identify the Jetson board

```
git clone https://github.com/jetsonhacks/jetsonUtilities
```


```
python3 jetsonInfo.py 
NVIDIA Jetson AGX Xavier [16GB]
 L4T 32.3.1 [ JetPack 4.3 ]
   Ubuntu 18.04.3 LTS
   Kernel Version: 4.9.140-tegra
 CUDA NOT_INSTALLED
   CUDA Architecture: 7.2
 OpenCV version: NOT_INSTALLED
   OpenCV Cuda: NO
 CUDNN: NOT_INSTALLED
 TensorRT: NOT_INSTALLED
 Vision Works: NOT_INSTALLED
 VPI: NOT_INSTALLED
 Vulcan: 1.1.70
xavier@xavier-desktop:~/jetsonUtilities$ 
```


```
sudo -H pip install -U jetson-stats
```

```
sudo -H pip install -U jetson-stats
Collecting jetson-stats
  Downloading https://files.pythonhosted.org/packages/70/57/ce1aec95dd442d94c3bd47fcda77d16a3cf55850fa073ce8c3d6d162ae0b/jetson-stats-3.1.1.tar.gz (85kB)
    100% |████████████████████████████████| 92kB 623kB/s 
Building wheels for collected packages: jetson-stats
  Running setup.py bdist_wheel for jetson-stats ... done
  Stored in directory: /root/.cache/pip/wheels/5e/b0/97/f0f8222e76879bf04b6e8c248154e3bb970e0a2aa6d12388f9
Successfully built jetson-stats
Installing collected packages: jetson-stats
Successfully installed jetson-stats-3.1.1
xavier@xavier-desktop:~/jetsonUtilities$ 
```

```
$jtop
I can't access jetson_stats.service.
Please logout or reboot this board.
```

![image](https://user-images.githubusercontent.com/34368930/132097743-b3698991-f1db-488b-ab9e-c35afc8a1d99.png)

![image](https://user-images.githubusercontent.com/34368930/132097789-01070b08-217e-409e-a8a0-aabe5e67c9fc.png)

![image](https://user-images.githubusercontent.com/34368930/132097801-5916ea54-4ab9-44c4-80e3-44d6e2c01e25.png)




## Running Jtop inside Docker container

```
xavier@xavier-desktop:~$ sudo docker run --rm -it --gpus all \
>                    -v /run/jtop.sock:/run/jtop.sock ajeetraina/jetson-stats-nano jtop
Unable to find image 'ajeetraina/jetson-stats-nano:latest' locally
latest: Pulling from ajeetraina/jetson-stats-nano
595b0fe564bb: Pull complete 
0fe8a6b629fd: Pull complete 
1105f4e4114d: Pull complete 
71e7b9c27f04: Pull complete 
c3ff736867a8: Pull complete 
1b2993689e65: Pull complete 
Digest: sha256:771ecd2ef10755e4ab398f9d230c3a8904c2621fee5bbb1066085c9478caa903
Status: Downloaded newer image for ajeetraina/jetson-stats-nano:latest
docker: Error response from daemon: could not select device driver "" with capabilities: [[gpu]].
ERRO[0020] error waiting for container: context canceled 
```
