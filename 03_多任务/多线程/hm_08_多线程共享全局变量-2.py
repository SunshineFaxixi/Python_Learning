import threading
import time


def test1(temp):
    temp.append(33)
    print("------test1 temp = %s" % str(temp))


def test2(temp):
    print("------test2 temp = %s" % str(temp))


g_nums = [11, 22]


def main():
    # target指定开启的线程执行的函数，args表示调用函数时传递的函数参数，此处temp会接收传递的参数
    t1 = threading.Thread(target=test1, args=(g_nums,))
    t2 = threading.Thread(target=test2, args=(g_nums,))

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print("--------in main g_nums = %s" % str(g_nums))


if __name__ == "__main__":
    main()
