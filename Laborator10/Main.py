
# Main
import numpy as np

from NeuralNetwork.NeuralNetwork import NeuralNetwork
from NeuralNetworkNumpy.NeuralNetworkNumpy import NeuralNetworkNumpy
from Read.Read import *
from SepiaCreator.SepiaCreator import transformImages
from random import random, seed

if __name__ == "__main__":
    # Test training backprop algorithm
    # data-ul meu trebuie sa fie o matrice
    # pe fiecare linie sa fie valorile unei poze , aka toate alea 1600 * 3 (xd) , plus valoarea de 0 sau 1 daca e sau nu sepia

    # matricea pozelor
    data = getMatrix()
    #train
    lungime = len(data)/2
    # array de poze normale
    normal = data[:50]
    # array de poze sepia
    sepia = data[50:]
    indexes = [i for i in range(50)]
    trainNormal = np.random.choice(indexes, int(0.8 * len(normal)), replace=False)
    trainSepia = np.random.choice(indexes, int(0.8 * len(sepia)), replace=False)

    testNormal = [i for i in indexes if i not in trainNormal]
    testSepia = [i for i in indexes if i not in trainSepia]
    # 50 * 0.8
    trainNormal = [normal[i] for i in trainNormal]
    trainSepia = [sepia[i] for i in trainSepia]
    #test
    # 50 * 0.2
    testNormal = [normal[i] for i in testNormal]
    testSepia = [sepia[i] for i in testSepia]
    #training
    trainData = [y for x in [trainNormal, trainSepia] for y in x]
    testData = [y for x in [testNormal, testSepia] for y in x]
    nrInputs = len(trainData[0]) - 1
    nrOutputs = len(set([row[-1] for row in trainData]))
    #neural network
    ANN = NeuralNetwork()
    networkTrain = ANN.initializeNetwork(nrInputs, 16, nrOutputs,2)
    ANN.trainNetwork(networkTrain, trainData,3,100, nrOutputs,testData)
    for layer in networkTrain:
        print(layer)
    # i = 0
    # s = 0
    # for row in trainData:
    #     prediction = ANN.predict(networkTrain, row)
    #     print('Expected=%d, Got=%d' % (row[-1], prediction))
    #     if (row[-1] == prediction):
    #         s = s + 1
    #     i = i + 1
    # print(s / i * 100)
    # #testing

    # i=0
    # s= 0
    # nrInputs = len(testData[0]) - 1
    # nrOutputs = len(set([row[-1] for row in testData]))
    # networkTest = ANN.initializeNetwork(nrInputs, 2, nrOutputs,2)
    # for row in testData:
    #     prediction = ANN.predict(networkTest, row)
    #     print('Expected=%d, Got=%d' % (row[-1], prediction))
    #     if(row[-1] == prediction):
    #         s = s + 1
    #     i = i+1
    # print(s/i*100)



# data = [[2.7810836, 2.550537003, 0],
    #            [1.465489372, 2.362125076, 0],
    #            [3.396561688, 4.400293529, 0],
    #            [1.38807019, 1.850220317, 0],
    #            [3.06407232, 3.005305973, 0],
    #            [7.627531214, 2.759262235, 1],
    #            [5.332441248, 2.088626775, 1],
    #            [6.922596716, 1.77106367, 1],
    #            [8.675418651, -0.242068655, 1],
    #            [7.673756466, 3.508563011, 1]]