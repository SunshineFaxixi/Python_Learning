from greenlet import greenlet
import time


def test1():
    while True:
        print("-----A------")
        gr2.switch()
        time.sleep(0.5)


def test2():
    while True:
        print("-----B-----")
        gr1.switch()
        time.sleep(0.5)


gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()


# def main():
#     gr1 = greenlet(test1)
#     gr2 = greenlet(test2)
#
#     gr1.switch()
#
#
# if __name__ == "__main__":
#     main()