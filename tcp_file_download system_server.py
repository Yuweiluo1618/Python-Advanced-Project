import socket

tcp_server_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_server_client.bind(('', 8080))

tcp_server_client.listen(129)

while True:

    new_client_socket, client_ip_port = tcp_server_client.accept()

    file_name = new_client_socket.recv(1024).decode()

    try:

        send_file = open('./filesource/'+file_name, 'rb')

        while True:
            send_content = send_file.read(1024)
            if len(send_content) == 0:
                break
            new_client_socket.send(send_content)

    except Exception as e:

        print('no this file')

    else:
        print('file download successful')
        send_file.close()

    new_client_socket.close()

#tcp_server_client.close()