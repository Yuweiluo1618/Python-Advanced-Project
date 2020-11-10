import socket
#this version could return webpage now
def http_handler(new_client_socket, ip_port):
    recv_data = new_client_socket.recv(4089)
    if not recv_data:
        print(f'the client{str(ip_port)} has disconnected')
        new_client_socket.close()
        return
    with open('./html_src/sample1.html', 'rb') as file:
        response_body = file.read()
    response_line = "HTTP/1.1 200 OK\r\n"
    response_header = 'Server: Python/Yuwei\r\n'
    response_blank = '\r\n'
    response_protocol = (response_line+response_header+response_blank).encode()+response_body

    new_client_socket.send(response_protocol)
    new_client_socket.close()


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind((('', 8080)))

    tcp_server_socket.listen(129)
    while True:
        new_client_socket, ip_port = tcp_server_socket.accept()
        print(f'the client {str(ip_port)} has joined')
        http_handler(new_client_socket, ip_port)


if __name__ == "__main__":
    main()