import os
import multiprocessing


def copy_file(file_name, old_folder_name, new_folder_name):
    old_file = open(old_folder_name + "/" + file_name, "rb")
    content = old_file.read()
    old_file.close()

    new_file = open(new_folder_name + "/" + file_name, "wb")
    new_file.write(content)
    new_file.close()


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

    # 5. 向进程池中添加待copy的文件名称
    for file_name in file_names:
        po.apply_async(copy_file, args=(file_name, old_folder_name, new_folder_name))

    po.close()
    po.join()


if __name__ == "__main__":
    main()
