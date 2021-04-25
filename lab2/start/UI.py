class UI(object):
    def __init__(self, service):
        self._service = service

    def start(self):
        while True:
            option = int(input('1. Prima problema\n2. A doua problema\n3. Salveaza in fisier\n4. Exit\n>> '))
            if option == 1:
                print(self._service.first_problem())
            if option == 2:
                print(self._service.second_problem())
            if option == 3:
                self._service.save_solution_on_file()
                print('Salvat in fisier')
            if option == 4:
                break
