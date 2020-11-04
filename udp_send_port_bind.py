import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.bind(("",6500))

udp_socket.sendto("hello".encode(), ('192.168.1.65', 8080))

udp_socket.close()