from math import sqrt


class Repository:
    def __init__(self,fileName):
        self.__fileName = fileName
        self.__data,self.__nodes = self.__load()
        #self.__data = []
        #self.__nodes = 0
        #self.__loadFromFile()

    def getNodes(self):
        return self.__nodes

    def getData(self):
        return self.__data

    def __loadFromFile(self):
        matrix = []
        file = open(self.__fileName, 'r')
        content = file.read()
        file.close()
        lines = content.split('\n')
        index = 0
        # number of cities on the first line
        n = int(lines[index])
        index = index + 1
        for i in range(0, n):
            aux = []
            # every line till n
            line = lines[index]
            # fields , aka the info of every line
            fields = line.split(",")
            for j in range(0, n):
                # for every line , we re adding the info
                aux.append(int(fields[j]))
            # at the end of every line , we add in the matrix
            matrix.append(aux)
            # next line
            index = index + 1
        self.__nodes = n
        self.__data = matrix
        print(self.__data)
        print(self.__nodes)

    def __pr2(self,xa, ya, xb, yb):
        lungime = sqrt((xb - xa) * (xb - xa) + (yb - ya) * (yb - ya))
        return lungime

    def __load(self):
        matrix = []
        file = open("D:\A-FACULTATE\Anu 2\Sem2\Inteligenta Artificiala\Laborator4\date.txt", 'r')
        content = file.read()
        file.close()
        lines = content.split('\n')
        n = int(lines[0])
        index = 1
        for i in range(0, 52):
            line = lines[index]
            fields = line.split(" ")
            ceva = fields[0]
            a = float(fields[1])
            b = float(fields[2])
            matrix.append((a,b))
            index = index + 1
        final = []
        for i in range(0,len(matrix)):
            rez = []
            for j in range(0,len(matrix)):
                lungime = float(self.__pr2(matrix[i][0],matrix[i][1],matrix[j][0],matrix[j][1]))
                rez.append(lungime)
            final.append(rez)
        print(final)
        return final,n

