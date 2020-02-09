import re


def main():
    email = input("请输入一个邮箱：")
    ret = re.match(r"\w{4,20}@(163|126|qq)\.com$", email)
    if ret:
        print("%s符合要求" % ret.group())
    else:
        print("%s不符合要求" % email)


if __name__ == "__main__":
    main()