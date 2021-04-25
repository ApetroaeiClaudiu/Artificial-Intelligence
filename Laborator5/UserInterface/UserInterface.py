from Service import *

class UserInterface:
    def __init__(self,Service):
        self.__Service = Service

    def run(self):
        ants = int(input("Number of ants: "))
        generations = int(input("Number of generations: "))
        # print("Normal : \n")
        # result, bestIteration = self.__Service.Solve(ants,generations,"D:\A-FACULTATE\Anu 2\Sem2\Inteligenta Artificiala\Laborator5\out.txt")
        # print("Shortest path: ",result.repres)
        # print("Length: ",result.length)
        # print("On Iteration: ",bestIteration)
        print("Dynamic : \n")
        result, bestIteration = self.__Service.SolveDynamic(ants, generations,"D:\A-FACULTATE\Anu 2\Sem2\Inteligenta Artificiala\Laborator5\out.txt")
        print("Shortest path: ", result.repres)
        print("Length: ", result.length)
        print("On Iteration: ", bestIteration)