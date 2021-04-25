from start.heap import MyHeap


def find_the_path(graph, n, source, destination):
    # the version when he just return to the source city

    # input: graph([][]) - the matrix with cost between the cities, n(int) - number of cities, source(int), destination(int)
    # output: (cost(int), path([]))
    # solution is to keep in a heap the pairs (cost, path) and select the path with minimal cost in every step
    # complexity: O(n) - best case O(n!) - worst case
    heap = MyHeap()

    # populate the heap
    for i in range(n):
        if i != source:
            heap.push((graph[source][i], [source, i]))

    while True:
        cost, path = heap.pop()

        if destination == path[-1] or source == path[-1]:
            return cost, path

        # the case when all the cities was visited and we must return to the source
        if len(path) == n:
            copy = path.copy()
            copy.append(source)
            heap.push((cost + graph[path[-1]][source], copy))

        # push in the heap just the cities that were not visited
        for i in range(n):
            if i not in path:
                copy = path.copy()
                copy.append(i)
                heap.push((cost + graph[path[-1]][i], copy))


class Service(object):
    def __init__(self, repo):
        self._repo = repo

    def first_problem(self):
        # get dates from repo
        graph = self._repo.get_graph()
        n = self._repo.get_length()

        # find the path for both problems with same method
        return find_the_path(graph, n, 0, -1)

    def second_problem(self):
        # get dates from repo
        graph = self._repo.get_graph()
        n = self._repo.get_length()
        source = self._repo.get_source()
        destination = self._repo.get_destination()

        # find the path for both problems with same method
        return find_the_path(graph, n, source -1 , destination -1 )

    def save_solution_on_file(self):
        # get dates from repo
        graph = self._repo.get_graph()
        n = self._repo.get_length()
        source = self._repo.get_source()
        destination = self._repo.get_destination()

        # find the path for both problems with same method
        first_solution = find_the_path(graph, n, 0, -1)
        second_solution = find_the_path(graph, n, source - 1, destination - 1)

        # delete source city
        del first_solution[1][-1]

        # repo will write the results
        self._repo.write_to_file(first_solution, second_solution)

