

class UserInterface(object):
    def __init__(self,Service):
        self.__Service = Service

    def run(self):
        size = int(input("Give the population size: "))
        generations = int(input("give the number of generations: "))
        self.__Service.functie(size,generations)