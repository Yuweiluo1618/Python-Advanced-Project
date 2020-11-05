import socket

tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_client_socket.connect(('192.168.1.65', 8080))

tcp_client_socket.send('hi'.encode())

recv_data = tcp_client_socket.recv(1024)

print(recv_data.decode())

tcp_client_socket.close()