# Curated List of Raspberry Pi Resources

Do you want to get started with Raspberry Pi? This is a right place to be.

# Pi 101


<details> 
  <summary>What is Raspberry Pi? </summary>
  Raspberry Pi is credit-card sized computer system.

  </table>
</details>

<details> 
  <summary>What are the components of Raspiberry Pi 3 Model B? </summary>
  
  Its components are listed below:<br>
  - USB Port x4<br>
  - LAN port<br>
  - In-built WiFi Modubr<br>
  - Display Port<br>
  - HDMI Port for Video Output<br>
  - Charging Port<br>
  - Memory Card<br>
  - Audio & Video Jack<br>
  - MicroSD Slot<br>
  - On-board Bluetooth 4.1 WiFI<br>
  GPIO Pins<br>
  ![My Image](https://github.com/collabnix/raspberrypi/blob/master/images/IMG_20200829_124256.jpg)
  </table>
  
</details>

<details> 
  <summary>How to connect Raspberry Pi to a Monitor? </summary>
  Using HDMI cable
  
![My Image](https://github.com/collabnix/raspberrypi/blob/master/images/IMG_20200829_125708.jpg)


  </table>
</details>


<details> 
  <summary>Which OS does Raspberry Pi run? </summary>
  Raspbian OS

  </table>
</details>

<details> 
  <summary>How to setup a static IP on Raspberry Pi?</summary>


* Open DHCP config for editing

```sh
sudo vim /etc/dhcpcd.conf
```

* Add your network interface at the top (run `route -n` to check yours)


```sh
# eth0 or whatever interface you use
interface wlan0

# This will always be your IP when you connect to this gateway
static ip_address=192.168.1.99

# Default gateway IP
static routers=192.168.1.1

# Space separated list of DNS servers
# The ones added here are Cloudflare servers
static domain_name_servers=1.1.1.1 1.0.0.1
```

* Save and reboot!

  </table>
</details>


<details> 
  <summary>How to access Raspberry Pi from an external network?</summary>
  You need to go into your router settings and set up port forwarding to the static IP of your raspberry pi, which you can get by running the following command:
  `hostname -I`

If you want to ssh into your rpi from external network then use the static IP and port 22, if any other service then use the same IP with the port of your choice.

  </table>
</details>



<details> 
  <summary>How to setup SSH in raspberry Pi?</summary>

* Run the following command and enable ssh:

```sh
sudo raspi-config
```

* Get your local IP

```sh
hostname -I

# or
ip addr | grep 192.168
```

* Go to raspberry PI and generate the SSH key pair (id_rsa and id_rsa.pub)

```sh
ssh-keygen -t rsa
```

* Add the key in known_hosts

```sh
cat id_rsa.pub >> ~/.ssh/known_hosts
```

* Do not keep the private key on the rpi for safety concerns. Copy it over to the client machine. To connect, run:

```sh
ssh -i id_rsa pi@<ip-addr-of-pi>
```
  </table>
</details>

<details> 
  <summary>How to view the Raspberry Pi display wirelessly?</summary>
  This can be done by using a VNC server on the raspberry pi and a VNC viewer on the client computer. The most secure way of doing this is using VNC over SSH.

  * VNC over SSH tunnel. On the client machine run:

```sh
ssh -L 5901:localhost:5901 -N -f <distant_user>@<server_ip>
```

* Make sure the pi is running a vncserver on localhost only:

```sh
# run this first
vncserver :1 -geometry 1280x800 -depth 16 -localhost -nolisten tcp
```

* Connect to the vnc using client machine

```sh
xtightvncviewer localhost:1 -compresslevel 9 -quality 4 -depth 8
```

  </table>
</details>

<details> 
  <summary>How to create a VPN server using Raspberry Pi?</summary>

  * Install openvpn and wget

* Get the openvpn installation script (only runs on Ubuntu, Fedora, CentOS) chmod and execute it as a superuser

```sh
wget https://raw.githubusercontent.com/Angristan/openvpn-install/master/openvpn-install.sh

chmod +x openvpn-install.sh

sudo ./openvpn-install.sh
```

* This will create a `.ovpn` file. Copy it to the client.

* In the client machine use this to connect to the VPN:

```sh
openvpn <name-of-conf>.ovpn

# or copy it here
sudo cp Downloads/*.ovpn /etc/openvpn/client/client.conf

openvpn /etc/openvpn/client/client.conf
```

  </table>
</details>

<details> 
  <summary>How to setup an ad-blocker on Raspberry Pi?</summary>

* A single command installation can be done by the following URL

```
curl -sSL https://install.pi-hole.net | bash
```

* Make sure you have a static IP first

* Go through the default options in the installation

* Admin portal password reset

```
pihole -a -p
```

* Adding domains for blocklist

```
pihole -w <domain>
```

* For bulk adding URLs with domains go to the admin portal: `Group Management > Adlists`. In the Address, copy paste the contents of [the blocklist](./blocklist.txt), which contains about 3 million domains.

* After adding domains, update the lists using `pihole -g` or from the tools section of the admin portal (<IP>/admin).

  </table>
</details>

<details> 
  <summary>What are some uses of Raspberry Pi?</summary>

* NAS (Network Attached Storage) server using `OMV` ([OpenMediaVault](https://www.openmediavault.org/))

* Media streaming OS using `OSMC` ([Open Source Media Center](https://osmc.tv/)) or Kodi Media streming server

* Network Wide Adblocker using [Pi-Hole](https://pi-hole.net/)

* VPN (Virtual Private Network) server using [openvpn](https://github.com/Nyr/openvpn-install)

* Tor Relay and a personal tor network using [tor-box](https://github.com/CMoncur/tor_box)

* Lightweight Kubernetes cluster using [k3s](https://github.com/rancher/k3s)

* A retro gaming machine/emulator using [RetroPie](https://retropie.org.uk/)

* An ethical hacking drop box since [Kali Linux](https://www.offensive-security.com/kali-linux-arm-images/) is available for 32 and 64 bit ARM architecture

* A telegram bot server which is very easy to setup since it does not need direct network ingress

* A chat, audio and video conferencing server using [jitsi-meet](https://jitsi.github.io/handbook/docs/devops-guide/devops-guide-quickstart)

  </table>
</details>

<details> 
  <summary>How to create an audio/video conferencing server on a Raspberry Pi?</summary>
  Jitsi is a opensource server and video-bridge for hosting a chat, audio and video conferencing server on a raspberry pi.
  It can be deployed easily on any debian based distro but requires port-forwarding to be enabled from the router settings.

  * [Install jitsi-meet with docker](https://jitsi.github.io/handbook/docs/devops-guide/devops-guide-docker)
  * [Install jitsi-meet the regular way](https://jitsi.github.io/handbook/docs/devops-guide/devops-guide-quickstart)

  During the process of the installation, you will have to point a DNS domain name to your raspberry pi. Use the same link as a sevrer URL in your [jitsi-meet mobile application to use your server.](https://jitsi.org/downloads/) 

  [Here](https://www.youtube.com/watch?v=IQRwtUamHQU&t=1078s) is a video that might help with the installation.

  </table>
</details>



