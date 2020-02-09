import threading
import time


def test():
    for i in range(5):
        print("-----test-----%d" % i)
        time.sleep(1)


def main():
    # 当调用Thread类创建出来的实例对象的start方法时，才会创建线程并让这个线程运行
    print(threading.enumerate())
    t1 = threading.Thread(target=test)
    print(threading.enumerate())
    t1.start()
    print(threading.enumerate())


if __name__ == "__main__":
    main()