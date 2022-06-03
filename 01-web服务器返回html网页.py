import socket
"""
需求:web服务器返回html网页的数据
分析:浏览器中看到的数据是保存在响应报文中的响应体中,修改响应体数据
"""
# ①创建服务端套接字
tcp_sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ②设置端口号复用
tcp_sever_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# ③绑定ip地址和端口号
tcp_sever_socket.bind(('', 8080))
# ④设置监听
tcp_sever_socket.listen(128)
while True:
    # ⑤等待接收客户端的连接
    client_server_socket, client_ip_port = tcp_sever_socket.accept()
    # ⑥接收客户端发来的请求报文
    recv_data = client_server_socket.recv(1024)
    # 对接收的数据进行解码
    recv_data = recv_data.decode('utf-8')
    print(recv_data)
    # ⑦返回数据给客户端(响应报文)
    # 响应报文组成
    # 响应行
    response_line = 'HTTP/1.1 200 OK\r\n'
    # 响应头
    response_header = 'Server:python\r\n'
    # 空行
    # 响应体,此时响应体数据就是一个网页数据
    with open('./html/render.html', 'r', encoding='utf-8') as f:
        response_body = f.read()
    # 拼接响应报文
    response_data = response_line + response_header + '\r\n' + response_body
    client_server_socket.send(response_data.encode('utf-8'))
    # ⑧关闭连接
    client_server_socket.close()
