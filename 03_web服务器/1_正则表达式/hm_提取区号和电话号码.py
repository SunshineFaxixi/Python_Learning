import re


def main():
    number = input("请输入电话号码：")
    ret = re.match(r"([^-]{3,4})-(\d{8}$)", number)  # ^在[]中使用时，表示下一个字符的反
    if ret:
        print("%s匹配正确" % (ret.group()))
        print("区号是：", ret.group(1))
        print("电话号码是：", ret.group(2))
    else:
        print("%s匹配不正确" % number)


if __name__ == "__main__":
    main()