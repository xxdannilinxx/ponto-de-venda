import os

#
# Classe abstrata
#
class Util():
    #
    # Mensagens no shell
    #
    def message(type, mensagem):
        if type == 'success':
            print('\033[32m', mensagem, '\033[0;0m')
        elif type == 'danger':
            print('\033[31m', mensagem, '\033[0;0m')
        elif type == 'info':
            print('\033[34m', mensagem, '\033[0;0m')
        elif type == 'warning':
            print('\033[33m', mensagem, '\033[0;0m')
        else:
            print(mensagem)

    #
    # Limpar console do shell
    #
    def clear():
        return os.system('cls' if os.name == 'nt' else 'clear')
