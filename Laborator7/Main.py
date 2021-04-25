import time as time
import numpy as np
import matplotlib.pyplot as plt
import random as rand
from matplotlib import cm
from sklearn import linear_model
from sklearn.metrics import mean_absolute_error, mean_squared_error
from Read import loadData
from Regression.Regression import Regression


def SklearnRegression(trainGdp,trainFreedom,trainOutputs):
    xx = [[el1, el2] for el1, el2 in zip(trainGdp, trainFreedom)]
    #sgdregression
    regressor = linear_model.LinearRegression()
    # Training the model by using the training inputs and known training outputs
    regressor.fit(xx, trainOutputs)
    w0, w1, w2 = regressor.intercept_, regressor.coef_[0], regressor.coef_[1]
    model = "The model with tool is: f(x) = " + str(w0) + " + " + str(w1) + "*x1 + " + str(w2) + "*x2"
    print(model)
    return regressor

def MyRegression(trainGdp,trainFreedom,trainOutputs):
    regressor = Regression()
    # Training the model by using the training inputs and known training outputs
    regressor.fit(trainGdp,trainFreedom,trainOutputs)
    w0, w1, w2 = regressor.intercept_, regressor.coef_[0], regressor.coef_[1]
    model = "The manual model is: f(x) = " + str(w0) + " + " + str(w1) + "*x1 + " + str(w2) + "*x2"
    print(model)
    return regressor

def plotDataHistogram(x, variableName):
    plt.hist(x, 10)
    plt.title('Histogram of ' + variableName)
    plt.show()

def main():
    gdp,freedom,output = loadData(
        'D:\A-FACULTATE\Anu 2\Sem2\Inteligenta Artificiala\Laborator7\world-happiness\\ranking2017.csv',
        'Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score')
    plotDataHistogram(gdp, 'GDP per Capita')
    plotDataHistogram(freedom, 'Freedom')
    plotDataHistogram(output, 'Happiness Score')
    time.sleep(0.3)

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
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    ax.scatter(trainGdp, trainFreedom, trainOutputs , marker='o', label='Training Data')
    ax.scatter(testGdp, testFreedom, testOutputs, marker='x', label='Testing Data')
    ax.set_xlabel('GDP per Capita')
    ax.set_ylabel('Freedom')
    ax.set_zlabel('Happiness Score')
    plt.title('Training vs Testing')
    plt.legend()
    plt.show()


    regressor = MyRegression(trainGdp,trainFreedom,trainOutputs)
    w0,w1,w2 = regressor.intercept_,regressor.coef_[0],regressor.coef_[1]

    noOfPoints = 50
    xrefGdp = []
    xrefFreedom = []
    valGdp = min(trainGdp)
    stepGdp = (max(trainGdp) - min(trainGdp)) / noOfPoints
    valFreedom = min(trainFreedom)
    stepFreedom = (max(trainFreedom) - min(trainFreedom)) / noOfPoints
    for _ in range(1, noOfPoints):
        xrefGdp.append(valGdp)
        xrefFreedom.append(valFreedom)
        valGdp += stepGdp
        valFreedom += stepFreedom

    yref = [[w0 + w1 * el1 + w2 * el2] for el1,el2 in zip(xrefGdp,xrefFreedom)]

    fig = plt.figure()
    ax = fig.add_subplot(111,projection="3d")
    ax.scatter(trainGdp, trainFreedom, trainOutputs , marker='o', label='Training Data')
    xrefGdp = np.array(xrefGdp)
    xrefFreedom = np.array(xrefFreedom)
    yref = np.array(yref)
    surf = ax.plot_surface(xrefGdp,xrefFreedom,yref,rstride=1,cstride=1 ,linewidth=0,antialiased=False,alpha=.2)
    #ax.scatter(xref1, xref2, yref, c='b', marker='+', label='Learnt Model')
    ax.set_xlabel('GDP per Capita')
    ax.set_ylabel('Freedom')
    ax.set_zlabel('Happiness Score')
    fig.colorbar(surf,shrink=0.5,aspect=5)
    plt.show()
    # Making predictions for testInput data => computed data
    computedTestOutputs = regressor.predict([[x1, x2] for x1, x2 in zip(testGdp, testFreedom)])
    ax = plt.axes(projection="3d")
    ax.scatter(testGdp, testFreedom, computedTestOutputs, c='orange', marker='o', label='Computed Data')
    ax.scatter(testGdp, testFreedom, testOutputs, c='g', marker='^', label='Real Data')
    ax.set_xlabel('GDP per Capita')
    ax.set_ylabel('Freedom')
    ax.set_zlabel('Happiness Score')
    plt.title('Real Data vs. Computed Data')
    plt.legend()
    plt.show()

    regressorTool = SklearnRegression(trainGdp, trainFreedom, trainOutputs)
    computedTestOutputsTool = regressorTool.predict([[x1, x2] for x1, x2 in zip(testGdp, testFreedom)])

    errorSk = mean_squared_error(testOutputs, computedTestOutputsTool)
    errorMy = 0.0
    for t1, t2 in zip(computedTestOutputs, testOutputs):
        errorMy += (t1-t2)**2
    errorMy = errorMy / len(testOutputs)

    print("Error with tool : " , errorSk)
    print("Error with my regression : ", errorMy)

main()