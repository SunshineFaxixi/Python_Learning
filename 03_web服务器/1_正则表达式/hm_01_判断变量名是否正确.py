import re


def main():
    names = ["age13", "age_11", "123age", "_age", "age!", "age_1_#"]
    for name in names:
        ret = re.match(r"[a-zA-Z_][a-zA-Z0-9_]*$", name)
        if ret:
            print("变量名%s符合" % (ret.group()))
        else:
            print("变量名不符合")


if __name__ == "__main__":
    main()