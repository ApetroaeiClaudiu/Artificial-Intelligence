
from math import sqrt
from random import  randint

from Regression.Regression import Regression, evalClassificationMultiClass


class KMeansCluster:
    def __init__(self,nrOfClusters,data,outputs,epochs):
        self.data = data
        self.nrOfClusters = nrOfClusters
        self.clusters = [-1] * len(data)
        self.modified = epochs
        self.outputs = outputs


    def distance(self,firstList,secondList):
        sum = 0
        for i,j in zip(firstList,secondList):
            sum = sum + (i-j)*(i-j)
        return sqrt(sum)

    def clustering(self):
        outputvector = []
        accMax= 0
        verif = 'positive'
        bad = 'negative'
        while self.modified > 0 :
            clusters = []
        #atribuim random clusteri
            for _ in range(self.nrOfClusters):
                trying = randint(0, len(self.data) - 1)
                while trying in clusters:
                    trying = randint(0, len(self.data) - 1)
                clusters.append(trying)
            epoch = True
            accMax = 0
            while epoch == True:
                epoch = False
                # pt fiecare propozitie
                # daca indicile propozitiei nu e cluster
                # in vectorul clusters , la propozitia i ii atribuim clusterul
                for i in range(len(self.data)):
                    if i not in clusters:
                        nou = min([(self.distance(self.data[i],self.data[k]),k) for k in clusters])[1]
                        if(self.clusters[i] != nou ):
                            self.clusters[i] = nou
                            epoch = True
                    else:
                        self.clusters[i] = i
                self.compute(clusters)

            coef1 = ['positive' if i == clusters[0] else 'negative' for i in self.clusters]
            coef2 = ['negative' if i == clusters[0] else 'positive' for i in self.clusters]
            if (self.getError(coef1, self.outputs) < self.getError(coef2, self.outputs)):
                finalComputedOutputs = coef1
                verif = 'positive'
                bad = 'negative'
            else:
                finalComputedOutputs = coef2
                verif = 'negative'
                bad = 'positive'
            labels = ['positive', 'negative']
            acc, precision, recall = evalClassificationMultiClass(self.outputs, finalComputedOutputs, labels)
            if(acc>accMax):
                outputvector = finalComputedOutputs
                accMax = acc
            self.modified = self.modified - 1
        return verif,bad,outputvector

    def predict(self,inputs):
        prediction = []
        ceva = set(self.clusters)
        for i in  range(len(inputs)):
            prediction.append(min([(self.distance(inputs[i],self.data[k]),k) for k in ceva])[1])
        return prediction

    def getError(self,firstList,secondList):
        error = 0
        for t1,t2 in zip(firstList,secondList):
            if(t1!=t2):
                error += 1
        return error

    def compute(self,clusters):
        # pt fiecare cluster
        for pos in clusters:
            # punem in nodes indicii propozitiilor care au drept cluster cel actual
            nodes = [i for i in range(len(self.clusters)) if self.clusters[i] == pos]
            # pt fiecare cuvant
            for i in range(len(self.data[0])):
                mean = 0
                # pt fiecare propozitie din clusterul actual
                for j in nodes:
                    #adunam valorile cuvintelor
                    mean = mean + self.data[j][i]
                if mean != 0 :
                    # impartim valorile la nr de propozitii
                    mean = mean/len(nodes)
                self.data[pos][i] = mean


