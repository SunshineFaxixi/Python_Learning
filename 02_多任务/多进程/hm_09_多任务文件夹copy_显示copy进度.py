import os
import multiprocessing


def copy_file(queue, file_name, old_folder_name, new_folder_name):
    old_file = open(old_folder_name + "/" + file_name, "rb")
    content = old_file.read()
    old_file.close()

    new_file = open(new_folder_name + "/" + file_name, "wb")
    new_file.write(content)
    new_file.close()

    queue.put(file_name)


def main():
    # 1. 获取要copy的文件夹名称
    old_folder_name = input("请输入要复制的文件夹名称：")

    # 2. 创建一个新的文件夹
    try:
        new_folder_name = old_folder_name + "[复件]"
        os.mkdir(new_folder_name)
    except:
        pass

    # 3. 获取文件夹的所有待copy的文件夹的名字
    file_names = os.listdir(old_folder_name)

    # 4. 创建进程池
    po = multiprocessing.Pool(5)

    # 5.创建一个队列
    q = multiprocessing.Manager().Queue()

    # 6. 向进程池中添加待copy的文件名称
    for file_name in file_names:
        po.apply_async(copy_file, args=(q, file_name, old_folder_name, new_folder_name))

    po.close()
    # po.join()
    all_file_num = len(file_names)
    copy_ok_num = 0
    while True:
        file_name = q.get()
        copy_ok_num += 1
        print("\r已经完成copy: %.2f%%" % (copy_ok_num * 100 / all_file_num), end="")
        if copy_ok_num >= all_file_num:
            break
    print()


if __name__ == "__main__":
    main()
