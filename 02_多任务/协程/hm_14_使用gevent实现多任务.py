import gevent
# import time


def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)  # 若程序中没有延时，则单线程执行
        # time.sleep(0.5)  # 不能用time.sleep(), 需要用gevent.sleep(), 否则没效果
        gevent.sleep(0.5)


def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)
        gevent.sleep(0.5)


def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)
        gevent.sleep(0.5)


def main():
    g1 = gevent.spawn(f1, 5)  # 只是创建对象，此时未运行
    g2 = gevent.spawn(f2, 5)
    g3 = gevent.spawn(f3, 5)

    g1.join()
    g2.join()
    g3.join()


if __name__ == "__main__":
    main()