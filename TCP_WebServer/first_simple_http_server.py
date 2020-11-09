import socket
#This is the simple http_server code can handle simple http service will update
def http_handle(new_tcp_client_socket, ip_port):
    request_data = new_tcp_client_socket.recv(2048)
    if len(request_data.decode()) == 0:
        print(f'{str(ip_port)} has disconneted')
        new_tcp_client_socket.close()
        return
    reply_line ='HTTP/1.1 200 OK\r\n'
    reply_head = 'Server: Python/yuwei\r\n'
    reply_blank = '\r\n'
    reply_body = 'Hello World'
    reply_request = reply_line+reply_head+reply_blank+reply_body

    new_tcp_client_socket.send(reply_request.encode())
    new_tcp_client_socket.close()


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(('', 8080))
    tcp_server_socket.listen(129)
    while True:
        new_tcp_client_socket, ip_port = tcp_server_socket.accept()
        print(f'{str(ip_port)} has been connected')
        http_handle(new_tcp_client_socket, ip_port)


if __name__ == "__main__":
    main()