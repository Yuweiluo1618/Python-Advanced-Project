import socket
def send_message(udp_socket):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    send_text = input('the message you want to wirte: ')
    udp_socket.sendto(send_text.encode(),('192.168.1.73', 8080))


def recieve_message(udp_socket):
    rec_text, ip_port = udp_socket.recvfrom(1024)
    print(f'the message is from {str(ip_port)} content is {rec_text.decode()} ')


def chat_display_frame():
    print('Welcome Chat Room')
    print('1. Send Message')
    print('2. Recieve message')
    print('quit program')

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('', 8080))
    while True:
        chat_display_frame()
        service_num = int(input("Select Service: "))
        if service_num == 1:
            send_message(udp_socket)
        elif service_num == 2:
            recieve_message(udp_socket)
        elif service_num == 3:
            break
        else:
            print("No this Service")
    udp_socket.close()


if __name__ == "__main__":
    main()
