import csv


def loadData(fileName, inputVariabName1, inputVariabName2,inputVariabName3,inputVariabName4, outputVariabName):
    data = []
    dataNames = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                dataNames = row
            else:
                data.append(row)
            line_count += 1
    selectedVariable1 = dataNames.index(inputVariabName1)
    selectedVariable2 = dataNames.index(inputVariabName2)
    selectedVariable3 = dataNames.index(inputVariabName3)
    selectedVariable4 = dataNames.index(inputVariabName4)
    inputMat1 = [float(data[i][selectedVariable1]) for i in range(len(data))]
    inputMat2 = [float(data[i][selectedVariable2]) for i in range(len(data))]
    inputMat3 = [float(data[i][selectedVariable3]) for i in range(len(data))]
    inputMat4 = [float(data[i][selectedVariable4]) for i in range(len(data))]

    selectedOutput = dataNames.index(outputVariabName)
    outputs = [data[i][selectedOutput] for i in range(len(data))]

    return inputMat1,inputMat2,inputMat3,inputMat4,outputs