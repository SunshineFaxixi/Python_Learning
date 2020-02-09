import socket


def service_client(new_socket):
    """返回客户端需要的数据"""

    # 1. 接收浏览器发送的请求, 即http请求
    # GET / HTTP/1.1
    request = new_socket.recv(1024)
    print(request)

    # 2. 返回http格式的数据给浏览器
    # 2.1 准备发送给浏览器的数据--header
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"
    # 2.2 准备发送给浏览器的数据--body
    response += "<h1>hahahhaha</h1>"
    new_socket.send(response.encode("utf-8"))
    
    # 3. 关闭套接字
    new_socket.close()


def main():
    """整体控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 绑定
    tcp_server_socket.bind(("", 9861))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)

    while True:
        # 4. 接收客户端请求
        new_socket, client_addr = tcp_server_socket.accept()

        # 5. 返回客户端需要的数据
        service_client(new_socket)

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
