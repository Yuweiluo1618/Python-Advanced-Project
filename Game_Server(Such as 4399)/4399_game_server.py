import socket
import threading
import multiprocessing
#This is 4399 like game server developer can add and deploy own game in game_path_dir
class GameServer(object):
    def __init__(self):
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        tcp_server_socket.bind(('', 8080))
        tcp_server_socket.listen(129)
        self.tcp_server_socket = tcp_server_socket
        self.game_path_dir = dict()
        #add game name and path here
        self.game_path_dir['snake'] = './Snake'
        self.cur_path = ''
        self.project_init()

    def project_init(self):
        game_path_list = list(self.game_path_dir.keys())
        for index, game_name in enumerate(game_path_list):
            print(f'{index}. {game_name}')
        sel_no = input('Select the game you want to deploy')
        game_tag = game_path_list[int(sel_no)]
        self.cur_path = self.game_path_dir[game_tag]


    def start(self):
        """This method will start Server"""
        print('game server has started')
        while True:
            new_client_socket, ip_port = self.tcp_server_socket.accept()
            print(f'client {str(ip_port)} has connected')
            #th1 = threading.Thread(target=self.http_handler, args=(new_client_socket, ip_port))
            #th1.setDaemon(True)
            #th1.start()

            game_process = multiprocessing.Process(target=self.http_handler, args=(new_client_socket, ip_port))
            game_process.start()

            new_client_socket.close()


    def http_handler(self, new_client_socket, ip_port):
        recv_data = new_client_socket.recv(4096)
        if not recv_data:
            print(f'client {str(ip_port)} has disconnected')
            new_client_socket.close()
            return
        recv_text = recv_data.decode()
        loc = recv_text.find('\r\n')
        request_line = recv_text[:loc]
        request_line_list = request_line.split(' ')
        game_path = request_line_list[1]
        if game_path == '/':
            game_path = '/index.html'

        resource_path = self.cur_path+game_path


        response_line = 'HTTP/1.1 200 OK\r\n'
        response_header = 'Server: Yuweiluo/4399\r\n'
        response_header += 'text/html;charset=utf-8\r\n'
        response_blank = '\r\n'
        try:
            with open(resource_path, 'rb') as file:
                response_body = file.read()
        except Exception as e:
            response_line = 'HTTP/1.1 404 Not Found\r\n'
            response_body = f'Game Not Found {str(e)}'
            response_body = response_body.encode()

        response_proto = (response_line+response_header+response_blank).encode()+response_body

        new_client_socket.send(response_proto)
        new_client_socket.close()

def main():
    gs = GameServer()
    gs.start()

if __name__ == '__main__':
    main()
