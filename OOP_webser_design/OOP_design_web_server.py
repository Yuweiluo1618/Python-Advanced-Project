import socket

#This is the OOP Web Server the test has been passed can be deployed
class WebServer(object):

    def __init__(self):
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        tcp_server_socket.bind(('', 8080))
        tcp_server_socket.listen(129)
        self.tcp_server_socket = tcp_server_socket

    def start(self):
        while True:
            new_client_socket, ip_port = self.tcp_server_socket.accept()
            print(f'the client {str(ip_port)} has joined')
            self.http_handler(new_client_socket, ip_port)


    def http_handler(self, new_client_socket, ip_port):
        recv_request_data = new_client_socket.recv(4098)

        if not  recv_request_data:
            new_client_socket.close()
            print(f'the client {str(ip_port)} has disconnected')
            return

        recv_request_text =  recv_request_data.decode()
        loc = recv_request_text.find('\r\n')
        request_line = recv_request_text[:loc]
        request_line_list = request_line.split(' ')
        file_path = request_line_list[1]

        if file_path == '/':
            file_path = '/sample1.html'

        response_line = 'HTTP/1.1 200 OK\r\n'
        response_hearder = 'Server: Python/Yuwei\r\n'
        response_blank = '\r\n'
        try:
            with open('./html_src'+file_path, 'rb') as file:
                response_body = file.read()
        except Exception as e:
            response_line = 'HTTP/1.1 404 Not Found\r\n'
            response_body = (f'Error! {str(e)}').encode()

        response_http = (response_line+response_hearder+response_blank).encode()+response_body

        new_client_socket.send(response_http)
        new_client_socket.close()


def main():
    ws = WebServer()
    ws.start()

if __name__ == '__main__':
    main()