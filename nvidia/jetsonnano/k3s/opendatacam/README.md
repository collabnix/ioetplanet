
# Running OpenDatacam on 5 Node K3s Cluster


## Create device plugin DaemonSet

The device plugin is responsible for advertising the nvidia.com/gpu resource on a node (via kubelet).
This needs to be done on the kubernetes node only once. 
Every node with the label cloud.google.com/gke-accelerator then gets automatically a pod from this DaemonSet assigned.

```
pico@pico1:~$ sudo kubectl apply -f https://raw.githubusercontent.com/kubernetes/kubernetes/release-1.14/cluster/addons/device-plugins/nvidia-gpu/daemonset.yaml
[sudo] password for pico: 
daemonset.apps/nvidia-gpu-device-plugin created
```

