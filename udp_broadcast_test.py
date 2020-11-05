import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)

udp_socket.sendto("brodcast test".encode(),("255.255.255.255", 8080))

udp_socket.close()