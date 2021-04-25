
from numpy.linalg import inv

class Regression:
    def __init__(self):
        self.intercept_ = 0.0
        self.coef_ = []


    """
        x[i][j]
        x : 
        gdp0 freedom0
        gdp1 freedom1
        
        len(x) = nr inregistrari
        len(x[0]) = nr de feature uri 
        0 0 = eroarea unui rand * prima valoare , eroarea unui rand * a doua valoare 
        1 1 
        2 2
        3 3
    """

    def fit(self, x, y, learningRate = 0.1, noEpochs = 1000):
        self.coef_ = [0.0 for _ in range(len(x[0]) + 1)]  # beta or w coefficients y = w0 + w1 * x1 + w2 * x2 + ...
        for epoch in range(noEpochs):
            fields = [0.0 for _ in range(len(x[0]) + 1)]
            for i in range(len(x)):  # pt fiecare inregistrare
                ycomputed = self.eval(x[i])  # estimate the output , x[i] - array de gdp/freedom
                crtError = ycomputed - y[i]  # compute the error for the current sample-un rand de gdp/freedom + output
                for j in range(0,len(x[0])):
                    fields[j] = fields[j] + crtError * x[i][j]
                fields[len(x[0])] =  fields[len(x[0])] + crtError * 1

            for j in range(0, len(x[0])):  # update the coefficients
                self.coef_[j] = self.coef_[j] - learningRate * fields[j] / len(x)
            self.coef_[len(x[0])] = self.coef_[len(x[0])] - learningRate * fields[len(x[0])] / len(x)
        self.intercept_ = self.coef_[-1]
        self.coef_ = self.coef_[:-1]
        print(self.intercept_)
        print(self.coef_)


    def fit2(self, x, y, learningRate=0.001, noEpochs=1000):
        self.coef_ = [0.0 for _ in range(len(x[0]) + 1)]  # beta or w coefficients y = w0 + w1 * x1 + w2 * x2 + ...
        # self.coef_ = [random.random() for _ in range(len(x[0]) + 1)]    #beta or w coefficients
        for epoch in range(noEpochs):
            # TBA: shuffle the trainind examples in order to prevent cycles
            for i in range(len(x)):  # for each sample from the training data
                ycomputed = self.eval(x[i])  # estimate the output
                crtError = ycomputed - y[i]  # compute the error for the current sample
                for j in range(0, len(x[0])):  # update the coefficients
                    self.coef_[j] = self.coef_[j] - learningRate * crtError * x[i][j]
                self.coef_[len(x[0])] = self.coef_[len(x[0])] - learningRate * crtError * 1
        self.intercept_ = self.coef_[-1]
        self.coef_ = self.coef_[:-1]

    def eval(self, xi):
        yi = self.coef_[-1]
        for j in range(len(xi)):
            yi += self.coef_[j] * xi[j]
        return yi

    def predict(self, x):
        return [self.intercept_ + self.coef_[0] * val[0] + self.coef_[1] * val[1] for val in x]

    def predictUni(self,x):
        return [self.intercept_ + self.coef_[0] * val[0]  for val in x]