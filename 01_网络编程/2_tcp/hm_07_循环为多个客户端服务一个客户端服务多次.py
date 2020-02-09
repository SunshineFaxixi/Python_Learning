import socket


def main():
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定本地信息
    tcp_server_socket.bind(("", 7890))

    # 3. 监听，让默认的套接字由主动变为被动
    tcp_server_socket.listen(128)

    while True:  # 为多个客户端服务

        # 4. 等待客户端的链接
        print("等待新的客户端的到来...")
        new_client_socket, client_addr = tcp_server_socket.accept()

        print(client_addr)

        while True:  # 为同一个客户端服务多次

            # 接收客户端发送过来的请求
            recv_data = new_client_socket.recv(1024)
            print("新的客户端接收到的数据是：%s", str(recv_data))

            if recv_data:
                # 回送一部分数据给客户端
                new_client_socket.send("hahah----ok-------".encode("utf-8"))
            else:
                # 关闭套接字
                new_client_socket.close()
                print("新的客户端服务完成...")

    tcp_server_socket.close()


if __name__ == "__main__":
    main()