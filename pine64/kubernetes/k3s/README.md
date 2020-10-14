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

