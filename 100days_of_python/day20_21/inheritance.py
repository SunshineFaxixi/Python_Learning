class Animal:
    def __init__(self):
        self.num_of_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this under water.")

    def swim(self):
        print("moving in the water.")


fish = Fish()
fish.swim()
fish.breathe()
print(fish.num_of_eyes)