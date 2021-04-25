

from Classification import evalClassification, evalClassificationMultiClass, evalClassificationProb
from Regression import RegressionMultiTarget, Regression


def Main():
    while True:
        print("0 = Exit")
        print("1 = Regression Single Target")
        print("2 = Regression Multi Target")
        print("3 = Classification Single Class")
        print("4 = Classification Multi Class")
        command = input("Select: ")
        if command == "0":
            break
        if command == "1":
            comm = input("1-AME / 2-RSME")
            realOutputs = [3, 9.5, 4, 5.1, 6, 7.2, 2, 1]
            computedOutputs = [2, 7, 4.5, 6, 3, 8, 3, 1.2]
            Regression(realOutputs,computedOutputs,comm)
        if command == "2":
            comm = input("1-AME / 2-RSME")
            realOutputs = [[3, 9.5, 4, 5.1, 6, 7.2, 2, 1],
                           [2, 7.5, 3, 5, 7.2, 3, 1.5, 8]]
            computedOutputs = [[2, 7, 4.5, 6, 3, 8, 3, 1.2],
                               [1.5, 7, 3, 4.5, 5, 2, 1.5, 7]]
            RegressionMultiTarget(realOutputs, computedOutputs, comm)
        if command == "3":
            realLabels = ['spam', 'spam', 'ham', 'ham', 'spam', 'ham']
            computedLabels = ['spam', 'ham', 'ham', 'spam', 'spam', 'ham']
            acc, prec, recall = evalClassification(realLabels, computedLabels, 'spam', 'ham')
            print('acc: ', acc, ' precision: ', prec, ' recall: ', recall)
        if command == "4":
            realLabels = ['cat', 'cat', 'mouse', 'dog', 'bird', 'dog', 'dog', 'bird']
            computedLabels = ['cat', 'dog', 'dog', 'cat', 'dog', 'mouse', 'dog', 'bird']
            acc, prec, recall = evalClassificationMultiClass(realLabels, computedLabels,['dog', 'cat', 'bird', 'mouse'])
            print('acc: ', acc, ' precision: ', prec, ' recall: ', recall)
        if command == "5":
            labels = ['dog', 'cat', 'bird', 'mouse']
            realLabels = ['cat', 'cat', 'mouse', 'dog', 'bird', 'dog', 'dog', 'bird']
            computedLabels = [[0.1, 0.2, 0.5,0.2], [0.2, 0.3, 0.3,0.2], [0.1, 0.7, 0.1,0.1], [0.4, 0.1, 0.2,0.3], [0.3, 0.3, 0.1,0.3],
                               [0.2, 0.2, 0.5,0.1], [0.3, 0.3, 0.2,0.2], [0.1, 0.2,0.2, 0.5]]
            acc, prec, recall = evalClassificationProb(realLabels, computedLabels,labels)
            print('acc: ', acc, ' precision: ', prec, ' recall: ', recall)


Main()