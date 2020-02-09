import re


def main():
    # 匹配多个字符
    html_content = """ajhshd
    akdwihdiw
    qiheiwdihffe
    """

    ret1 = re.match(r".*", html_content)  # .*表示匹配任何多个字符，除了\n
    print(ret1.group())

    ret2 = re.match(r".*", html_content, re.S)
    print(ret2.group())


if __name__ == "__main__":
    main()