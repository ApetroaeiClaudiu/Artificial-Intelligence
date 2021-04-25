from math import sqrt



def Regression(realOutputs,computedOutputs,command):
    if command == "1":
        print("Loss for AME : "+ str(sum(abs(r - c) for r, c in zip(realOutputs, computedOutputs))))
        error = sum(abs(r - c) for r, c in zip(realOutputs, computedOutputs)) / len(realOutputs)
        print("Error single target for AME : ", error)
    if command == "2":
        print("Loss for RSME :" +str(sqrt(sum((r-c)**2 for r,c in zip(realOutputs,computedOutputs)))))
        error = sqrt(sum((r-c)**2 for r,c in zip(realOutputs,computedOutputs)) / len(realOutputs))
        print("Error single target for RSME : ",error)

def RegressionMultiTarget(realOutputs,computedOutputs,command):
    if command == "1":
        result = []
        for i in range(len(computedOutputs)):
            result.append(sum(abs(r-c) for r,c in zip(realOutputs[i],computedOutputs[i])))
        error=0
        for err in result:
            error += err
        print('Loss for AME: ' + str(error))
        error = error / len(realOutputs[0])
        print('Error in multi target for AME: ', error)
    if command == "2":
        result = []
        for i in range(len(computedOutputs)):
            result.append(sqrt(sum((r-c)**2 for r,c in zip(realOutputs[i],computedOutputs[i]))))
        error = 0
        for err in result:
            error += err
        print('Loss for RSME: ' + str(error))
        error = error / len(realOutputs[0])
        print('Error in multi target for RSME : ', error)
