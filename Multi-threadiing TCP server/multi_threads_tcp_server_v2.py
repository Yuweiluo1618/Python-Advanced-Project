import socket
import threading

def recv_msg(new_client_socket, ip_port):
    while True:
        recv_data = new_client_socket.recv(1024)
        if not recv_data:
            break
        recv_text = recv_data.decode()
        print(f'clien {str(ip_port)} content: {recv_text}')
    new_client_socket.close()

def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(('', 8080))
    tcp_server_socket.listen(129)
    while True:
        new_client_socket, ip_port = tcp_server_socket.accept()
        print(f"clien {str(ip_port)} has been connected ")
        tc1 = threading.Thread(target=recv_msg, args=(new_client_socket, ip_port))
        tc1.setDaemon(True)
        tc1.start()

if __name__ == '__main__':
    main()
