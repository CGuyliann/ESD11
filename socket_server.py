import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = ''
PORT = 106
s.bind((HOST, PORT))
s.listen(5)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
	data = conn.recv(2048)
	print data
	if not data: break
	conn.sendall (data)	
socket.close()
