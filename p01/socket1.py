import socket

#建立tcp套接字
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#创建udp套接字
s1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#用完需关闭
s.close()
s1.close()

