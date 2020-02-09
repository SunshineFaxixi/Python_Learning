from multiprocessing import Pool
import time, os, random


def worker(msg):
    start_time = time.time()
    print("%s开始执行，进程号为%d" %(msg, os.getpid()))
    time.sleep(random.random() * 2)
    stop_time = time.time()
    print("执行完成，用时%.2f" % (stop_time - start_time))


def main():
    po = Pool(3)  # 创建一个进程池，最大进程数为3
    for i in range(10):
        po.apply_async(worker, (i,))  # 每次循环将会用空闲下来的子进程去调用目标

    print("-------start--------")
    po.close()  # 关闭进程池，关闭后不再接收新的请求
    po.join()  # 等待po中所有子进程执行完成，必须在po.close()之后
    print("-------stop---------")


if __name__ == "__main__":
    main()