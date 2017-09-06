# -*- coding:Utf8 -*-

#################################
# Title : Socket Client		#
# Date : 06/09/2017		#
# Auteur : GCO  		#
#################################


########### fuction #############


	

########### body ################

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '192.168.159.128'
PORT = 106
s.connect((HOST, PORT))
s.sendall(raw_input('Message a envoyer ? : '))
data = s.recv(2048)
s.close()
print 'Le message a bien ete envoyer' 

