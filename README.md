# lab3-CMSC426-CmpSec
## Description
In this lab 3, I worked with my group to compromise mutual authentication between machine A and machine B. There were over-arching methods applied: ARP cache poisoning, and a Man-In-The-Middle attack. Scapy packet building tools as well as Wireshark were used in this lab.<br>
## Repo Contents
- Labsetup: 
    - docker-compose.yml: file required to set up the containers hosting the three parties. Provided by professor<br>
    - messWitYa.py: eavesdrop on network traffice, intercept messages betweeen targets A & B, when sender is target A, always replace the word "Jim" with "AAA". Partially provided by professor.<br>
    - packetBuilder.py: original file, used to complete the ARP cache poisoning or Task 1 of lab 3. <br>
    - sniff-and-spoof.py: this program listens to network traffice for communication between two target members, and intercepts and replaces all communication originating from target A with a captal Z. Partially provided by professor.<br>  
- "Lab3-Group10-CMSC426-Spring2021-UMBC.pdf": This document was submitted by group 10 in response to the requirements of lab 3 as detailed in "arp_attack.pdf".<br>
- README.md<br>
- arp_attack.pdf : lab 3 instructions and requirements.<br>
