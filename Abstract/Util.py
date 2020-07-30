
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
            print('\n\033[32m', mensagem, '\033[0;0m\n')
        elif type == 'danger':
            print('\n\033[31m', mensagem, '\033[0;0m\n')
        elif type == 'info':
            print('\n\033[34m', mensagem, '\033[0;0m\n')
        elif type == 'warning':
            print('\n\033[33m', mensagem, '\033[0;0m\n')
        else:
            print(mensagem)

    #
    # Limpar console do shell
    #
    def clear():
        return os.system('cls' if os.name == 'nt' else 'clear')
