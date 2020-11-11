import socket
from application import app

#Encapsulation the method to different modules which makes program more reusable

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
            print(f'client {str(ip_port)} has connected')
            self.http_handler(new_client_socket, ip_port)


    def http_handler(self, new_client_socket, ip_port):
        recv_data = new_client_socket.recv(4089)
        if not recv_data:
            print(f'client {str(ip_port)} has disconnected')
            new_client_socket.close()
            return

        response = app.application('./html_src', recv_data)
        new_client_socket.send(response)
        new_client_socket.close()



def main():
    ws = WebServer()
    ws.start()


if __name__ == '__main__':
    main()