#coding=utf-8
import socket
import time

g_socket_list = list()
def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server_socket.bind(("", 7890))
    tcp_server_socket.listen(128)
    while True:
        time.sleep(0.5)
        try:
            new_socket, client_addr = tcp_server_socket.accept()
        except Exception as ret:
            pass
        else:
            print("一个新的客户端到来")
            new_socket.setblocking(False)  # 设置为非堵塞
            g_socket_list.append(new_socket)

    
    for client_socket in g_socket_list:
        try:
            recv_data = client_socket.recv(1024)
            if recv_data:
                print("收到客户端发送的数据")
            else:
                print("客户端已经关闭")
                client_socket.close()
                g_socket_list.remove(client_socket)

        except Exception as result:
            pass


if __name__ == "__main__":
    main()
