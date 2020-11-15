import socket
import threading

#This Chat Room allows send message and recv at same time
def send_msg(udp_socket):
    content = input('send content: ')
    udp_socket.sendto(content.encode(), ('192.168.1.65', 8080))


def recv_msg(udp_socket):
    while True:
        recv_data, ip_port = udp_socket.recvfrom(1024)
        print(f'\nMessage from {str(ip_port)}: {recv_data.decode()}')



def begin_title():
    print('------Welcome The ChatRoom-------')
    print('1. Send Message')
    print('2. Exit the room')


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('', 8080))
    tc1 = threading.Thread(target=recv_msg, args=(udp_socket,))
    tc1.setDaemon(True)
    tc1.start()
    while True:
        begin_title()
        sel_no = int(input('Select the service: '))
        if sel_no == 1:
            send_msg(udp_socket)
        elif sel_no == 2:
            print('Exiting.....')
            break
    udp_socket.close()


if __name__ == '__main__':
    main()