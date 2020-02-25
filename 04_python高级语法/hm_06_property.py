class Pager(object):
    def __init__(self, current_page):
        self.current_page = current_page
        self.per_items = 10


    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val


    @property
    def end(self):
        val = self.current_page * self.per_items
        return val


def main():
    p = Pager(1)
    print(p.start)
    print(p.end)


if __name__ == "__main__":
    main()
