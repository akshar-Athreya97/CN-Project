# CN-Project



Demonstrating Denial-Of-Service attacks using Socket Programming in Python for a project part of Computer Networks course 

This project was carried out as an assessment for Computer Networks course part of Electronics and Communication Engineering course at PES University

The main contributors to this project are:-
   -Akshar Deepankar Athreya
   -Ashwin Kumar Singh
   -Aditya Mandeep Vakani
   -Anurag Muttur

This repository contains the entire python script used to simulate different types of DoS attacks between 2 end systems with the knowledge of the victim's IP address.

We've demonstrated 4 different types of attacks:

    1. UDP Flood
    2. TCP Syn Flood
    3. TCP Rst Flood
    4. ICMP Flood 
    
The python script "dos.py" contains separate functions for each attack and the attacker can choose the attack he wants to carry out.

1. UDP Flooding -> (def UDPFlood)
    In this function, we create a socket of UDP type, using this we send UDP packers of random size to a specific IP address , with
    a while loop.
2. TCP SYN Flooding -> (def SYNFlood)
    Here we use python's raw sockets to create a socket of TCP type, specify the IP and TCP headers ,including source(spoofed) and
    destination IP address.
3. TCP RST Flooding -> (in main())
    RST packets are send from randomly generated source IPs to a victim, thereby making the victim's system use up a lot of 
    resources in managing the packets.
4. ICMP FLood -> (in main())
    The attacker sends a large amount of ICMP(Echo requests) to the victim overwhelmin it.
