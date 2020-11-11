# Installing K3s

```
[ajeetraina@pine64 ~]$ curl -sfL https://get.k3s.io | sh -
[sudo] password for ajeetraina: 
[INFO]  Finding release for channel stable
[INFO]  Using v1.18.9+k3s1 as release
[INFO]  Downloading hash https://github.com/rancher/k3s/releases/download/v1.18.9+k3s1/sha256sum-arm64.txt
[INFO]  Downloading binary https://github.com/rancher/k3s/releases/download/v1.18.9+k3s1/k3s-arm64
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
[ajeetraina@pine64 ~]$ 
```

```
[ajeetraina@pine64 ~]$ sudo  curl -LO https://raw.githubusercontent.com/portainer/portainer-k8s/master/portainer-nodeport.yaml
[sudo] password for ajeetraina: 
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1421  100  1421    0     0   1546      0 --:--:-- --:--:-- --:--:--  1544

```

```
[ajeetraina@pine64 ~]$ sudo kubectl apply -f portainer-nodeport.yaml
namespace/portainer created
serviceaccount/portainer-sa-clusteradmin created
clusterrolebinding.rbac.authorization.k8s.io/portainer-crb-clusteradmin created
service/portainer created
deployment.apps/portainer created
[ajeetraina@pine64 ~]$
```

```
[ajeetraina@pine64 ~]$ sudo kubectl get svc -n portainer


NAME        TYPE       CLUSTER-IP    EXTERNAL-IP   PORT(S)                         AGE
portainer   NodePort   10.43.9.186   <none>        9000:30777/TCP,8000:30776/TCP   114s
```


```
pico@pico1:~$ sudo k3s kubectl describe  po -n portainer
Name:         portainer-5fbd6bb5d8-dxgp4
Namespace:    portainer
Priority:     0
Node:         pico2/192.168.1.161
Start Time:   Tue, 10 Nov 2020 22:37:55 -0700
Labels:       app=app-portainer
              pod-template-hash=5fbd6bb5d8
Annotations:  <none>
Status:       Running
IP:           10.42.1.3
IPs:
  IP:           10.42.1.3
Controlled By:  ReplicaSet/portainer-5fbd6bb5d8
Containers:
  portainer:
    Container ID:   containerd://70d7a96eaaa5aaf338194ceaaf858d3e2ce2ed74390e17cbceaef9cefdccc092
    Image:          portainerci/portainer:develop
    Image ID:       docker.io/portainerci/portainer@sha256:31ce431595a4e8223e07e992a5d9d2412c05191355723d56d542c08ff64c971f
    Port:           9000/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Tue, 10 Nov 2020 22:38:07 -0700
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from portainer-sa-clusteradmin-token-g9qmz (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  portainer-sa-clusteradmin-token-g9qmz:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  portainer-sa-clusteradmin-token-g9qmz
    Optional:    false
QoS Class:       BestEffort
Node-Selectors:  <none>
Tolerations:     node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                 node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  4m40s  default-scheduler  Successfully assigned portainer/portainer-5fbd6bb5d8-dxgp4 to pico2
  Normal  Pulling    4m39s  kubelet            Pulling image "portainerci/portainer:develop"
  Normal  Pulled     4m28s  kubelet            Successfully pulled image "portainerci/portainer:develop" in 10.98939761s
  Normal  Created    4m28s  kubelet            Created container portainer
  Normal  Started    4m28s  kubelet            Started container portainer
  ```
