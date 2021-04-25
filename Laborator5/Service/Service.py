from Domain import *
from Domain.ACO import ACO


class Service:
    def __init__(self,Repository):
        self.Repository = Repository
        self.data = self.Repository.getData()


    def startzero(self,repres):
        while repres[0] != 0:
            repres.insert(0, repres.pop())
        return repres


    def Solve(self, ants, it, outFile):
        global rez
        bestiteration = 0
        param = {"nrAnts": ants, "nrIterations": it}
        problParam = self.data
        test = ACO(param)
        for i in range(param["nrIterations"]):
            test.initialisation(problParam)
            if i == 0:
                rez = test.bestAnt()
            for j in range(problParam["nrNodes"] - 1):
                test.oneStep()
            problParam = test.lastStep()
            print(test.bestAnt())
            print("Iteration:  ", i + 1, "\n")
            if test.bestAnt().length < rez.length:
                rez = test.bestAnt()
                bestiteration = i + 1
        rez.repres.pop()
        rez.repres = self.startzero(rez.repres)
        self.Repository.writerez(rez, outFile)
        return rez, bestiteration


    def SolveDynamic(self, ants, it, outFile):
        global rez
        bestiteration = 0
        param = {"nrAnts": ants, "nrIterations": it}
        problParam = self.data
        test = ACO(param)
        tens = [[False for _ in range(problParam["nrNodes"])] for _ in range(problParam["nrNodes"])]
        for i in range(param["nrIterations"]):
            test.initialisation(problParam)
            if i == 0:
                rez = test.bestAnt()
            for j in range(problParam["nrNodes"] - 1):
                test.oneStep()
            problParam = test.lastStep()
            print(test.bestAnt())
            print("Iteration ", i + 1, "\n")
            if test.bestAnt().length < rez.length:
                rez = test.bestAnt()
                bestiteration = i + 1
            for a in range(problParam["nrNodes"]):
                for b in range(problParam["nrNodes"]):
                    if problParam["pheromone"][a][b] > problParam["dynamic"]:
                        if tens[a][b] == False:
                            problParam["matrix"][a][b] += 10
                            tens[a][b] = True
                            problParam["pheromone"][a][b] = 1
            if i == param["nrIterations"]/2:
                for a in range(problParam["nrNodes"]):
                    for b in range(problParam["nrNodes"]):
                        if tens[a][b] == True:
                            problParam["matrix"][a][b] -= 10
                        else:
                            tens[a][b] = True
        rez.repres.pop()
        rez.repres = self.startzero(rez.repres)
        self.Repository.writerez(rez,outFile)
        return rez, bestiteration