import socket

"""
需求:web服务器根据不同的请求资源路径返回不同的html网页的数据
分析:
①浏览器中看到的数据是保存在响应报文中的响应体中,修改响应体数据
②获取接收数据(请求报文)中的请求行
③获取请求行中的请求资源路径
④根据请求资源路径判断请求是哪个网页,读取对应网页的数据 if语句
"""
# ①创建服务端套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ②设置端口号复用
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# ③绑定ip地址和端口号
tcp_server_socket.bind(('', 8080))
# ④设置监听
tcp_server_socket.listen(128)
while True:
    # ⑤等待接收客户端的连接
    client_server_socket, client_ip_port = tcp_server_socket.accept()
    # ⑥接收客户端发来的请求报文
    recv_data = client_server_socket.recv(1024)
    # 对接收的数据进行解码
    recv_data = recv_data.decode('utf-8')
    print(recv_data)
    # 获取请求报文中请求行的内容,实际上就是对字符串通过 \n 进行分割, [0] 取列表中的第一个元素
    request_line = recv_data.split('\r\n')[0]
    print(f'请求行的数据为:{request_line}')
    request_load = request_line.split(' ')[1]
    print(f'请求的资源路径为{request_load}')
    # ⑦返回数据给客户端(响应报文)
    # 响应报文组成
    # 响应行
    response_line = 'HTTP/1.1 200 OK\r\n'
    # 响应头
    response_header = 'Server:python\r\n'
    if 'render.html' in request_load:
        with open('./html/render.html', 'r', encoding='utf-8') as f:
            response_body = f.read()
    elif 'gdp.html' in request_load:
        with open('./html/gdp.html', 'r', encoding='utf-8') as f:
            response_body = f.read()
    # 拼接响应报文
    response_data = response_line + response_header + '\r\n' + response_body
    client_server_socket.send(response_data.encode('utf-8'))
    # ⑧关闭连接
    client_server_socket.close()
