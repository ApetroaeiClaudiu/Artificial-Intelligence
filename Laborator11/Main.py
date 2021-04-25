import numpy as np

from Kmeans.Kmeans import KMeansCluster
from Read import loadData, createWordsArray, createFinalArrays, returnAllWords, tfidf
from Regression.Regression import Regression, evalClassificationMultiClass


def getMeanValue(features):
    return sum(features) / len(features)
def getStdDevValue(features,meanValue):
    return (1 / len(features) * sum([(feat - meanValue) ** 2 for feat in features])) ** 0.5
def statisticalNormalisation(features,meanValue,stdDevValue):
    normalisedFeatures = [(feat - meanValue) / stdDevValue for feat in features]
    return normalisedFeatures

def Main():
    propozitii,out = loadData("D:\A-FACULTATE\Anu 2\Sem2\Inteligenta Artificiala\Laborator11\\reviews.csv")


    #bag of words

    # array de 726 string uri
    #allTheWords = createWordsArray(propozitii)
    # #matrice de 207 linii a cate 726 cuvinte
    #final = createFinalArrays(propozitii,allTheWords)
    final = tfidf(propozitii)


    #indexes = gucci
    indexes = [i for i in range(len(final))]
    #trainSample = final[:len(final)//2]
    #print(trainSample)
    #trainSample = np.random.choice(indexes, int(0.8 * len(final)), replace=False)
    #testSample = [i for i in indexes if i not in trainSample]
    #testSample = final[len(final)//2:]
    np.random.seed(5)
    #impartire train
    lungime = int((len(final) -1)*0.8)
    trainInputs = final[:lungime]
    trainOutputs = out[:lungime]
    #trainInputs = [final[i] for i in trainSample]
    #trainOutputs =[out[i] for i in trainSample]
    #impartire test
    testInputs = final[lungime:]
    testOutputs = out[lungime:]
    #testInputs = [final[i] for i in testSample]
    #testOutputs = [out[i] for i in testSample]


    # print("Regresie logistica ----------")
    # regressorPositive = Regression()
    # regressorPositive.fitBatch(trainInputs,trainOutputs,'positive')
    # w0Positive = regressorPositive.intercept_
    # weightsPositive = regressorPositive.coef_
    #
    # regressorNegative = Regression()
    # regressorNegative.fitBatch(trainInputs,trainOutputs,'negative')
    # w0Negative = regressorNegative.intercept_
    # weightsNegative = regressorNegative.coef_
    #
    # computedOutputsPositive =regressorPositive.predict(testInputs)
    # computedOutputsNegative = regressorNegative.predict(testInputs)
    #
    # computedOutputsPositive = [(x,'positive') for x in computedOutputsPositive]
    # computedOutputsNegative = [(x,'negative') for x in computedOutputsNegative]
    #
    # finalComputedOutputs = [max(x,y)[1] for x,y in zip(computedOutputsPositive,computedOutputsNegative)]
    #
    # labels = ['positive','negative']
    # acc, precision, recall = evalClassificationMultiClass(testOutputs, finalComputedOutputs, labels)
    # print("Classification manual : ----------")
    # print("Accuracy : ", acc)
    # for prec in precision:
    #     print("Precision for", prec[1], "is", prec[0])
    # for rec in recall:
    #     print("Recall for", rec[1], "is", rec[0])
    # error = 0.0
    # for t1, t2 in zip(finalComputedOutputs, testOutputs):
    #     if (t1 != t2):
    #         error += 1
    # error = error / len(testOutputs)
    # print("classification error (manual): ", error)
    # print()

    print("Clusterizare K-means ----------")

    kmeans = KMeansCluster(2,trainInputs,trainOutputs,6)
    first,second,clusters = kmeans.clustering()
    labels = ['positive', 'negative']
    prediction = kmeans.predict(testInputs)
    finalComputedOutputs = []
    xd =[]
    for ceva in prediction:
        if ceva == kmeans.clusters[0]:
            finalComputedOutputs.append(first)
            xd.append(second)
        else:
            finalComputedOutputs.append(second)
            xd.append(first)

    acc, precision, recall = evalClassificationMultiClass(testOutputs, finalComputedOutputs, labels)
    print("Classification manual : ----------")
    print("Accuracy : ", acc)
    for prec in precision:
        print("Precision for", prec[1], "is", prec[0])
    for rec in recall:
        print("Recall for", rec[1], "is", rec[0])
    error = 0.0
    for t1, t2 in zip(finalComputedOutputs, testOutputs):
        if (t1 != t2):
            error += 1
    error = error / len(out)
    print("classification error (manual): ", error)
    print()



    #
    # meanValueTrain = getMeanValue(train)
    # stDevTrain = getStdDevValue(train,meanValueTrain)
    # train = statisticalNormalisation(train,meanValueTrain,stDevTrain)
    #
    # test = statisticalNormalisation(test,meanValueTrain,stDevTrain)
    #
    # for i in range(len(train)):
    #     print(train[i])
    #
    # for i in range(len(test)):
    #     print(test[i])

    # for i in range(len(final)):
    #     print(final[i])
Main()