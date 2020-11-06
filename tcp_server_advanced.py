import socket

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_server_socket.bind(('', 8081))

tcp_server_socket.listen(129)
while True:
    new_client_socket, client_ip_port = tcp_server_socket.accept()
    print(f'the client: {repr(client_ip_port)} has been connected')

    while True:
        recv_data = new_client_socket.recv(1024)
        if len(recv_data) != 0:
            print(f'Message: {recv_data.decode()}')
        else:
            break

    new_client_socket.close()

tcp_server_socket.close()