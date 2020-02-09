import socket


def main():
    # 1. 创建套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 获取服务器的ip, port
    dest_ip = input("请输入服务器的ip：")
    dest_port = int(input("请输入服务器的port："))

    # 3. 链接服务器
    tcp_client_socket.connect((dest_ip, dest_port))

    # 4. 获取要下载的文件名称
    download_file_name = input("请输入要下载的文件名：")

    # 5. 发送文件名
    tcp_client_socket.send(download_file_name.encode("utf-8"))

    # 6. 接收服务器发送的数据
    recv_data = tcp_client_socket.recv(1024)

    if recv_data:
        # 7. 将接收到的数据写到文件中
        with open("[新]" + download_file_name, "wb") as f:
            f.write(recv_data)

    # 8. 关闭套接字
    tcp_client_socket.close()


if __name__ == "__main__":
    main()