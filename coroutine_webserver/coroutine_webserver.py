from gevent import monkey
monkey.patch_all()

import gevent
import socket

class WebServer(object):
    def __init__(self):
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        tcp_server_socket.bind(('', 8080))
        tcp_server_socket.listen()
        self.tcp_server_socket = tcp_server_socket

    def start(self):
        while True:
            new_client_socket, ip_port = self.tcp_server_socket.accept()
            print(f'{str(ip_port)} has connected:')
            gevent.spawn(self.requet_handler, new_client_socket, ip_port)



    def requet_handler(self, new_client_socket, ip_port):
        while True:
            recv_data = new_client_socket.recv(2048)
            if not recv_data:
                print(f'{str(ip_port)} has left')
                break
            print(f'{str(ip_port)} says: {recv_data.decode()}')

        new_client_socket.close()

def main():
    ws = WebServer()
    ws.start()

if __name__ == '__main__':
    main()