
def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        ret = yield a
        print("=====ret=====", ret)
        a, b = b, a + b
        current_num += 1


def main():
    obj = create_num(10)

    ret = next(obj)
    print(ret)

    ret = obj.send("ahhaha")  # send启动生成器可以向生成器中传入参数，一般不用在第一次调用中，因为生成器中没有可接收的地方
    print(ret)


if __name__ == "__main__":
    main()