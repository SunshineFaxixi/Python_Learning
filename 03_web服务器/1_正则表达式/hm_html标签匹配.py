# 需求：匹配出<html><h1>www.itcast.cn</h1></html>
import re


def main():
    html_str = "<html><h1>www.itcast.cn</h1></html>"
    ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", html_str)
    if ret:
        print("%s符合" % (ret.group()))
    else:
        print("%s不符合" % html_str)


if __name__ == "__main__":
    main()