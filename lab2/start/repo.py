
class Repo(object):
    def __init__(self):
        self._length = 0
        self._graph = []
        self._source = -1
        self._destination = -1
        self.load_from_file()

    def load_from_file(self):
        # read the dates and save it in memory
        f = open("input.txt", "r")
        lines = f.readlines()

        self._length = int(lines[0])
        for i in range(1, self._length + 1):
            self._graph.append([int(j.rstrip()) for j in lines[i].split(',')])

        self._source = int(lines[self._length + 1])
        self._destination = int(lines[self._length + 2])

    def write_to_file(self, first_solution, second_solution):
        cost1, graph1 = first_solution
        cost2, graph2 = second_solution

        # convert the result to array of strings
        lines = [str(len(graph1)) + '\n',
                 ','.join([str(node + 1) for node in graph1]) + '\n',
                 str(cost1) + '\n',
                 str(len(graph2)) + '\n',
                 ','.join([str(node + 1) for node in graph2]) + '\n',
                 str(cost2) + '\n'
                 ]

        # writing to file
        file = open('output.txt', 'w')
        file.writelines(lines)
        file.close()
        return 0

    def get_graph(self):
        return self._graph

    def get_length(self):
        return self._length

    def get_source(self):
        return self._source

    def get_destination(self):
        return self._destination
