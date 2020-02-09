import re


def main():
    tels = ["13100001234", "18912344321", "10086", "18800007777"]
    for tel in tels:
        ret = re.match(r"1\d{9}[0-35-68-9]$", tel)
        if ret:
            print("%s符合" % (ret.group()))
        else:
            print("%s不符合" % tel)


if __name__ == "__main__":
    main()