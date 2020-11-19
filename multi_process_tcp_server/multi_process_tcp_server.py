import socket
import multiprocessing

class WebServer(object):
    def __init__(self):
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        tcp_server_socket.bind(('',8080))
        tcp_server_socket.listen()
        self.tcp_server_socket = tcp_server_socket

    def start(self):
        while True:
            new_client_socket, ip_port = self.tcp_server_socket.accept()
            print(f'client {str(ip_port)} has joined')
            client_process = multiprocessing.Process(target=self.client_handler, args=(new_client_socket, ip_port))
            client_process.start()
            #new_client_socket.close()

    def client_handler(self, new_client_socket, ip_port):
        while True:
            recv_data = new_client_socket.recv(1024)
            if not recv_data:
                print(f'client {str(ip_port)} has left')
                new_client_socket.close()
                break
            recv_text = recv_data.decode()
            print(recv_text)
        new_client_socket.close()


def main():
    ws = WebServer()
    ws.start()

if __name__ == '__main__':
    main()