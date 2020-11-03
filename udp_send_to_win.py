import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.sendto("udp message".encode(), ("192.168.1.65", 8080))

udp_socket.close()