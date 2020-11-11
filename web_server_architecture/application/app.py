from application import utils

def parse(recv_data):
    recv_text = recv_data.decode()
    loc = recv_text.find('\r\n')
    request_line = recv_text[:loc]
    request_line_list = request_line.split(' ')
    file_path = request_line_list[1]
    if file_path == '/':
        file_path = '/sample1.html'
    return file_path


def application(cur_dir, recv_data):
    file_path = parse(recv_data)
    resource_path = cur_dir+file_path

    try:
        with open(resource_path, 'rb') as file:
            response_body = file.read()
            response_protocol = utils.create_http_request('200 OK', response_body)
    except Exception as e:
        response_body = f'Error! {str(e)}'
        response_body = response_body.encode()
        response_protocol = utils.create_http_request('404 Not Found', response_body)

    return response_protocol