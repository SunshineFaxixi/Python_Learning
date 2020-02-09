import threading
import time


def test1(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("-----in test1 g_num = %d" % g_num)


def test2(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("-----in test2 g_num = %d" % g_num)


g_num = 0


def main():
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))

    t1.start()
    t2.start()

    time.sleep(1)

    print("-------in main g_num = %d" % g_num)


if __name__ == "__main__":
    main()

# -----in test1 g_num = 1194238
# -----in test2 g_num = 1236699
# -------in main g_num = 1236699
# 解释：因为g_num += 1在执行时分为好几步：
# 1. 获取g_num的值
# 2. 将g_num值加1
# 3. 将步骤2的值赋给g_num
# 由于有一个主线程和两个子线程，其中一个子线程在执行这一句时可能并未执行完所有三步，然后另一个子线程开始执行最终可能导致每个子线程都执行了一遍g_num += 1,但是g_num只增加了1
