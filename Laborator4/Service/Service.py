from Domain.GA import GA


class Service:
    def __init__(self,Repository):
        self.Repository = Repository
        self.data = self.Repository.getData()


    def fitness(self,path,param):
        noNodes = param['noNodes']
        mat = param['matrix']
        cost = 0
        for i in range(0,len(path) - 1):
            cost = cost + mat[path[i]][path[i+1]]
        cost = cost + mat[path[-1]][path[0]]
        return cost

    def functie(self,size,generations):
        dic = {}
        dic['noNodes'] = self.Repository.getNodes()
        dic['matrix'] = self.data
        dic['popSize'] = size
        dic['function'] = self.fitness
        ga = GA(dic,dic)
        ga.initialisation()
        ga.evaluation()
        for i in range(0,generations):
            bestChromo = ga.bestChromosome()
            ga.oneGenerationSteadyState()
            #print(bestChromo.repres)
            print("Generation " + str(i) + " has fitness " + str(bestChromo.fitness))
