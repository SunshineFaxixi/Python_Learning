import re


def main():
    input_num = input("请输入一个数字：")
    ret = re.match(r"[1-9]?\d$|100", input_num)
    if ret:
        print("%s符合" % (ret.group()))
    else:
        print("%s不符合" % input_num)


if __name__ == "__main__":
    main()