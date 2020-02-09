
def create_num(all_num):
    print("-----1------")
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        print("------2------")
        yield a  # 当一个函数中含有yield函数时，这个函数就变成一个生成器模板
        print("-------3------")
        # print(a)
        a, b = b, a + b
        current_num += 1
        print("------4------")


def main():
    obj = create_num(10)  # 当调用一个生成器模板时，会创建一个生成器对象。创建时生成器不会往下执行
    ret = next(obj)  # 当调用next()方法时，生成器会往下执行，一直到yield停止
    print(ret)
    ret = next(obj)  # 当再次调用next()方法时，会从上次停止的位置继续执行
    print(ret)


if __name__ == "__main__":
    main()