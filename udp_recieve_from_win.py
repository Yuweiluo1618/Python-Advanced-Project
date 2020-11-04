import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.sendto("hello".encode(),('192.168.1.65', 8080) )

udp_rec = udp_socket.recvfrom(1024)
rec_text = udp_rec[0].decode()
print(f"the message from: {udp_rec[1]} content is {rec_text}")

udp_socket.close()