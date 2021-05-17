from network import LoRa
import socket
import time
import binascii
import pycom

lora = LoRa(mode=LoRa.LORAWAN)#,region=LoRa.EU868)

dev_eui = binascii.unhexlify('70b3d54994c61237'.replace(' ',''))
app_eui = binascii.unhexlify('AC 01 DA C1 DA 71 B1 2A'.replace(' ',''))
app_key = binascii.unhexlify('11 00 22 00 33 00 44 00 55 00 66 00 77 00 88 00'.replace(' ',''))
lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key),  timeout=0)

print ("devEUI {}".format(binascii.hexlify(lora.mac())))

pycom.heartbeat(False)
pycom.rgbled(0x111111)

print(lora.stats().tx_frequency)

while not lora.has_joined():
    time.sleep(1)
    print('Not yet joined...')
print('Network joined!')


print(lora.stats().tx_frequency)


#s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
##s.bind(5)
#s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
#s.setsockopt(socket.SOL_LORA,  socket.SO_CONFIRMED,  False)

#cpt = 1

#while True:
#    pycom.rgbled(0x110000)
#    s.setblocking(True)
#    s.settimeout(15)

# for testing new code, remove try/except

#    try:
#        s.send('Hello LoRa {}'.format(cpt))
#    except:
#        print ('timeout in sending')

#    pycom.rgbled(0x001100)

#    try:
#        data = s.recv(64)

#        print(data)
#        pycom.rgbled(0x000011)
#    except:
#        print ('timeout in receive')
#        pycom.rgbled(0x000000)


#    s.setblocking(False)
#    time.sleep (30)

#    cpt += 1
