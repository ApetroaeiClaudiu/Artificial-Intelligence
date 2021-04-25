from Repository.Repository import Repository
from Service.Service import Service
from UserInterface.UserInterface import UserInterface

repo = Repository("D:\A-FACULTATE\Anu 2\Sem2\Inteligenta Artificiala\lab04-gatsp-ApetroaeiClaudiu\in.txt")
service = Service(repo)
ui = UserInterface(service)
ui.run()
