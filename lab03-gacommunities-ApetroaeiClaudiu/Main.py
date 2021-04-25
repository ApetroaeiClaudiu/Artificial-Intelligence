from Repository.Repository import Repository
from Service.Service import Service
from UserInterface.UserInterface import UserInterface

repo = Repository("D:\A-FACULTATE\Anu 2\Sem2\Inteligenta Artificiala\lab03-gacommunities-ApetroaeiClaudiu\in.gml")
service = Service(repo)
ui = UserInterface(service)
ui.run()
