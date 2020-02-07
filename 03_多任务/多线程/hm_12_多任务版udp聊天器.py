import socket
import threading


def recv_msg(udp_socket):
    """接收数据"""
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)


def send_msg(udp_socket, dest_ip, dest_port):
    """发送数据"""
    while True:
        send_data = input("请输入要发送的内容：")
        udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def main():
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定本地信息
    udp_socket.bind(("", 7890))

    # 3. 获取对方本地信息
    dest_ip = input("请输入对方的ip：")
    dest_port = int(input("请输入对方的port："))

    # 4. 创建两个线程，接收和发送数据
    t_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
    t_send = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port))

    t_recv.start()
    t_send.start()

    # 5. 关闭套接字
    # udp_socket.close()


if __name__ == "__main__":
    main()