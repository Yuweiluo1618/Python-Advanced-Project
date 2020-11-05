import socket

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_server_socket.bind(('', 8080))

tcp_server_socket.listen(129)

new_socket,ip_port = tcp_server_socket.accept()

recv_data = new_socket.recv(1024)

print(f'This message is from {str(ip_port)} content {recv_data.decode()}')

new_socket.close()

tcp_server_socket.close()