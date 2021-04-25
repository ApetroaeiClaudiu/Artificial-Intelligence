from random import randint, uniform, random,shuffle


# Binary representation
class Chromosome:
    def __init__(self,problParam=None):
        self.__problParam = problParam
        self.__repres = self.__initialize()
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

    def __initialize(self):
        array = []
        for i in range(0,self.__problParam['noNodes']):
            array.append(i)
        shuffle(array)
        return array

    def normalize(self):
        return 0

    def crossover(self, c):
        #recombinare
        rez = []
        for i in range(0,len(self.__repres)):
            rez.append(-99)
        firstPoz = randint(0,len(self.__repres) - 1)
        secondPoz = randint(0,len(self.__repres) - 1)
        while firstPoz == secondPoz:
            secondPoz = randint(0, len(self.__repres) - 1)
        if firstPoz > secondPoz :
            firstPoz,secondPoz = secondPoz,firstPoz
        for i in range(firstPoz,secondPoz + 1):
            rez[i] = self.__repres[i]
        unu = firstPoz
        doi = secondPoz
        contor = secondPoz - firstPoz + 1
        secondPoz = secondPoz + 1
        firstPoz = 0
        poz = secondPoz
        #nr de pozitii completata
        while contor < len(self.__repres):
            if poz == len(self.__repres):
                poz = 0
            if secondPoz <= len(self.__repres) - 1:
                if c.__repres[secondPoz] not in rez :
                    rez[poz] = c.__repres[secondPoz]
                    contor = contor + 1
                    poz = poz + 1
                secondPoz = secondPoz + 1
            else:
                if firstPoz <= len(self.__repres) - 1:
                    if c.__repres[firstPoz] not in rez:
                        rez[poz] = c.__repres[firstPoz]
                        contor = contor + 1
                        poz = poz + 1
                    firstPoz = firstPoz + 1
        new = Chromosome(self.__problParam)
        new.repres = rez
        #print(unu,doi)
        #print(self.__repres,c.__repres,new.__repres)
        return new

    def mutation(self):
        firstPoz = randint(0,len(self.__repres) - 1)
        secondPoz = randint(0,len(self.__repres) - 1)
        while firstPoz == secondPoz:
            secondPoz = randint(0, len(self.__repres) - 1)
        self.__repres[firstPoz],self.__repres[secondPoz] = self.__repres[secondPoz],self.__repres[firstPoz]


    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness