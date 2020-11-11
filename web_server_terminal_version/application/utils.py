def create_http_request(header_dis, response_body):
    response_line = f'HTTP/1.1 {header_dis}\r\n'
    response_header = 'Server: Python/Yuwei\r\n'
    response_blank = '\r\n'
    response_porotocol = (response_line + response_header + response_blank).encode() + response_body
    return response_porotocol