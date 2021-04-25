from Heap.Heap import Heap

"""
    input: the matrix of costs , the number of cities/dimension of matrix 
            the index of source and destination cities
    output: pair formed with (cost,path) / (int,array)
    complexity: best case - O(n)
                worst case - O(n!)
"""
def findPath(matrix, n, source, destination):
    # solution is to keep in a heap the pairs (cost, path) and select the path with minimal cost in every step
    heap = Heap()
    #initialize the heap with basic data from the matrix
    #for the second problem , source will be 0 so we will initialize everything
    for i in range(n):
        if i != source:
            #heap will have (the weight from source to node i , the path created by the [source,i] )
            heap.push( (matrix[source][i], [source, i]) )
    while True:
        #selecting the minimal cost from the heap
        cost, path = heap.pop()
        #if the destination node is the last element of the path array or the source is the last
        #aka we reached the end or we reached the beginning
        #we return the pair
        if destination == path[-1] or source == path[-1]:
            return cost, path
        #all the cities have been visited
        #we need to return to the source
        if len(path) == n:
            #a copy array where we add the source
            copy = path.copy()
            copy.append(source)
            #add to heap the new array and its cost (cost + the weight from the last element of the path to the source)
            heap.push((cost + matrix[path[-1]][source], copy))
        # push in the heap just the cities that were not visited
        for i in range(n):
            if i not in path:
                copy = path.copy()
                copy.append(i)
                #add to heap the new copy array and its cost
                heap.push((cost + matrix[path[-1]][i], copy))


class Service(object):

    def __init__(self,Repository):
        self.Repository = Repository
        self.matrix = self.Repository.getMatrix()
        self.n = self.Repository.getNumberOfCities()
        self.source = self.Repository.getSource()
        self.destination = self.Repository.getDestination()


    def firstEx(self):
        cost, path = findPath(self.matrix,self.n,0,-1)
        copy = path.copy()
        for i in range(len(copy)):
            copy[i] = copy[i] + 1
        return cost,copy

    def secondEx(self):
        cost, path = findPath(self.matrix,self.n,self.source,self.destination)
        copy = path.copy()
        for i in range(len(copy)):
            copy[i] = copy[i] + 1
        return cost, copy

    def save(self):
        # find the path for both problems with same method
        first = findPath(self.matrix,self.n,0,-1)
        second = findPath(self.matrix,self.n,self.source,self.destination)
        # delete source city
        del first[1][-1]
        #writing the results to file
        self.Repository.writeToFile(first,second)