import socket
#This Advance http server can be deploed on linux
def http_handler(new_client_socket, ip_port):
    rec_data = new_client_socket.recv(4089)
    if not rec_data:
        new_client_socket.close()
        return

    rec_text =  rec_data.decode()
    loc = rec_text.find('\r\n')
    request_line = rec_text[:loc]
    request_line_list = request_line.split(" ")
    file_path = request_line_list[1]

    if file_path == '/':
        file_path = '/sample1.html'

    response_line = "HTTP/1.1 200 OK\r\n"
    response_header = 'Server: Python/Yuwei\r\n'
    response_blank = '\r\n'

    try:
        with open('./html_src' + file_path, 'rb') as file:
            response_body = file.read()

    except Exception as e:
        response_line = "HTTP/1.1 404 Not Found\r\n"
        response_body = f'Erroe! {str(e)}'
        response_body = response_body.encode()

    response_request = (response_line+response_header+response_blank).encode()+response_body

    new_client_socket.send(response_request)

    new_client_socket.close()




def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    tcp_server_socket.bind(('', 8080))
    tcp_server_socket.listen(129)
    while True:
        new_client_socket, ip_port = tcp_server_socket.accept()
        print(f'the client {str(ip_port)} has connected')
        http_handler(new_client_socket, ip_port)





if __name__ == '__main__':
    main()