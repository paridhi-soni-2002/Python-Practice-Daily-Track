class Laptop:

    def __init__(self):
        self.__volume = 50

    def increase_volume(self):

        if self.__volume < 100:
            self.__volume += 10

    def decrease_volume(self):

        if self.__volume > 0:
            self.__volume -= 10

    def get_volume(self):
        return self.__volume


obj = Laptop()

obj.increase_volume()

obj.decrease_volume()

print(obj.get_volume())