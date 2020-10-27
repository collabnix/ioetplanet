# RDP (Remote Desktop) with JETSON NANO


##  Steps


## Install xrdp

```
$ sudo apt install xrdp -y 
```

## Install xfce4 ( compatible with ubuntu xrdp)

```
$ sudo apt install xfce4 xfce4-terminal -y
```

## Setting

```
$ cp -p ~ / .xsession ~ / .xsession.org
$ echo xfce4-session > ~ / .xsession
$ sudo cp -p /etc/xrdp/startwm.sh /etc/xrdp/startwm.sh.org
$ sudo nano /etc/xrdp/startwm.sh
```

Fixed startwm.sh

Among the contents of the file, the last two lines commented out and, to append a `startxfce4` the subsequent line.

```
(... omitted)
 #test -x / etc / X11 / Xsession && exec / etc / X11 / Xsession 
#exec / bin / sh / etc / X11 / Xsession
startxfce4
````
## Start xrdp

```
$ sudo service xrdp restart
```

With the steps up to this point, you can access the JETSON NANO X environment from the RDP client on Windows .
