from Repository.Repository import Repository
from Service.Service import Service
from UserInterface.UserInterface import UserInterface

def main():
    repo= Repository("D:\A-FACULTATE\Anu 2\Sem2\Inteligenta Artificiala\Laborator2\hard_01_tsp.txt")
    serv = Service(repo)
    ui = UserInterface(serv)
    ui.run()

main()