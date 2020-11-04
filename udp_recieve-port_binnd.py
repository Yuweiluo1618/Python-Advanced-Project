import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(('', 6666))

rec_text, ip_port = udp_socket.recvfrom(1024)
print(f'recieve message from {str(ip_port)} content is {rec_text.decode()}')

udp_socket.close()



