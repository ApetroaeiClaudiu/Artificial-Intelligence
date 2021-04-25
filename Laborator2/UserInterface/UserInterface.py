
class UserInterface(object):
    def __init__(self,Service):
        self.__Service = Service

    def run(self):
        while True:
            option = int(input("1 - First exercise \n"
                               "2 - Second Exercise\n"
                               "3 - Save to File\n"
                               "4 - Exit\n"))
            if option == 1:
                print(self.__Service.firstEx())
            if option == 2:
                print(self.__Service.secondEx())
            if option == 3:
                self.__Service.save()
            if option == 4:
                break
