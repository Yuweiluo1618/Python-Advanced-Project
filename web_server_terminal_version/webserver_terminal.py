import socket
import sys
from application import app

#This Server is final version which can be run in linux terminal and assign port manually

class WebServer(object):

    def __init__(self,port_num):
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        tcp_server_socket.bind(('', port_num))
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
    arg_list = sys.argv
    if len(arg_list) != 2:
        print("This is wrong format the correct format is: Python3 xxxx.py xxxx(port)")
        return
    if not arg_list[1].isdigit():
        print('The port should enter as integer')
        return

    port_num = int(arg_list[1])

    ws = WebServer(port_num)
    print('The Server has started, waiting for client...')
    ws.start()


if __name__ == '__main__':
    main()