import socket
#simple browser need update

tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_client_socket.connect(('192.168.1.73', 80))

http_line = 'GET / HTTP/1.1\r\n'
http_header = 'Host: 192.168.1.73\r\n '
http_blank = '\r\n'
http_request = http_line+http_header+http_blank



tcp_client_socket.send(http_request.encode())

recv_data = tcp_client_socket.recv(4096)
recv_text = recv_data.decode()
html_index = recv_text.find('\r\n\r\n')
html_text = recv_text[html_index+4:]

with open('./htmlStorage/1.html', 'w') as file:
    file.write(html_text)

tcp_client_socket.close()