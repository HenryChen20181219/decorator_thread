'''
tcp客户端流程：
1.创建套接字
2.链接到目标服务器
3.发送数据
4.接收服务器的数据
5.关闭套接字
'''
import socket
tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

addr = ('123.23.2.43',323)
tcp_client_socket.connect(addr)

send_data = input('客户端输入的数据：')
tcp_client_socket.send(send_data.encode('utf-8'))

recv_data = tcp_client_socket.recv(1024)
print(recv_data.decode('utf-8'))

tcp_client_socket.close()

'''
tcp服务器流程
1.创建套接字
2.绑定端口号
3.listen监听，被动链接
4.accept等待客户端链接,产生新的套接字
5.接收数据，发送数据
6.关闭这个新的套接字
'''
tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

tcp_server_socket.bind(('123.23.2.43',323))

tcp_server_socket.listen(128)

client_socket,client_addr = tcp_server_socket.accept()

recv_data = client_socket.recv(1024)
print(recv_data.decode('utf-8'))
client_socket.send('thank you'.encode('utf-8'))

client_socket.close()

