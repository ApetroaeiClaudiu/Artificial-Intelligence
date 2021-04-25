import numpy as np
from random import random,shuffle

class NeuralNetwork():

    def initializeNetwork(self,nrInput,nrHidden,nrOutput,nrOfHiddenLayers):
        # layer = vector de dictionare
        # network = vector de layers
        network = list()
        # in layerul hidden avem nrHidden neuroni si fiecare neuron are nrInput weights plus un bias
        # matrice cu nrHidden x nrInput
        if nrOfHiddenLayers == 1:
            hidden = [{'weights': [random() for i in range(nrInput + 1)]} for i in range(nrHidden)]
            network.append(hidden)
        else :
            nrInput = nrInput
            for i in range(nrOfHiddenLayers):
                hidden = [{'weights': [random() for i in range(nrInput + 1)]} for i in range(nrHidden)]
                network.append(hidden)
                nrInput = nrHidden
                nrHidden = nrHidden
        # in layerul output avem nrOutputs neuroni ( pot fi 2 ) si fiecare neuron are nrHidden weights (legaturi catre neuronii din layerul hidden) plus un bias
        # matrice cu nrOutput x nrHidden
        output = [{'weights': [random() for i in range(nrHidden + 1)]} for i in range(nrOutput)]
        network.append(output)
        # reteaua are un layer hidden si unul de output
        return network


    def sigmoid(self,x):
        return 1.0 / (1.0 + np.exp(-x))

    def sigmoidDerivative(self,x):
        return x * (1.0 - x)

    # activation = sum (weights[i] * input[i])  + bias
    def activate(self,weights,inputs):
        # bias-ul e ultima valoare a weight-ului
        activation = weights[-1]
        for i in range(len(weights) - 1):
            #calculam suma
            activation += weights[i] * inputs[i]
        return activation


    # valoarea de output calculata pt un neuron e memorata in 'output'
    # row este o linie , un vector
    def forwardPropagation(self,network,row):
        inputs = row
        for layer in network:
            newInputs = []
            for neuron in layer:
                # calculam valoarea
                activation = self.activate(neuron['weights'],inputs)
                # aplicam sigmoid si retinem in output
                neuron['output'] = self.sigmoid(activation)
                # cream urmatorul layer cu output urile din momentul actual
                newInputs.append(neuron['output'])
            # acest nou vector format in output-urile calculate devine vectorul pe care il folosim sa calculam urmatoarele output-uri
            inputs = newInputs
        # cand am ajuns la output layer , returnam vectorul final
        return inputs


    # eroare = (expected - output ) * sigmoidDerivative(output)
    # eroare = (weightK * errorJ) * sigmoidDerivative(output)
    def backPropagationError(self,network,expected):
        # in ordine inversa ( output -> hidden )
        for i in reversed(range(len(network))):
            # layer-ul actual
            layer = network[i]
            # lista de erori
            errors = list()
            if i != len(network) - 1:
                # pt fiecare neuron din layer
                for j in range(len(layer)):
                    error = 0.0
                    # pt fiecare neuron din layer ul de dinainte ( spre ex pt layer ul hidden , acum trecem in output)
                    for neuron in network[i + 1]:
                        # calculam eroarea specifica neuronilor de dinainte
                        error+=(neuron['weights'][j] * neuron['error'])
                        # in erori punem valorile inainte de sigmoid
                    errors.append(error)
            else:
                # daca layer ul e output
                for j in range(len(layer)):
                    # fiecare neuron
                    neuron = layer[j]
                    # in erori punem valorile inainte de sigmoid
                    errors.append(expected[j] - neuron['output'])
            # la final , pt fiecare neuron al layer ului , ii calculam eroarea cu valoarea memorata anterior inmultita cu sigmoid derivat de output
            for  j in range(len(layer)):
                neuron = layer[j]
                neuron['error'] = errors[j] * self.sigmoidDerivative(neuron['output'])


    # weight = weight  + learningRate * error * input
    # bias = bias + learningRate * error
    # apeleaza dupa ce s-a facut deja forward and backward propagation
    def updateWeights(self,network,row,learningRate):
        # pt fiecare layer
        for i in range(len(network)):
            # stratul de input daca suntem pe primul layer hidden
            inputs = row[:-1]
            if i != 0 :
                # valorile neuronilor de dinainte daca nu suntem pe primul layer
                inputs = [neuron['output'] for neuron in network[i-1]]
            # pt fiecare neuron din layerul actual
            for neuron in network[i]:
                # pt fiecare neuron de dinainte
                for j in range(len(inputs)):
                    # actualizam dupa formula data
                    neuron['weights'][j] += learningRate * neuron['error'] * inputs[j]
                # actualizam si bias-ul cu valoare de input egala cu 1
                neuron['weights'][-1] += learningRate * neuron['error']


    # stochastic GD
    def trainNetwork(self,network,train,learningRate,numberOfEpochs,nrOutputs):
        # pt fiecare epoca
        for epoch in range(numberOfEpochs):
            shuffle(train)
            sumError = 0
            # pt fiecare linie din trainInput
            a = 0
            s = 0
            for row in train:
                # prezicem outputul
                outputs = self.forwardPropagation(network,row)
                # vectorul de valori reale de output
                expected = [0 for i in range(nrOutputs)]
                expected[row[-1]] = 1
                sumError += sum([(expected[i] - outputs[i])**2 for i in range(len(expected))])
                # apelam back propagation
                self.backPropagationError(network,expected)
                # actualizam weight urile
                self.updateWeights(network,row,learningRate)
                # print(row[-1])
                # print(outputs)
                if (outputs[0] > outputs[1]):
                    c = 0
                else :
                    c = 1
                if(c==row[-1]):
                    s += 1
                a += 1
            print("Accuracy : " , str(s/a) )
            # print(outputs)
            # exit(0)
            print('>epoch=%d, learningRate=%.3f, error=%.3f' % (epoch, learningRate, sumError/len(train)))


    def predict(self,network,row):
        outputs = self.forwardPropagation(network,row)
        return outputs.index(max(outputs))
