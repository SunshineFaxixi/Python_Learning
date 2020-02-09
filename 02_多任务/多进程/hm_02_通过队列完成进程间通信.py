import multiprocessing


def download_from_web(q):
    # 模拟从网上下载的数据
    data = [11, 22, 33]

    # 向队列中写入数据
    for temp in data:
        q.put(temp)

    print("下载器下载完数据并存入队列中")


def analysis_data(q):
    """数据处理"""
    waiting_analysis_data = list()
    # 从队列中获取数据
    while True:
        data = q.get()
        waiting_analysis_data.append(data)

        if q.empty():
            break

    # 处理数据
    print(waiting_analysis_data)


def main():
    # 1. 创建一个队列
    q = multiprocessing.Queue()

    # 2. 创建两个进程
    q1 = multiprocessing.Process(target=download_from_web, args=(q,))
    q2 = multiprocessing.Process(target=analysis_data, args=(q,))
    q1.start()
    q2.start()


if __name__ == "__main__":
    main()