


class Repository:
    def __init__(self,fileName):
        self.__fileName = fileName
        self.__matrix = []
        self.__numberOfCities = 0
        self.__sourceIndex = 0
        self.__destinationIndex = 0
        self.__readData()

    def getMatrix(self):
        return self.__matrix

    def getNumberOfCities(self):
        return self.__numberOfCities

    def getSource(self):
        return self.__sourceIndex

    def getDestination(self):
        return self.__destinationIndex


    """
        first line : n = numberOfCities 
        from second to n+1 lines : n values per line , meaning the distances from the i city to all other cities 
        n+2 line : sourceIndex
        n+3 line : destinationIndex
    """
    def __readData(self):
        matrix = []
        #opening for reading
        file = open(self.__fileName,'r')
        content = file.read()
        file.close()
        #we have all the lines , from 0 to ...
        lines = content.split('\n')
        #first line index
        index = 0
        #number of cities on the first line
        n = int(lines[index])
        index = index + 1
        for i in range (0,n):
            aux = []
            #every line till n
            line = lines[index]
            #fields , aka the info of every line
            fields = line.split(",")
            for j in range(0,n):
                #for every line , we re adding the info
                aux.append(int(fields[j]))
            #at the end of every line , we add in the matrix
            matrix.append(aux)
            #next line
            index = index + 1

        self.__numberOfCities = n
        self.__sourceIndex = int(lines[index]) - 1
        index = index + 1
        self.__destinationIndex = int(lines[index]) - 1
        self.__matrix = matrix

    def writeToFile(self, first_solution, second_solution):
        costFirst, pathFirst = first_solution
        costSecond, pathSecond = second_solution

        # convert the result to array of strings
        lines = [str(len(pathFirst)) + '\n',
                 ','.join([str(node + 1) for node in pathFirst]) + '\n',
                 str(costFirst) + '\n',
                 str(len(pathSecond)) + '\n',
                 ','.join([str(node + 1) for node in pathSecond]) + '\n',
                 str(costSecond) + '\n'
                 ]

        # writing to file
        file = open('D:\A-FACULTATE\Anu 2\Sem2\Inteligenta Artificiala\Laborator2\out.txt', 'w')
        file.writelines(lines)






