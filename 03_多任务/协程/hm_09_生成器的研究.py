
def create_num(all_num):
    print("-----1-------")
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        print("------2------")
        yield a
        print("------3------")
        a, b = b, a + b
        current_num += 1
        print("------4-------")


def main():
    obj = create_num(10)
    obj2 = create_num(10)

    ret = next(obj)
    print(ret)

    ret = next(obj)
    print(ret)

    ret = next(obj)
    print(ret)

    ret = next(obj2)
    print(ret)

    ret = next(obj2)
    print(ret)

    ret = next(obj)
    print(ret)


if __name__ == "__main__":
    main()