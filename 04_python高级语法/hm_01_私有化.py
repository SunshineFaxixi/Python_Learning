#coding=utf-8


class Person(object):
    def __init__(self, name, age, taste):
        self.name = name
        self._age = age
        self.__taste = taste


    def showperson(self):
        print(self.name)
        print(self._age)
        print(self.__taste)


    def dowork(self):
        self._work()
        self.__away()


    def _work(self):
        print('my_work')


    def __away(self):
        print('my __away')


class Student(Person):
    def construction(self, name, age, taste):
        self.name = name
        self._age = age
        self.__taste = taste


    def showstudent(self):
        print(self.name)
        print(self._age)
        print(self.__taste)


    @staticmethod
    def testbug():
        _Bug.showbug()


class _Bug(object):
    @staticmethod
    def showbug():
        print("showbug")


s1 = Student('jack', 25, 'football')
s1.showperson()
print("*" * 20)

# s1.showstudent()  无法访问__taste
s1.construction('rose', 30, 'basketball')
s1.showperson()
print("*" * 20)

s1.showstudent()
print("*" * 20)

Student.testbug()

