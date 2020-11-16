# Setting up K3s Cluster on 5 Node Jetson Nano 

## Prerequisite


## Hardware Setup

- 4x Jetson Nano 4GB/2GB


```
pico1 - 192.168.1.160
pico2 - 192.168.1.161
pico3 - 192.168.1.162
pico4 - 192.168.1.163
```


- Jetson Nano SD Card Image flashed


## Software Setup

Login to Jetson Nano and install ```curl```
```
apt install curl
```

Ensure that each of the Jetson Nano boxes have ```/etc/hosts``` entries on each of the nodes.

## Setting up K3s Master Node

```
pico@pico1:~$ curl -sfL https://get.k3s.io | sh -
[INFO]  Finding release for channel stable
[INFO]  Using v1.19.3+k3s2 as release
[INFO]  Downloading hash https://github.com/rancher/k3s/releases/download/v1.19.3+k3s2/sha256sum-arm64.txt
[INFO]  Downloading binary https://github.com/rancher/k3s/releases/download/v1.19.3+k3s2/k3s-arm64
[INFO]  Verifying binary download
[INFO]  Installing k3s to /usr/local/bin/k3s
[INFO]  Creating /usr/local/bin/kubectl symlink to k3s
[INFO]  Creating /usr/local/bin/crictl symlink to k3s
[INFO]  Skipping /usr/local/bin/ctr symlink to k3s, command exists in PATH at /usr/bin/ctr
[INFO]  Creating killall script /usr/local/bin/k3s-killall.sh
[INFO]  Creating uninstall script /usr/local/bin/k3s-uninstall.sh
[INFO]  env: Creating environment file /etc/systemd/system/k3s.service.env
[INFO]  systemd: Creating service file /etc/systemd/system/k3s.service
[INFO]  systemd: Enabling k3s unit
Created symlink /etc/systemd/system/multi-user.target.wants/k3s.service → /etc/systemd/system/k3s.service.
[INFO]  systemd: Starting k3s
```

## Verify K3s Nodes

```
sudo k3s kubectl get node -o wide
NAME    STATUS   ROLES    AGE   VERSION        INTERNAL-IP     EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION   CONTAINER-RUNTIME
pico1   Ready    master   70s   v1.19.3+k3s2   192.168.1.160   <none>        Ubuntu 18.04.5 LTS   4.9.140-tegra    containerd://1.4.0-k3s1
```


## Listing K3s Nodes

```
sudo k3s kubectl get node
NAME    STATUS   ROLES    AGE    VERSION
pico1   Ready    master   101s   v1.19.3+k3s2
```

## Getting K3s Cluster Information

```
sudo k3s kubectl cluster-info
Kubernetes master is running at https://127.0.0.1:6443
CoreDNS is running at https://127.0.0.1:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
Metrics-server is running at https://127.0.0.1:6443/api/v1/namespaces/kube-system/services/https:metrics-server:/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
pico@pico1:~$ 
```

## Getting Detailed Information

```
pico@pico1:~$ sudo k3s kubectl get all --all-namespaces
NAMESPACE     NAME                                         READY   STATUS      RESTARTS   AGE
kube-system   pod/metrics-server-7b4f8b595-74bzc           1/1     Running     0          2m24s
kube-system   pod/local-path-provisioner-7ff9579c6-nwjwx   1/1     Running     0          2m24s
kube-system   pod/coredns-66c464876b-s2qw4                 1/1     Running     0          2m24s
kube-system   pod/helm-install-traefik-8zk79               0/1     Completed   0          2m25s
kube-system   pod/svclb-traefik-kz94r                      2/2     Running     0          105s
kube-system   pod/traefik-5dd496474-wg74c                  1/1     Running     0          106s

NAMESPACE     NAME                         TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)                      AGE
default       service/kubernetes           ClusterIP      10.43.0.1       <none>          443/TCP                      2m41s
kube-system   service/kube-dns             ClusterIP      10.43.0.10      <none>          53/UDP,53/TCP,9153/TCP       2m39s
kube-system   service/metrics-server       ClusterIP      10.43.45.77     <none>          443/TCP                      2m38s
kube-system   service/traefik-prometheus   ClusterIP      10.43.75.182    <none>          9100/TCP                     106s
kube-system   service/traefik              LoadBalancer   10.43.125.136   192.168.1.160   80:30315/TCP,443:31527/TCP   106s

NAMESPACE     NAME                           DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
kube-system   daemonset.apps/svclb-traefik   1         1         1       1            1           <none>          106s

NAMESPACE     NAME                                     READY   UP-TO-DATE   AVAILABLE   AGE
kube-system   deployment.apps/metrics-server           1/1     1            1           2m38s
kube-system   deployment.apps/local-path-provisioner   1/1     1            1           2m38s
kube-system   deployment.apps/coredns                  1/1     1            1           2m39s
kube-system   deployment.apps/traefik                  1/1     1            1           106s

NAMESPACE     NAME                                               DESIRED   CURRENT   READY   AGE
kube-system   replicaset.apps/metrics-server-7b4f8b595           1         1         1       2m25s
kube-system   replicaset.apps/local-path-provisioner-7ff9579c6   1         1         1       2m25s
kube-system   replicaset.apps/coredns-66c464876b                 1         1         1       2m25s
kube-system   replicaset.apps/traefik-5dd496474                  1         1         1       106s

NAMESPACE     NAME                             COMPLETIONS   DURATION   AGE
kube-system   job.batch/helm-install-traefik   1/1           41s        2m38s
pico@pico1:~$ 
```

## Testing NGINX Pod


```
sudo k3s kubectl run mynginx --image=nginx --replicas=3 --port=80
Flag --replicas has been deprecated, has no effect and will be removed in the future.
pod/mynginx created
pico@pico1:~$ 
```

## Retrieving Nginx Pod

```
sudo k3s kubectl get po
NAME      READY   STATUS    RESTARTS   AGE
mynginx   1/1     Running   0          44s
```

## Adding the first K3s Worker Node(Jetson Nano)


### Preparing Worker Nodes

- Installing ```curl``` CLI on Jetson Nano


```
pico@pico2:~$ sudo curl -sfL https://get.k3s.io | K3S_URL=https://pico1:6443 K3S_TOKEN=K10ddc558bd2734738e45ffc9ad1a149203910e990de39aaf49c5c39b5ca0017c4c::server:39c8376b20e2d075b7e0796452b063ba  sh -
[INFO]  Finding release for channel stable
[INFO]  Using v1.19.3+k3s2 as release
[INFO]  Downloading hash https://github.com/rancher/k3s/releases/download/v1.19.3+k3s2/sha256sum-arm64.txt
[INFO]  Skipping binary downloaded, installed k3s matches hash
[INFO]  Skipping /usr/local/bin/kubectl symlink to k3s, already exists
[INFO]  Skipping /usr/local/bin/crictl symlink to k3s, already exists
[INFO]  Skipping /usr/local/bin/ctr symlink to k3s, command exists in PATH at /usr/bin/ctr
[INFO]  Creating killall script /usr/local/bin/k3s-killall.sh
[INFO]  Creating uninstall script /usr/local/bin/k3s-agent-uninstall.sh
[INFO]  env: Creating environment file /etc/systemd/system/k3s-agent.service.env
[INFO]  systemd: Creating service file /etc/systemd/system/k3s-agent.service
[INFO]  systemd: Enabling k3s-agent unit
Created symlink /etc/systemd/system/multi-user.target.wants/k3s-agent.service → /etc/systemd/system/k3s-agent.service.
[INFO]  systemd: Starting k3s-agent
```

```
sudo k3s kubectl get nodes
NAME    STATUS   ROLES    AGE   VERSION
pico1   Ready    master   18h   v1.19.3+k3s2
pico2   Ready    <none>   12s   v1.19.3+k3s2
```


```
pico@pico1:~$ sudo k3s kubectl get nodes
[sudo] password for pico: 
NAME    STATUS   ROLES    AGE     VERSION
pico1   Ready    master   19h     v1.19.3+k3s2
pico2   Ready    <none>   13m     v1.19.3+k3s2
pico3   Ready    <none>   8m57s   v1.19.3+k3s2
pico4   Ready    <none>   39s     v1.19.3+k3s2
```

## Running Portainer on Jetson Nano Cluster

```
pico@pico1:~$ sudo  curl -LO https://raw.githubusercontent.com/portainer/portainer-k8s/master/portainer-nodeport.yaml
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1421  100  1421    0     0   3229      0 --:--:-- --:--:-- --:--:--  3236
```

```
pico@pico1:~$ sudo kubectl apply -f portainer-nodeport.yaml
namespace/portainer created
serviceaccount/portainer-sa-clusteradmin created
Warning: rbac.authorization.k8s.io/v1beta1 ClusterRoleBinding is deprecated in v1.17+, unavailable in v1.22+; use rbac.authorization.k8s.io/v1 ClusterRoleBinding
clusterrolebinding.rbac.authorization.k8s.io/portainer-crb-clusteradmin created
service/portainer created
deployment.apps/portainer created
pico@pico1:~$ 
```

```
pico@pico1:~$ sudo k3s kubectl get po,svc,deploy -n portainer
NAME                             READY   STATUS    RESTARTS   AGE
pod/portainer-5fbd6bb5d8-dxgp4   1/1     Running   0          53s

NAME                TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)                         AGE
service/portainer   NodePort   10.43.227.233   <none>        9000:30777/TCP,8000:30776/TCP   53s

NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/portainer   1/1     1            1           53s
pico@pico1:~$ 
```
