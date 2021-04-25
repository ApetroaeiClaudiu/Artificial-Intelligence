from Repository.Repository import Repository
from Service.Service import Service
from UserInterface import *
from math import *

from UserInterface.UserInterface import UserInterface

repo = Repository("D:\A-FACULTATE\Anu 2\Sem2\Inteligenta Artificiala\Laborator5\hard.txt")
service = Service(repo)
ui = UserInterface(service)
ui.run()

