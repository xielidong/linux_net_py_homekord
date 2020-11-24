import socket
import threading

#tcp
#ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#udp
ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("建立服务套接字")

ss.bind(("127.0.0.1", 8888))

print("绑定端口和主机")

#ss.listen(5)

print("开始等待客户的请求")
#c = ss.accept()

#print("某个客户链接到我了")

def myrevc(c):
	while True:
		msg = c.recv(1024) # 当没有消息的时候休息，阻塞
		print(msg.decode())

#threading._start_new_thread(myrevc,(c[0],))

while True:
	msg = input()
	c[0].send(msg.encode())