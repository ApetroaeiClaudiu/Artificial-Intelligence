import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from Read import loadData
from Regression.Regression import Regression, evalClassificationMultiClass
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

def plotDataHistogram(x, variableName):
    plt.hist(x, 10)
    plt.title('Histogram of ' + variableName)
    plt.show()


def getMeanValue(features):
    return sum(features) / len(features)
def getStdDevValue(features,meanValue):
    return (1 / len(features) * sum([(feat - meanValue) ** 2 for feat in features])) ** 0.5
def statisticalNormalisation(features,meanValue,stdDevValue):
    normalisedFeatures = [(feat - meanValue) / stdDevValue for feat in features]
    return normalisedFeatures


def main():
    SepalLength,SepalWidth,PetalLength,PetalWidth,outputs = loadData("D:\A-FACULTATE\Anu 2\Sem2\Inteligenta Artificiala\Laborator9\data\iris.data",'SepalLength','SepalWidth','PetalLength','PetalWidth','ClassName')
    plotDataHistogram(SepalLength,'Sepal Length')
    plotDataHistogram(SepalWidth, 'Sepal Width')
    plotDataHistogram(PetalLength, 'Petal Length')
    plotDataHistogram(PetalWidth, 'Petal Length')
    plotDataHistogram(outputs, 'Class Name')
    np.random.seed(5)

    indexes = [i for i in range(len(SepalLength))]
    trainSample = np.random.choice(indexes, int(0.8 * len(SepalLength)), replace=False)
    testSample = [i for i in indexes if i not in trainSample]

    #train
    trainSepalLength = [SepalLength[i] for i in trainSample]
    trainSepalWidth = [SepalWidth[i] for i in trainSample]
    trainPetalLength = [PetalLength[i] for i in trainSample]
    trainPetalWidth = [PetalWidth[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]
    #test
    testSepalLength = [SepalLength[i] for i in testSample]
    testSepalWdith = [SepalWidth[i] for i in testSample]
    testPetalLength = [PetalLength[i] for i in testSample]
    testPetalWidth = [PetalWidth[i] for i in testSample]
    testOutputs = [outputs[i] for i in testSample]

    plotDataHistogram(trainOutputs, 'train classes')
    plotDataHistogram(testOutputs, 'test classes')

    #normalizing data
    meanValueSepalLength = getMeanValue(trainSepalLength)
    stDevSepalLength = getStdDevValue(trainSepalLength,meanValueSepalLength)
    trainSepalLength = statisticalNormalisation(trainSepalLength,meanValueSepalLength,stDevSepalLength)

    meanValueSepalWidth = getMeanValue(trainSepalWidth)
    stDevSepalWidth = getStdDevValue(trainSepalWidth, meanValueSepalWidth)
    trainSepalWidth = statisticalNormalisation(trainSepalWidth, meanValueSepalWidth, stDevSepalWidth)

    meanValuePetalLength = getMeanValue(trainPetalLength)
    stDevPetalLength = getStdDevValue(trainPetalLength, meanValuePetalLength)
    trainPetalLength = statisticalNormalisation(trainPetalLength, meanValuePetalLength, stDevPetalLength)

    meanValuePetalWdith = getMeanValue(trainPetalWidth)
    stDevPetalWidth = getStdDevValue(trainPetalWidth, meanValuePetalWdith)
    trainPetalWidth = statisticalNormalisation(trainPetalWidth, meanValuePetalWdith, stDevPetalWidth)

    #normalizing test data
    testSepalLength = statisticalNormalisation(testSepalLength,meanValueSepalLength,stDevSepalLength)
    testSepalWdith = statisticalNormalisation(testSepalWdith,meanValueSepalWidth,stDevSepalWidth)
    testPetalLength = statisticalNormalisation(testPetalLength,meanValueSepalLength,stDevPetalLength)
    testPetalWidth = statisticalNormalisation(testPetalWidth,meanValuePetalWdith,stDevPetalWidth)

    #the 4 inputs in one matrix
    trainInputs = [[x1, x2, x3, x4 ] for x1, x2,x3,x4 in
                   zip(trainSepalLength, trainSepalWidth, trainPetalLength, trainPetalWidth)]
    testInputs = [[x1, x2, x3, x4 ] for x1, x2,x3,x4 in zip(testSepalLength,testSepalWdith,testPetalLength,testPetalWidth)]

    print("Models : ----------")
    #setosa regressor
    regressorSetosa = Regression()
    regressorSetosa.fitBatch(trainInputs, trainOutputs, 'Iris-setosa')
    w0, w1, w2, w3, w4 = regressorSetosa.intercept_, regressorSetosa.coef_[0], regressorSetosa.coef_[1], regressorSetosa.coef_[2], \
                         regressorSetosa.coef_[3]
    model = "The manual model for setosa is: f(x) = " + str(w0) + " + " + str(w1) + "*x1 + " + str(w2) + "*x2 + " + str(w3) + "*x3 + "+ str(w4) + "*x4 "
    print(model)
    #versi regressor
    regressorVersi = Regression()
    regressorVersi.fitBatch(trainInputs, trainOutputs, 'Iris-versicolor')
    w0, w1, w2, w3, w4 = regressorVersi.intercept_, regressorVersi.coef_[0], regressorVersi.coef_[1], regressorVersi.coef_[2], \
                         regressorVersi.coef_[3]
    model = "The manual model for versicolor is: f(x) = " + str(w0) + " + " + str(w1) + "*x1 + " + str(w2) + "*x2 + " + str(w3) + "*x3 + "+ str(w4) + "*x4 "
    print(model)
    #virginica regressor
    regressorVirginica = Regression()
    regressorVirginica.fitBatch(trainInputs, trainOutputs, 'Iris-virginica')
    w0, w1, w2, w3, w4 = regressorVirginica.intercept_, regressorVirginica.coef_[0], regressorVirginica.coef_[1],regressorVirginica.coef_[2], \
                         regressorVirginica.coef_[3]
    model = "The manual model for virginica is: f(x) = " + str(w0) + " + " + str(w1) + "*x1 + " + str(w2) + "*x2 + " + str(w3) + "*x3 + "+ str(w4) + "*x4 "
    print(model)
    print()

    computedOutputsSetosa = regressorSetosa.predict(testInputs)
    computedOutputsVersi = regressorVersi.predict(testInputs)
    computedOutputsVirginica = regressorVirginica.predict(testInputs)

    computedOutputsSetosa = [(x,'Iris-setosa') for x in computedOutputsSetosa]
    computedOutputsVersi = [(x,'Iris-versicolor') for x in computedOutputsVersi]
    computedOutputsVirginica = [(x,'Iris-virginica') for x in computedOutputsVirginica]

    finalComputedOutputs = [max(x,y,z)[1] for x,y,z in zip(computedOutputsSetosa,computedOutputsVersi,computedOutputsVirginica)]


    labels = ['Iris-setosa','Iris-versicolor','Iris-virginica']
    acc,precision,recall = evalClassificationMultiClass(testOutputs,finalComputedOutputs,labels)
    print("Classification manual : ----------")
    print("Accuracy : ",  acc)
    for prec in precision :
        print("Precision for", prec[1] , "is" , prec[0])
    for rec in recall :
        print("Recall for", rec[1] , "is", rec[0])
    error = 0.0
    for t1, t2 in zip(finalComputedOutputs, testOutputs):
        if (t1 != t2):
            error += 1
    error = error / len(testOutputs)
    print("classification error (manual): ", error)
    error = 1 - accuracy_score(testOutputs, finalComputedOutputs)
    print("classification error (tool): ", error)
    print()

    #tool :
    tool = LogisticRegression()
    tool.fit(trainInputs,trainOutputs)
    finalOutputs = tool.predict(testInputs)

    print("Classification with tool : ----------")
    acc, precision, recall = evalClassificationMultiClass(testOutputs, finalOutputs, labels)
    print("Accuracy with tool: ", acc)
    for prec in precision:
        print("Precision with tool for", prec[1], "is", prec[0])
    for rec in recall:
        print("Recall with tool for", rec[1], "is", rec[0])
    error = 1 - accuracy_score(testOutputs, finalOutputs)
    print("classification error (tool): ", error)


main()