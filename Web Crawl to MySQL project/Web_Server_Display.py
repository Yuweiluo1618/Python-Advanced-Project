import socket
import pymysql

class WebServer(object):
    def __init__(self):
        web_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        web_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        web_server_socket.bind(("", 8080))
        web_server_socket.listen(129)
        self.conn = pymysql.connect(host='localhost', user='root', password='', database='movie_db')
        self.cur =  self.conn.cursor()
        self.web_server_socket = web_server_socket

    def handle_request(self):
        while True:
            new_client_socket, ip_port = self.web_server_socket.accept()
            response_line = 'HTTP/1.1 200 ok\r\n'
            response_header ='Server: Python/Yuwei\r\n'
            response_header += 'Content-type:text/html;charset=GBK\r\n'
            response_blank = '\r\n'
            response_body = ''
            sql = 'select film_name, film_link from movie_link'
            self.cur.execute(sql)
            movie_list = self.cur.fetchall()
            for movie in movie_list:
                response_body += f"movie name: {movie[0]} movie link:<a href='{movie[1]}'>{movie[1]}</a>\r\n"

            response_request = (response_line+response_header+response_blank+response_body).encode('GBK')
            new_client_socket.send(response_request)

            new_client_socket.close()



def main():
    ws = WebServer()
    ws.handle_request()

if __name__ == '__main__':
    main()