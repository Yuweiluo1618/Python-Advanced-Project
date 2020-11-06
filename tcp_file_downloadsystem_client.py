import socket

tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

file_name = input("enter the name you want to download")

tcp_client_socket.connect(('192.168.1.73', 8080))

tcp_client_socket.send(file_name.encode())

file_save = open('./filedst/download.txt', 'wb')

while True:
    file_content = tcp_client_socket.recv(1024)
    if len(file_content) == 0:
        break
    file_save.write(file_content)

file_save.close()

tcp_client_socket.recv(1024)