import threading
import time


def test1(num):
    global g_num
    for i in range(num):
        mutex.acquire()  # 上锁，如果之前没有被上锁，此时上锁成功，若之前已经上锁，此时会堵塞
        g_num += 1
        mutex.release()  # 解锁
    print("-----in test1 g_num = %d" % g_num)


def test2(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("-----in test2 g_num = %d" % g_num)

`  \

g_num = 0
# 创建一把锁，但是此时锁并没有被使用
mutex = threading.Lock()


def main():
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))

    t1.start()
    t2.start()

    time.sleep(1)

    print("-------in main g_num = %d" % g_num)


if __name__ == "__main__":
    main()

