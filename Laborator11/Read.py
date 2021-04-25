import csv
import string
import re
from math import log

regex = "|,.;?\*'()|+"


def loadData(fileName):
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
    prop = dataNames.index('Text')
    out = dataNames.index('Sentiment')
    propozitii = [data[i][prop] for i in range(len(data))]
    output = [data[i][out] for i in range(len(data))]
    return  propozitii,output




def returnAllWords(propozitii):
    allWords = []
    for i in range(len(propozitii)):
        cuvinte = re.findall(r'\w+', propozitii[i])
        for word in cuvinte:
            allWords.append(word)
    return allWords

def createWordsArray(propozitii):
    allWords = []
    for i in range(len(propozitii)):
        cuvinte = re.findall(r'\w+',propozitii[i])
        for word in cuvinte :
            allWords.append(word)

    final = []
    for word in allWords:
        if word not in final:
            final.append(word)
    return final

def freq(cuvant,vector):
    contor = 0
    for i in range(len(vector)):
        if(vector[i] == cuvant):
            contor+=1
    return contor

def createFinalArrays(propozitii,allTheWords):
    #o matrice cu nr de propoztii linii ori nr de cuvinte coloane
    # pt fiecare propozitie , de cate ori apare fiecare cuvant in propozitia respectiva
    final = []
    for i in range(len(propozitii)):
        actuala = re.findall(r'\w+',propozitii[i])
        prop = []
        for word in allTheWords:
            prop.append(freq(word,actuala))
        final.append(prop)
    return final

def tf(cuvant,propozitie):
    count = 0
    for word in propozitie:
        if cuvant == word:
            count += 1
    return log(count +1)

def idf(cuvant,propozitii):
    count =0
    for propozitie in propozitii:
        actuala = re.findall(r'\w+', propozitie)
        if (cuvant in actuala):
            count += 1
    return log(len(propozitii) / (count))

def tfidf(propozitii):
    wordsIDF = {}
    final = []
    for propozitie in propozitii:
        actuala = re.findall(r'\w+', propozitie)
        for cuvant in actuala:
            if cuvant not in wordsIDF.keys():
                wordsIDF[cuvant] = idf(cuvant,propozitii)
    for propozitie in propozitii:
        actuala = re.findall(r'\w+', propozitie)
        prop = []
        for cuvant in wordsIDF.keys():
            prop.append(wordsIDF[cuvant] * tf(cuvant,actuala))
        final.append(prop)
    return final

# for propozitie in propozitii :
# for cuvant in toateCuvintele :
# --- numara de cate ori se gaseste cuvantul in propozitie
# ---pentru propozitie in propozitii :
# ---cate propozitii au cuvantul ?