import re


def main():
    email = input("请输入一个邮箱：")
    ret = re.match(r"[a-zA-Z0-9]{4,20}@(163|126)\.com$", email)
    if ret:
        print("邮箱符合要求")
    else:
        print("邮箱不符合要求")


if __name__ == "__main__":
    main()