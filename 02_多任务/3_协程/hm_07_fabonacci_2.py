
class Fabonacci(object):
    def __init__(self, all_num):
        self.all_num = all_num
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.all_num:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1
            return result
        else:
            raise StopIteration


def main():
    fabo = Fabonacci(10)
    for num in fabo:
        print(num)


if __name__ == "__main__":
    main()