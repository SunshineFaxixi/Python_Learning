
def create_num(all_num):
    # print("-----1-------")
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        # print("------2------")
        yield a
        # print("------3------")
        a, b = b, a + b
        current_num += 1
        # print("------4-------")

    return "ok...."


def main():
    obj = create_num(20)
    while True:
        try:
            ret = next(obj)
            print(ret)
        # except StopIteration:
        #     break
        except Exception as res:
            print(res.value)  # return的值在此处可以打印
            break


if __name__ == "__main__":
    main()