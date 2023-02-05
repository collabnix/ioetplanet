# Getting started with Docker on NVIDIA Jetson Xavier AGX

## Installing Docker

By default, the latest version of Docker is shipped with the development platform. You can verify it by running the below command:

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


## Clone the repository

```
git clone https://github.com/jetsonhacks/jetsonUtilities
```

## Execute the Python Script:

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

## Installing Jtop

Lucky You! I have created a Docker Image for Jetson Nano few weeks back that you can leverage on Xavier developer kit too. Check this out:

```
docker run --rm -it --gpus all -v /run/jtop.sock:/run/jtop.sock ajeetraina/jetson-stats-nano jtop
```

If you want to keep it simple and new to Docker, no worries. Try to install the Python module and you are all good to go.

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

Don’t get surprise if you encounter the below message. Reboot your system and re-run the command:

```
$jtop
I can't access jetson_stats.service.
Please logout or reboot this board.
```

![image](https://user-images.githubusercontent.com/313480/216812735-dd7e7cb6-3bfc-47a6-a757-5efe825d92e1.png)


## Using Jtop to see the GPU and CPU details

![image](https://user-images.githubusercontent.com/313480/216812747-1f1c107f-27e5-4fef-9a9b-b14146768aee.png)


## Displaying Xavier Information

![image](https://user-images.githubusercontent.com/313480/216812754-3dd7d4c7-f166-4a50-9290-6b656a55db0e.png)


## Displaying the Xavier Release Info

```
xavier@xavier-desktop:~$ jetson_release -v
 - NVIDIA Jetson AGX Xavier [16GB]
   * Jetpack 4.3 [L4T 32.3.1]
   * NV Power Mode: MODE_15W - Type: 2
   * jetson_stats.service: active
 - Board info:
   * Type: AGX Xavier [16GB]
   * SOC Family: tegra194 - ID:25
   * Module: P2888-0001 - Board: P2822-0000
   * Code Name: galen
   * CUDA GPU architecture (ARCH_BIN): 7.2
   * Serial Number: 1420921055981
 - Libraries:
   * CUDA: NOT_INSTALLED
   * cuDNN: NOT_INSTALLED
   * TensorRT: NOT_INSTALLED
   * Visionworks: NOT_INSTALLED
   * OpenCV: NOT_INSTALLED compiled CUDA: NO
   * VPI: NOT_INSTALLED
   * Vulkan: 1.1.70
 - jetson-stats:
   * Version 3.1.1
   * Works on Python 2.7.17
xavier@xavier-desktop:~$ 
```

