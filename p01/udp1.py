'''
udp发送接收数据流程
1.创建udp套接字
2.准备接收方的地址
3.获取数据
4.发送数据到对方地址
5.关闭套接字
'''
import socket

udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

address = ('192.1.1.23',3244)#IP+端口的元组，ip是字符串，端口是数字

send_data = input('要输入的数据：')

udp_socket.sendto(send_data.encode('utf-8'),address)#转换成二进制的计算机字节语言

#接收数据
recv_data = udp_socket.recvfrom(1024)#1024最大字节数

udp_socket.close()


