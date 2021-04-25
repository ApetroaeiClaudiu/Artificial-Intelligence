from random import randint, uniform


# Binary representation
class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam
        self.__repres = []
        #for _ in range(problParam['noNodes']):
         #   self.__repres.append(randint(0, problParam['noNodes']-1))
        noLeaders = round(0.2 * self.__problParam['noNodes'])
        self.__repres = [None for _ in range(self.__problParam['noNodes'])]
        for i in range(len(self.__repres)):
            if self.__repres[i] is None:
                self.__repres[i] = randint(0, self.__problParam['noNodes']-1)
                rem = self.__problParam['noNodes'] - i
                if uniform(0, 1) <= noLeaders / rem:
                    noLeaders -= 1
                    indices = (self.__problParam['matrix'][i] > 0).nonzero()[1]
                    for j in indices:
                        if self.__repres[j] is None:
                            self.__repres[j] = self.__repres[i]
        self.__fitness = 0.0

    @property
    def repres(self):
        return  self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def normalize(self):
        # 5 1 1 2 2
        # 1 2 2 3 3
        dic = {}
        com = 0
        vector = []
        for i in range(0, len(self.repres)):
            if self.repres[i] not in dic :
                com+=1
                dic[self.repres[i]] = com
            vector.append(dic[self.repres[i]])
        self.repres = vector

    def crossover(self, c):
        #recombinare
        self.normalize()
        c.normalize()
        poz = randint(0,self.__problParam['noNodes'] - 1)
        rezultat = []
        for i in range(0, poz):
            rezultat.append(self.__repres[i])
        for j in range (poz,len(c.repres)):
            rezultat.append(c.repres[j])
        c = Chromosome(self.__problParam)
        c.repres = rezultat
        return c

    def mutation(self):
        #random resetting
        vecini = []
        poz = randint(0,self.__problParam['noNodes']-1)
        for i in range(0,self.__problParam['noNodes']):
            if self.__problParam['matrix'][poz, i] > 0 :
                vecini.append(i)
        unu = randint(0, len(vecini) - 1)
        self.__repres[poz] = self.__repres[vecini[unu]]


    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness