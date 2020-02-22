#coding:utf-8
import socket
import re
import select


def service_client(new_socket, request):
    """为这个客户端服务"""
    request_lines = request.splitlines()
    print("")
    print(">" * 20)
    print(request_lines)

    file_name = ""
    ret = re.match(r"[^/] + (/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "index.html"

    try:
        f.open("./html" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "----------file not found--------"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        response_body = html_content
        response_header += "HTTP/1.1 200 OK\r\n"
        response_header += "COntent_Length:%d\r\n" % len(response_body)
        response_header += "\r\n"
        response = response_header.encode("utf-8") + response_body

        new_socket.send(response)

def main():
    """完成整体控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 绑定
    tcp_server_socket.bind(("", 7890))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)
    
    # 创建一个epoll对象
    epl = select.epoll()

    # 注册事件到epoll中
    epoll.register(tcp_server_socket.fileno(), select.EPOLLIN|select.EPOLLET)

    connections = {}
    addresses = {}

    while True:

        # 4. 等待新客户端的链接
         new_socket, client_addr = tcp_server_socket.accept()
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)

        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024).decode("utf-8")
            except Exception as ret:
                pass
            else:
                if recv_data:
                    service_client(client_socket, recv_data)
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
