from Domain.Ant import Ant


class ACO:
    def __init__(self, param=None):
        self.__param = param
        self.__problParam = {}
        self.__population = []

    @property
    def population(self):
        return self.__population

    def initialisation(self, problParam):
        self.__population.clear()
        self.__problParam = problParam
        for _ in range(0, self.__param["nrAnts"]):
            a = Ant(self.__problParam)
            self.__population.append(a)

    def oneStep(self):
        for ant in self.__population:
            ant.next()
        return

    def lastStep(self):
        for ant in self.__population:
            ant.retreat()
        for i in range(self.__problParam["nrNodes"]):
            for j in range(self.__problParam["nrNodes"]):
                newPheromone = 0
                for ant in self.__population:
                    if ant.pheromoneLvl[i][j] == 1:
                        newPheromone = newPheromone +  1 / ant.length
                self.__problParam["pheromone"][i][j] += (1 - self.__problParam["evaporation"])*self.__problParam["pheromone"][i][j] + newPheromone
        return self.__problParam

    def bestAnt(self):
        best = self.__population[0]
        for c in self.__population:
            if c.length < best.length:
                best = c
        return best

    def worstAnt(self):
        worst = self.__population[0]
        for c in self.__population:
            if c.length > worst.length:
                worst = c
        return worst