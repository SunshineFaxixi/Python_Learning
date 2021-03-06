from collections import Iterable
from collections import Iterator
import time


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如要使一个对象成为可迭代的，一定要使用__iter__方法"""
        return ClassIterator(self)


class ClassIterator(object):
    def __init__(self, obj):
        self.obj = obj
        self.current_num = 0

    def __iter__(self):
        pass

    def __next__(self):
        result = self.obj.names[self.current_num]
        self.current_num += 1
        return result


def main():
    classmate = Classmate()
    classmate.add("zhangsan")
    classmate.add("lisi")
    classmate.add("wangwu")

    # print("判断classmate是否是可迭代的：", isinstance(classmate, Iterable))
    # classmate_iterator = iter(classmate)
    # print("判断classmate_iterator是否是迭代器：", isinstance(classmate_iterator, Iterator))
    # print(next(classmate_iterator))

    for temp in classmate:
        print(temp)
        time.sleep(1)


if __name__ == "__main__":
    main()