import re


def main():
    # search的用法：找到符合规则的第一个字符串
    ret = re.search(r"\d+", "文章阅读数：9999")
    print(ret.group())

    # findall的用法：找到所有符合规则的字符串
    ret = re.findall(r"\d+", "a = 999, b = 100, c = 672")
    print(ret)

    # sub的用法：将匹配到的字符串进行替换
    print(re.sub("\d+", "998", "python = 997"))


if __name__ == "__main__":
    main()