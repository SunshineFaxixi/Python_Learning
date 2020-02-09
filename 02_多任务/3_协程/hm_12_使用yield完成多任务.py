import time


def task_1():
    while True:
        print("-----1------")
        time.sleep(0.1)
        yield


def task_2():
    while True:
        print("-----2------")
        time.sleep(0.1)
        yield


def main():
    t1 = task_1()
    t2 = task_2()
    # 先让t1运行一会儿，当t1遇到yield, 返回主程序，开始运行t2, 如此反复t1/t2/t1/t2, 最终实现多任务---协程
    while True:
        next(t1)
        next(t2)


if __name__ == "__main__":
    main()