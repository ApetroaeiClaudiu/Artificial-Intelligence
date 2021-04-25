from random import *

class Ant:
    def __init__(self, problParam=None):
        self.__problParam = problParam
        #initializam reprezentarea furnicii doar cu un oras ales aleatoriu
        self.__repres = [randint(0, self.__problParam["nrNodes"] - 1)]
        self.__length = 0.0
        #initializam matrice feromon cu 0
        self.__pheromoneLvl = [[0 for _ in range(self.__problParam["nrNodes"])] for _ in range(self.__problParam["nrNodes"])]

    @property
    def pheromoneLvl(self):
        return self.__pheromoneLvl

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, l):
        self.__length = l

    @property
    def repres(self):
        return self.__repres

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    def next(self):
        rez = []
        total = 0.0
        #pt fiecare oras
        for j in range(self.__problParam["nrNodes"]):
            rez.append(0)
            #daca orasul nu e in reprezentare
            if j not in self.__repres:
                #daca feromonul drumului de la ultimul element din reprezentare catre j este zero
                if self.__problParam["pheromone"][self.__repres[-1]][j] == 0:
                    t = 1
                else:
                    #tour construction
                    t = self.__problParam["pheromone"][self.__repres[-1]][j]**self.__problParam["alfa"]
                n = (1 / self.__problParam["matrix"][self.__repres[-1]][j])**self.__problParam["beta"]
                rez[j] = t*n
                total += rez[j]
        prob = random()
        #ruleta
        if prob < self.__problParam["pseudo"]:
            max = 0
            city = 0
            for i in range(len(rez)):
                if rez[i] > max:
                    max = rez[i]
                    city = i
        else:
            probs = []
            for j in range(self.__problParam["nrNodes"]):
                if rez[j] != 0:
                    probs.append([j, rez[j] / total])
            probs.sort(key=lambda x: x[1])
            cumsum = []
            for i in range(len(probs)):
                suma = 0.0
                for s in cumsum:
                    suma += s[1]
                cumsum.append([probs[i][0], suma + probs[i][1]])
            if cumsum[-1][1] != 1:
                cumsum[-1][1] = 1
            path = random()
            city = 0
            for s in cumsum:
                if path < s[1]:
                    city = s[0]
                    break
        self.__repres.append(city)
        self.__pheromoneLvl[self.__repres[-2]][self.__repres[-1]] = 1
        self.__pheromoneLvl[self.__repres[-1]][self.__repres[-2]] = 1
        self.__length += self.__problParam["matrix"][self.__repres[-2]][self.__repres[-1]]
        return

    def retreat(self):
        self.__repres.append(self.__repres[0])
        self.__pheromoneLvl[self.__repres[-2]][self.__repres[-1]] = 1
        self.__pheromoneLvl[self.__repres[-1]][self.__repres[-2]] = 1
        self.__length += self.__problParam["matrix"][self.__repres[-2]][self.__repres[-1]]
        return

    def __str__(self):
        return "\nAnt: " + str(self.__repres) + " Length: " + str(self.__length)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres