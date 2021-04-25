def evalClassification(realLabels, computedLabels, pos, neg):
    acc = sum([1 if realLabels[i] == computedLabels[i] else 0 for i in range(0, len(realLabels))]) / len(realLabels)

    TP = sum([1 if (realLabels[i] == pos and computedLabels[i] == pos) else 0 for i in range(len(realLabels))])
    FP = sum([1 if (realLabels[i] == neg and computedLabels[i] == pos) else 0 for i in range(len(realLabels))])
    TN = sum([1 if (realLabels[i] == neg and computedLabels[i] == neg) else 0 for i in range(len(realLabels))])
    FN = sum([1 if (realLabels[i] == pos and computedLabels[i] == neg) else 0 for i in range(len(realLabels))])

    precisionPos = TP / (TP + FP)
    recallPos = TP / (TP + FN)
    precisionNeg = TN / (TN + FN)
    recallNeg = TN / (TN + FP)

    return acc, [precisionPos,precisionNeg], [recallPos,recallNeg]

def evalClassificationMultiClass(realLabels,computedLabels,labels):
    acc=0
    correct=0
    for i in range(len(realLabels)):
        if realLabels[i]==computedLabels[i]:
            correct+=1
    acc=correct/len(realLabels)
    precision = []
    recall = []
    x1 = []
    x2 = []
    for label in labels:
        TP=0
        FP=0
        TN=0
        FN=0
        for i in range(len(realLabels)):
            if realLabels[i] == label and computedLabels[i] == label:
                TP += 1
            if realLabels[i] != label and computedLabels[i] == label:
                FP += 1
            if realLabels[i] != label and computedLabels[i] != label:
                TN += 1
            if realLabels[i] == label and computedLabels[i] != label:
                FN += 1
        precision.append(TP/(TP + FP))
        recall.append(TP/(TP + FN))
        #x1.append(TN/(TN+FN))
        #x2.append(TN/(TN+FP))

    return acc,precision,recall

def evalClassificationProb(realLabels,computedLabels,labels):
     rez = []
     for p in computedLabels:
         probMaxPos = p.index(max(p))
         label = labels[probMaxPos]
         rez.append(label)
     print(rez)
     acc,prec,recall = evalClassificationMultiClass(realLabels,rez,labels)
     return acc,prec,recall


