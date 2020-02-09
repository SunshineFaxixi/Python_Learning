import socket


def main():
	# 创建一个udp套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# 可以使用套接字收发数据

	# 关闭套接字
	udp_socket.close()

	print("-----------run--------")


if __name__ == "__main__":
	main()