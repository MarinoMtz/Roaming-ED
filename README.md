# Adding a roaming node (visiting node)

## Network parameters 

dev_eui included in the afnic side:  ` 344b770044aa1250, ... 55`

` app_key = 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 `

` app_eui =  00 00 00 00 00 00 00 01 ` 

## Python file example, to launch with Pycom included in ` join-req.py `

## Captures 

1. Chirpstack Application Server ![Alt text](/images/chirp.png?raw=true "JR")

2. Network server trace ` journalctl -u chirpstack-network-server -f -n 50` 

![Alt text](/images/NS_log.png?raw=true "JR")

3. Port 53: ` sudo tcpdump -ni ens3 udp port 53 ` ![Alt text](/images/port_53.png?raw=true "JR") 

# Local and and nodes visiting other networks

dev_eui included in the afnic side:  `b3e02e3f60308872, ... 80`

` app_key = e8 25 9b ae 9f b4 5e 7c 30 ae d8 1a 76 a9 44 d8 `

` app_eui = AC 01 DA C1 DA 71 B1 2A ` 

1. Chirpstack Application Server ![Alt text](/images/JR.png?raw=true "JR")

2. Network server trace ` sudo journalctl -f -n 100 -u chirpstack-application-server` 

![Alt text](/images/App_serverrue "JR")

3. Port 53: ` sudo tcpdump -ni ens3 udp port 53 ` ![Alt text](/images/port_53_home.png?raw=true "JR") 
