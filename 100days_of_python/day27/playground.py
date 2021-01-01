# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# res = add(1, 2, 3, 4, 5, 19)
# print(res)


# def calculator(n, **kwargs):
#     # n += kwargs["add"]
#     # n *= kwargs["multiply"]
#     n += kwargs.get("add")
#     n *= kwargs.get("multiply")
#     print(n)
# calculator(2, add=3, multiply=10)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(model="GT-R")
print(my_car.make)