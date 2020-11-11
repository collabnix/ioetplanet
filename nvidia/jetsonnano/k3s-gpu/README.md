# Using K3s with GPU


If you run the below command on your Jetson Nano board and see the below result, then it means you haven't enabled Docker Engine with GPU:

```
sudo docker info | grep Runtime
  Runtimes: nvidia runc
 Default Runtime: runc
```

This is expected. runc in its current state isn’t GPU-aware, or at least, not aware enough to natively integrate with Nvidia GPU’s, but the Nvidia runtime is. 

# Configuring Docker Daemon for NVIDIA

Open /etc/docker/daemon.json and add the below content:

```

```
{
    "default-runtime": "nvidia",
    "runtimes": {
        "nvidia": {
            "path": "/usr/bin/nvidia-container-runtime",
            "runtimeArgs": []
        }
    }
}
```
## Restarting Docker Daemon

```
sudo systemctl restart docker
```


## Verifying 

```
pico@pico1:~$ sudo docker info | grep Runtime
 Runtimes: runc nvidia
 Default Runtime: nvidia
pico@pico1:~$ 
```


