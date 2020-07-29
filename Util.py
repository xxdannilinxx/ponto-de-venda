import os

class Util():
    def success(mensagem):
        print('\033[32m', mensagem, '\033[0;0m')

    def danger(mensagem):
        print('\033[31m', mensagem, '\033[0;0m')

    def info(mensagem):
        print('\033[34m', mensagem, '\033[0;0m')
    
    def warning(mensagem):
        print('\033[33m', mensagem, '\033[0;0m')

    def clear():
        return os.system('cls' if os.name=='nt' else 'clear')
