import socket


def send_file_2_cilent(new_client_socket):

    # 1. 接收客户端需要下载的文件名
    file_name = new_client_socket.recv(1024).decode("utf-8")
    file_content = None

    # 2. 打开文件，读取数据
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件 %s" % file_name)

    # 3. 发送文件数据给客户端
    if file_content:
        new_client_socket.send(file_content.encode("utf-8"))


def main():
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定ip和端口
    tcp_server_socket.bind(("", 7890))

    # 3. 让套接字由主动变被动
    tcp_server_socket.listen(128)

    while True:
        # 4. 等待客户端连接
        new_client_socket, client_addr = tcp_server_socket.accept()

        send_file_2_cilent(new_client_socket)


if __name__ == "__main__":
    main()