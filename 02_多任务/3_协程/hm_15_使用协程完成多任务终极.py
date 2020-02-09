import gevent
import time
import random
from gevent import monkey


def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name, i)
        time.sleep(random.random())


def main():
    monkey.patch_all()  # 打补丁

    gevent.joinall([
        gevent.spawn(coroutine_work, "work1"),
        gevent.spawn(coroutine_work, "work2")
    ])



if __name__ == "__main__":
    main()