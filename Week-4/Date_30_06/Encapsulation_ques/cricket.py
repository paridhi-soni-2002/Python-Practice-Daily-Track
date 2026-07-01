class Player:

    def __init__(self):
        self.__runs = 0
        self.__matches = 0

    def add_runs(self, runs):
        self.__runs += runs

    def add_match(self):
        self.__matches += 1

    def batting_average(self):

        if self.__matches == 0:
            return 0

        return self.__runs / self.__matches


obj = Player()

obj.add_runs(150)
obj.add_match()
obj.add_match()

print(obj.batting_average())