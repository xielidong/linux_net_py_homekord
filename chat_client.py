import socket
import threading

#tcp
#u = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#udp
u = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("创建客户套接字")

#u.connect(("127.0.0.1",8888))
u.sendto('127.0.0.1', 8888)

#print("我已连接到服务器")

def myrevc(c):
	while True:
		msg = c.recv(1024)
		print(msg.decode())

threading._start_new_thread(myrevc)

while True:
	print("输入")
	msg = input()
	u.send(msg.encode())
