from math import exp

def evalClassificationMultiClass(realLabels, computedLabels, labels):
    acc = 0
    correct = 0
    for i in range(len(realLabels)):
        if realLabels[i] == computedLabels[i]:
            correct += 1
    acc = correct / len(realLabels)
    precision = []
    recall = []
    x1 = []
    x2 = []
    for label in labels:
        TP = 0
        FP = 0
        TN = 0
        FN = 0
        for i in range(len(realLabels)):
            if realLabels[i] == label and computedLabels[i] == label:
                TP += 1
            if realLabels[i] != label and computedLabels[i] == label:
                FP += 1
            if realLabels[i] != label and computedLabels[i] != label:
                TN += 1
            if realLabels[i] == label and computedLabels[i] != label:
                FN += 1
        if(TP+FP == 0):
            precision.append((1,label))
        else:
            precision.append((TP / (TP + FP),label))
        if(TP+FN == 0):
            recall.append((1,label))
        else:
            recall.append((TP / (TP + FN),label))
        # x1.append(TN/(TN+FN))
        # x2.append(TN/(TN+FP))

    return acc, precision, recall

class Regression:
    def __init__(self):
        self.intercept_ = 0.0
        self.coef_ = []

    def fitBatch(self, x, y,className, learningRate = 0.1, noEpochs = 100):
        self.coef_ = [0.0 for _ in range(len(x[0]) + 1)]  # beta or w coefficients y = w0 + w1 * x1 + w2 * x2 + ...
        aux = []
        for nume in y:
            if (nume == className):
                verif = 1
            else:
                verif = 0
            aux.append(verif)
        y = aux
        for epoch in range(noEpochs):
            print(epoch)
            fields = [0.0 for _ in range(len(x[0]) + 1)]
            for i in range(len(x)):  # pt fiecare inregistrare
                ycomputed = self.sigmoid(self.eval(x[i], self.coef_))  # estimate the output , x[i] - array of 4 info
                crtError = ycomputed - y[i]  # compute the error for the current sample-un rand de gdp/freedom + output
                for j in range(0,len(x[0])):
                    fields[j+1] = fields[j+1] + crtError * x[i][j]
                fields[0] =  fields[0] + crtError * 1
            for j in range(0, len(x[0])):  # update the coefficients
                self.coef_[j+1] = self.coef_[j+1] - learningRate * fields[j+1] / len(x)
            self.coef_[0] = self.coef_[0] - learningRate * fields[0] / len(x)
        self.intercept_ = self.coef_[0]
        self.coef_ = self.coef_[1:]




    def sigmoid(self,x):
        return 1 / (1 + exp(-x))

    def eval(self, xi, coef):
        yi = coef[0]
        for j in range(len(xi)):
            yi += coef[j + 1] * xi[j]
        return yi

    def predict(self,input):
        computedLabels = []
        threshold = 0.5
        coefficients = [self.intercept_] + [c for c in self.coef_]
        for sample in input:
            computedFloatValue = self.eval(sample, coefficients)
            computedValue = self.sigmoid(computedFloatValue)
            # if computedValue < threshold:
            #     computedLabel = 0
            # else:
            #     computedLabel = 1
            computedLabels.append(computedValue)
        return computedLabels
