import time as time

import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from Read import loadData
from sklearn.preprocessing import StandardScaler
from Regression.Regression import Regression


def SGDRegression(trainGdp,trainFreedom,trainOutputs):
    if(trainFreedom):
        xx = [[el1, el2] for el1, el2 in zip(trainGdp, trainFreedom)]
        #sgdregression
        regressor = linear_model.SGDRegressor(max_iter=2000,tol=1e-7)
        # Training the model by using the training inputs and known training outputs
        regressor.fit(xx, trainOutputs)
        w0, w1, w2 = regressor.intercept_[0], regressor.coef_[0], regressor.coef_[1]
        model = "The model with tool is: f(x) = " + str(w0) + " + " + str(w1) + "*x1 + " + str(w2) + "*x2"
        print(model)
        return regressor
    else:
        trainGdp = [[el] for el in trainGdp]
        regressor = linear_model.SGDRegressor(max_iter=2000, tol=1e-7)
        # Training the model by using the training inputs and known training outputs
        regressor.fit(trainGdp, trainOutputs)
        w0, w1 = regressor.intercept_[0], regressor.coef_[0]
        model = "The model with tool is: f(x) = " + str(w0) + " + " + str(w1) + "*x1 "
        print(model)
        return regressor


def MyRegression(trainGdp,trainFreedom,trainOutputs):
    if(trainFreedom):
        regressor = Regression()
        # Training the model by using the training inputs and known training outputs
        trainInputs = [[el1,el2] for el1,el2 in zip(trainGdp,trainFreedom)]
        regressor.fit(trainInputs,trainOutputs)
        w0, w1, w2 = regressor.intercept_, regressor.coef_[0], regressor.coef_[1]
        model = "The manual model is: f(x) = " + str(w0) + " + " + str(w1) + "*x1 + " + str(w2) + "*x2"
        print(model)
        return regressor
    else:
        trainGdp = [[el] for el in trainGdp]
        regressor = Regression()
        regressor.fit(trainGdp, trainOutputs)
        w0, w1 = regressor.intercept_, regressor.coef_[0]
        model = "The manual model is: f(x) = " + str(w0) + " + " + str(w1) + "*x1 "
        print(model)
        return regressor

def plotDataHistogram(x, variableName):
    plt.hist(x, 10)
    plt.title('Histogram of ' + variableName)
    plt.show()

def plot3Ddata(x1Train, x2Train, yTrain, x1Model = None, x2Model = None, yModel = None, x1Test = None, x2Test = None, yTest = None, title = None):
    ax = plt.axes(projection = '3d')
    if (x1Train):
        plt.scatter(x1Train, x2Train, yTrain, c = 'r', marker = 'o', label = 'train data')
    if (x1Model):
        plt.scatter(x1Model, x2Model, yModel, c = 'b', marker = '_', label = 'learnt model')
    if (x1Test):
        plt.scatter(x1Test, x2Test, yTest, c = 'g', marker = '^', label = 'test data')
    plt.title(title)
    ax.set_xlabel("capita")
    ax.set_ylabel("freedom")
    ax.set_zlabel("happiness")
    plt.legend()
    plt.show()

def plotData(x1, y1, x2 = None, y2 = None, x3 = None, y3 = None, title = None):
    plt.plot(x1, y1, 'ro', label = 'train data')
    if (x2):
        plt.plot(x2, y2, 'b-', label = 'learnt model')
    if (x3):
        plt.plot(x3, y3, 'g^', label = 'test data')
    plt.title(title)
    plt.legend()
    plt.show()

def scale01(features):
    minFeat = min(features)
    maxFeat = max(features)
    scaledFeatures = [(feat - minFeat) / (maxFeat - minFeat) for feat in features]
    return scaledFeatures


def getMeanValue(features):
    return sum(features) / len(features)
def getStdDevValue(features,meanValue):
    return (1 / len(features) * sum([(feat - meanValue) ** 2 for feat in features])) ** 0.5
def statisticalNormalisation(features,meanValue,stdDevValue):
    normalisedFeatures = [(feat - meanValue) / stdDevValue for feat in features]
    return normalisedFeatures



def mainUnivariata():
    gdp, freedom, output = loadData(
        'D:\A-FACULTATE\Anu 2\Sem2\Inteligenta Artificiala\Laborator8\world-happiness\\ranking2017.csv',
        'Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score')
    plotDataHistogram(gdp, 'GDP per Capita')
    plotDataHistogram(output, 'Happiness Score')
    plotData(gdp, output,[], [], [], [], 'capita  vs happiness')
    np.random.seed(5)
    # info
    indexes = [i for i in range(len(gdp))]
    trainSample = np.random.choice(indexes, int(0.8 * len(gdp)), replace=False)
    testSample = [i for i in indexes if i not in trainSample]
    # train
    trainGdp = [gdp[i] for i in trainSample]
    trainOutputs = [output[i] for i in trainSample]
    # test
    testGdp = [gdp[i] for i in testSample]
    testOutputs = [output[i] for i in testSample]
    # Plotting training data and testing data
    plotData(trainGdp, trainOutputs, [], [], testGdp, testOutputs, "train and test data before normalisation")

    meanValueGdp = getMeanValue(trainGdp)
    stDevGdp = getStdDevValue(trainGdp, meanValueGdp)
    trainGdp = statisticalNormalisation(trainGdp, meanValueGdp, stDevGdp)
    meanValueOutputs = getMeanValue(trainOutputs)
    stDevOutputs = getStdDevValue(trainOutputs, meanValueOutputs)
    trainOutputs = statisticalNormalisation(trainOutputs, meanValueOutputs, stDevOutputs)
    testGdp = statisticalNormalisation(testGdp, meanValueGdp, stDevGdp)
    testOutputs = statisticalNormalisation(testOutputs, meanValueOutputs, stDevOutputs)

    plotData(trainGdp, trainOutputs, [], [], testGdp, testOutputs, "train and test data after normalisation")

    regressor = MyRegression(trainGdp,[], trainOutputs)
    w0, w1 = regressor.intercept_, regressor.coef_[0]

    noOfPoints = 1000
    xrefGdp = []
    valGdp = min(trainGdp)
    step1 = (max(trainGdp) - min(trainGdp)) / noOfPoints
    for _ in range(1, noOfPoints):
        xrefGdp.append(valGdp)
        valGdp += step1

    yref = [w0 + w1 * el1  for el1 in xrefGdp]
    plotData(trainGdp, trainOutputs, xrefGdp, yref, [], [], title = "train data and model")

    # plot3Ddata(trainGdp,trainFreedom, trainOutputs,xrefGdp, xrefFreedom, yref, [], [], [], 'train data and the learnt model')

    # Making predictions for testInput data => computed data
    computedTestOutputs = regressor.predictUni([[x1] for x1 in testGdp])
    plotData([], [], testGdp, computedTestOutputs, testGdp, testOutputs, "predictions vs real test data")

    regressTool = SGDRegression(trainGdp,[], trainOutputs)
    computedTestOutputsTool = regressTool.predict([[x1] for x1 in testGdp])

    errorSk = mean_squared_error(testOutputs, computedTestOutputsTool)

    errorMy = 0.0
    for t1, t2 in zip(computedTestOutputs, testOutputs):
        errorMy += (t1 - t2) ** 2
    errorMy = errorMy / len(testOutputs)

    print("Error with tool : ", errorSk)
    print("Error with my regression : ", errorMy)




def mainMultivariata():
    gdp,freedom,output = loadData(
        'D:\A-FACULTATE\Anu 2\Sem2\Inteligenta Artificiala\Laborator7\world-happiness\\ranking2017.csv',
        'Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score')
    plotDataHistogram(gdp, 'GDP per Capita')
    plotDataHistogram(freedom, 'Freedom')
    plotDataHistogram(output, 'Happiness Score')
    plot3Ddata(gdp, freedom, output, [], [], [], [], [], [], 'capita vs freedom vs happiness')
    np.random.seed(5)
    #info
    indexes = [i for i in range(len(gdp))]
    trainSample = np.random.choice(indexes, int(0.8 * len(gdp)), replace=False)
    testSample = [i for i in indexes if i not in trainSample]
    #train
    trainGdp = [gdp[i] for i in trainSample]
    trainFreedom = [freedom[i] for i in trainSample]
    trainOutputs = [output[i] for i in trainSample]
    #test
    testGdp = [gdp[i] for i in testSample]
    testFreedom = [freedom[i] for i in testSample]
    testOutputs = [output[i] for i in testSample]
    # Plotting training data and testing data
    #plot3Ddata(trainGdp,trainFreedom, trainOutputs, [], [], [], testGdp, testFreedom, testOutputs, "train and test data (before normalisation)")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(trainGdp, trainFreedom, trainOutputs, marker='o', label='Training Data')
    ax.scatter(testGdp, testFreedom, testOutputs, marker='x', label='Testing Data')
    ax.set_xlabel('GDP per Capita')
    ax.set_ylabel('Freedom')
    ax.set_zlabel('Happiness Score')
    plt.title('before normalisation')
    plt.legend()
    plt.show()

    meanValueGdp = getMeanValue(trainGdp)
    stDevGdp = getStdDevValue(trainGdp,meanValueGdp)
    trainGdp = statisticalNormalisation(trainGdp,meanValueGdp,stDevGdp)
    meanValueFreedom = getMeanValue(trainFreedom)
    stDevFreedom = getStdDevValue(trainFreedom, meanValueFreedom)
    trainFreedom = statisticalNormalisation(trainFreedom,meanValueFreedom,stDevFreedom)
    meanValueOutputs = getMeanValue(trainOutputs)
    stDevOutputs = getStdDevValue(trainOutputs, meanValueOutputs)
    trainOutputs = statisticalNormalisation(trainOutputs,meanValueOutputs,stDevOutputs)

    testGdp = statisticalNormalisation(testGdp,meanValueGdp,stDevGdp)
    testFreedom = statisticalNormalisation(testFreedom,meanValueFreedom,stDevFreedom)
    testOutputs = statisticalNormalisation(testOutputs,meanValueOutputs,stDevOutputs)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(trainGdp, trainFreedom, trainOutputs, marker='o', label='Training Data')
    ax.scatter(testGdp, testFreedom, testOutputs, marker='x', label='Testing Data')
    ax.set_xlabel('GDP per Capita')
    ax.set_ylabel('Freedom')
    ax.set_zlabel('Happiness Score')
    plt.title('after normalisation')
    plt.legend()
    plt.show()
    #plot3Ddata(trainGdp,trainFreedom, trainOutputs, [], [], [], testGdp, testFreedom, testOutputs, "train and test data (after normalisation)")

    regressor = MyRegression(trainGdp,trainFreedom,trainOutputs)
    w0,w1,w2 = regressor.intercept_,regressor.coef_[0],regressor.coef_[1]

    noOfPoints = 50
    xrefGdp = []
    valGdp = min(trainGdp)
    step1 = (max(trainGdp) - min(trainGdp)) / noOfPoints
    for _ in range(1, noOfPoints):
        for _ in range(1, noOfPoints):
            xrefGdp.append(valGdp)
        valGdp += step1

    xrefFreedom = []
    valFreedom = min(trainFreedom)
    step2 = (max(trainFreedom) - min(trainFreedom)) / noOfPoints
    for _ in range(1, noOfPoints):
        aux = valFreedom
        for _ in range(1, noOfPoints):
            xrefFreedom.append(aux)
            aux += step2

    yref = [w0 + w1 * el1 + w2 * el2 for el1,el2 in zip(xrefGdp,xrefFreedom)]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(trainGdp, trainFreedom, trainOutputs, marker='o', label='Training Data')
    ax.scatter(xrefGdp,xrefFreedom,yref, marker='x', label='Testing Data')
    ax.set_xlabel('GDP per Capita')
    ax.set_ylabel('Freedom')
    ax.set_zlabel('Happiness Score')
    plt.title('train data vs learnt model')
    plt.legend()
    plt.show()
    #plot3Ddata(trainGdp,trainFreedom, trainOutputs,xrefGdp, xrefFreedom, yref, [], [], [], 'train data and the learnt model')

    # Making predictions for testInput data => computed data
    computedTestOutputs = regressor.predict([[x1, x2] for x1, x2 in zip(testGdp, testFreedom)])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(testGdp, testFreedom, computedTestOutputs, marker='o', label='Training Data')
    ax.scatter(testGdp, testFreedom, testOutputs, marker='x', label='Testing Data')
    ax.set_xlabel('GDP per Capita')
    ax.set_ylabel('Freedom')
    ax.set_zlabel('Happiness Score')
    plt.title('predicitions vs real data')
    plt.legend()
    plt.show()
    #plot3Ddata([], [], [],testGdp,testFreedom, computedTestOutputs, testGdp,testFreedom, testOutputs, 'predictions vs real test data')

    regressTool = SGDRegression(trainGdp,trainFreedom,trainOutputs)
    computedTestOutputsTool = regressTool.predict([[x1, x2] for x1, x2 in zip(testGdp, testFreedom)])

    errorSk = mean_squared_error(testOutputs, computedTestOutputsTool)

    errorMy = 0.0
    for t1, t2 in zip(computedTestOutputs, testOutputs):
        errorMy += (t1-t2)**2
    errorMy = errorMy / len(testOutputs)

    print("Error with tool : " , errorSk)
    print("Error with my regression : ", errorMy)

def main():
    comm = int(input("1-univariata \n2-multivariata \n"))
    if(comm==1):
        mainUnivariata()
    if(comm==2):
        mainMultivariata()

main()