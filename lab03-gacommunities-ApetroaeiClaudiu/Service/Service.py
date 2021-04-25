from Domain.GA import GA
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

class Service(object):
    def __init__(self,Repository):
        self.Repository = Repository
        self.data = self.Repository.getData()

    def modularity(self,communities, param):
        noNodes = param['noNodes']
        mat = param['matrix']
        degrees = param['degrees']
        noEdges = param['noEdges']
        M = 2 * noEdges
        Q = 0.0
        for i in range(0, noNodes):
            for j in range(0, noNodes):
                if (communities[i] == communities[j]):
                    Q += (mat[i, j] - degrees[i] * degrees[j] / M)
        return Q * 1 / M

    def functie(self,size,generations):
        dic = {}
        dic['noNodes'] = self.data.number_of_nodes()
        dic['matrix'] = nx.to_numpy_matrix(self.data)
        dic['degrees'] = [ x[1] for x in self.data.degree() ]
        dic['noEdges'] = self.data.number_of_edges()
        dic['popSize'] = size
        dic['function'] = self.modularity
        ga = GA(dic)
        ga.initialisation()
        ga.evaluation()
        file = open('D:\A-FACULTATE\Anu 2\Sem2\Inteligenta Artificiala\Laborator3\out.txt', 'w')
        for i in range(0,generations):
            bestChromo = ga.bestChromosome()
            dictionar = {}
            apartenenta = {}
            for j in range(0, len(bestChromo.repres)):
                #dictionar[j] = bestChromo.repres[j]
                dictionar[bestChromo.repres[j]] = 1
            for x in range(0,len(bestChromo.repres)):
                apartenenta[x] = bestChromo.repres[x]
            #print(bestChromo.repres)
            print("Generation " + str(i) + " fitness " + str(bestChromo.fitness) + " Number of communities :" + str(len(dictionar.keys())))
            #file.write("Generation " + str(i) + " fitness " + str(bestChromo.fitness) + " Number of communities :" + str(len(dictionar.keys())) + "\n")
            #print(str(apartenenta))
            #file.write(str(apartenenta) + "\n")

            #print(dictionar)
            #print(str(i) + "," + str(len(dictionar.keys())) + " , " + str(bestChromo.fitness))
            ga.oneGenerationElitism()

        file.close()
        G = self.data
        pos = nx.spring_layout(G)  # compute graph layout
        plt.figure(figsize=(10, 10))  # image is 8 x 8 inches
        nx.draw_networkx_nodes(G, pos, node_size=600, node_color=bestChromo.repres)
        nx.draw_networkx_edges(G, pos, alpha=0.3)
        plt.show(G)
