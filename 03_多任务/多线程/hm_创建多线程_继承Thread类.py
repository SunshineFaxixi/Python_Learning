import threading


class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print("-----1------")
        self.login()

    def login(self):
        print("登录")

    def register(self):
        print("注册")


def main():
    t1 = MyThread()
    t1.start()  # 继承的Thread类中的start方法会自动调用run方法


if __name__ == "__main__":
    main()