# 1. 装饰器方式
# 经典类，具有一种@property属性
class Goods1:
    @property
    def price(self):
        return 20


# 新式类,具有三种@property装饰器
class Goods2(object):
    @property
    def price(self):
        print('@property')


    @price.setter
    def price(self, value):
        print('@price.setter')


    @price.deleter
    def price(self):
        print('@price.deleter')


# 2. 类属性方式
class Foo(object):
    def get_bar(self):
        print("getter...")
        return 100

    def set_bar(self, value):
        print("setter...")
        return value

    def del_bar(self):
        print("deleter...")
        return 100

    BAR = property(get_bar, set_bar, del_bar, "description...")


def main():
    obj1 = Goods1()
    result = obj1.price
    print(result)

    
    obj2 = Goods2()
    obj2.price
    obj2.price = 123
    del obj2.price

    obj = Foo()
    obj.BAR
    obj.BAR = 'acd'
    desc = Foo.BAR.__doc__
    print(desc)
    del obj.BAR


if __name__ == "__main__":
    main()
