import socket
import threading

def recv_msg(tcp_server_socket):
    new_client_socket, ip_port = tcp_server_socket.accept()
    print(f'client {str(ip_port)} has connected')
    while True:
        recv_data = new_client_socket.recv(1024)
        if not recv_data:
            new_client_socket.close()
            print(f"client{str(ip_port)} has disconnected")
            break
        recv_text = recv_data.decode()
        print(f'Messsage: {recv_text}')
    new_client_socket.close()





def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(('', 8080))

    tcp_server_socket.listen(129)

    while True:
        if tcp_server_socket.accept():
            print('in while')
            tc = threading.Thread(target=recv_msg, args=(tcp_server_socket, ))
            tc.setDaemon(True)
            tc.start()

if __name__ == '__main__':
    main()