from math import sqrt


class Repository:
    def __init__(self,fileName):
        self.__fileName = fileName
        #self.__data = self.readData()
        self.__data = self.load()

    def getData(self):
        return self.__data

    def readData(self):
        file = open(self.__fileName, "r")
        data = {}
        content = file.read()
        file.close()
        lines = content.split('\n')
        index = 0
        n = int(lines[index])
        data["nrNodes"] = n
        matrix = []
        pheromoneMatrix = []
        index = index + 1
        for i in range(n):
            matrix.append([])
            pheromoneMatrix.append([])
            line = lines[index]
            fields = line.split(",")
            for j in range(n):
                matrix[i].append(float(fields[j]))
                pheromoneMatrix[i].append(0)
            index = index + 1
        data["matrix"] = matrix
        data["pheromone"] = pheromoneMatrix
        params = open("D:\A-FACULTATE\Anu 2\Sem2\Inteligenta Artificiala\Laborator5\parameters.txt", "r")
        parameters = params.read()
        params.close()
        datas = parameters.split('\n')
        data["alfa"] = int(datas[0].split("=")[1])
        data["beta"] = int(datas[1].split("=")[1])
        data["evaporation"] = float(datas[2].split("=")[1])
        data["pseudo"] = float(datas[3].split("=")[1])
        data["dynamic"] = float(datas[4].split("=")[1])
        return data


    def writerez(self,rez, filename):
        f = open(filename, "w", encoding="utf-8-sig")
        f.write(str(len(rez.repres)))
        f.write("\n")
        for i in rez.repres:
            f.write(str(i) + ",")
        f.write("\n")
        f.write(str(rez.length))
        f.close()

    def __pr2(self,xa, ya, xb, yb):
        lungime = sqrt((xb - xa) * (xb - xa) + (yb - ya) * (yb - ya))
        return lungime

    def load(self):
        data = {}
        matrix = []
        file = open(self.__fileName, 'r')
        content = file.read()
        file.close()
        lines = content.split('\n')
        n = int(lines[0])
        data["nrNodes"] = n
        index = 1
        for i in range(0, n):
            line = lines[index]
            fields = line.split(" ")
            ceva = fields[0]
            a = float(fields[1])
            b = float(fields[2])
            matrix.append((a,b))
            index = index + 1
        final = []
        pheromoneMatrix = []
        for i in range(0,len(matrix)):
            rez = []
            pheromoneMatrix.append([])
            for j in range(0,len(matrix)):
                lungime = float(self.__pr2(matrix[i][0],matrix[i][1],matrix[j][0],matrix[j][1]))
                rez.append(lungime)
                pheromoneMatrix[i].append(0)
            final.append(rez)
        data["matrix"] = final
        data["pheromone"] = pheromoneMatrix
        params = open("D:\A-FACULTATE\Anu 2\Sem2\Inteligenta Artificiala\Laborator5\parameters.txt","r")
        parameters = params.read()
        params.close()
        datas = parameters.split('\n')
        data["alfa"] = int(datas[0].split("=")[1])
        data["beta"] = int(datas[1].split("=")[1])
        data["evaporation"] = float(datas[2].split("=")[1])
        data["pseudo"] = float(datas[3].split("=")[1])
        data["dynamic"] = float(datas[4].split("=")[1])
        return data