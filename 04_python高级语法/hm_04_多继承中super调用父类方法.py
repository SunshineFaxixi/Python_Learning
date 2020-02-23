#coding=utf-8


print("****多继承使用super().__init__发生的状态****")
class Parent(object):
    def __init__(self, name, *args, **kwargs):
        print("parent的init开始被调用")
        self.name = name
        print("parent的init结束被调用")


class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):
        print("Son1的init开始被调用")
        self.age = age
        super().__init__(name, *args, **kwargs)
        print("Son1的init结束被调用")


class Son2(Parent):
    def __init__(self, name, gender, *args, **kwargs):
        print("Son2的init开始被调用")
        super.__init__(name, *args, **kwargs)
        self.gender = gender
        print("Son2的init结束被调用")


class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        print("Grandson的init开始被调用")
        super().__init__(name, age, gender)
        print("Grandson的init结束被调用")


print(Grandson.__mro__)


gs = Grandson('grandson', 12, '男')
print('姓名:', gs.name)
print('年龄:', gs.age)
print('性别:', gs.gender)
print("****多继承使用super().__init__发生的状态****")
