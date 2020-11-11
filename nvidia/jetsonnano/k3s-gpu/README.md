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

## Running K3s using Docker

```
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="--docker" sh -s -
[INFO]  Finding release for channel stable
[INFO]  Using v1.19.3+k3s2 as release
[INFO]  Downloading hash https://github.com/rancher/k3s/releases/download/v1.19.3+k3s2/sha256sum-arm64.txt
[INFO]  Skipping binary downloaded, installed k3s matches hash
[INFO]  Skipping /usr/local/bin/kubectl symlink to k3s, already exists
[INFO]  Skipping /usr/local/bin/crictl symlink to k3s, already exists
[INFO]  Skipping /usr/local/bin/ctr symlink to k3s, command exists in PATH at /usr/bin/ctr
[INFO]  Creating killall script /usr/local/bin/k3s-killall.sh
[INFO]  Creating uninstall script /usr/local/bin/k3s-uninstall.sh
[INFO]  env: Creating environment file /etc/systemd/system/k3s.service.env
[INFO]  systemd: Creating service file /etc/systemd/system/k3s.service
[INFO]  systemd: Enabling k3s unit
Created symlink /etc/systemd/system/multi-user.target.wants/k3s.service → /etc/systemd/system/k3s.service.
[INFO]  systemd: Starting k3s
```

