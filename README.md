# Adding a roaming node (visiting node)

## Network parameters 

dev_eui included in the afnic side:  ` 344b770044aa1250, ... 55`

` app_key = 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 `

` app_eui =  00 00 00 00 00 00 00 01 ` 

## Python file example, to launch with Pycom included in ` join-req.py `

## Captures 

1. Chirpstack Application Server ![Alt text](/images/chirp.png?raw=true "JR")

2. Network server trace ` journalctl -u chirpstack-gateway-bridge -f -n 50` 

![Alt text](/images/NS_log.png?raw=true "JR")

3. Port 53: ` sudo tcpdump -ni ens3 udp port 53 ` ![Alt text](/images/port_53.png?raw=true "JR") 
