import re as regex

from Abstract.Util import Util
from Caixa.Caixa import Caixa
from Pessoas.Pessoa import Pessoa


def PDV(exibirMenu):
    #
    # Menu inicial de opções
    #
    if exibirMenu:
        Util.message('warning',
                     '/***************************************************************************/\n' +
                     '                               PONTO DE VENDA                                \n' +
                     '                            ESCOLHA A OPÇÃO DESEJADA                         \n' +
                     '/***************************************************************************/\n' +
                     '                                                                             \n' +
                     ' menu - Exibir menu de opções                                                \n' +
                     ' abrir - Abertura de caixa.                                                  \n' +
                     ' fechar - Fechamento de caixa.                                               \n' +
                     ' cancelar - Cancela a venda em andamento ou a venda informada.               \n' +
                     ' finalizar - Finaliza a venda em andamento.                                  \n' +
                     ' vendas - Lista as vendas por data.                                          \n' +
                     ' pessoas - Lista os clientes cadastrados.                                    \n' +
                     ' pessoa - Define o cliente da venda.                                         \n' +
                     ' addpessoa - Adiciona uma pessoa aos registros.                              \n' +
                     ' rmpessoa - Remove uma pessoa aos registros.                                 \n' +
                     ' relatorios - Exibe as opções de relatórios                                  \n' +
                     ' encerrar - Encerra o programa.                                              \n' +
                     '                                                                             \n'
                     )
    Util.message('warning',
                 '\nInforme a opção desejada: '
                 )
    opcao = input()

    #
    # Core das opções
    #
    while opcao != 'encerrar':
        if regex.search("^menu", opcao):
            PDV(True)
        elif regex.search("^abrir", opcao):
            Caixa().abrir()
        elif regex.search("^fechar", opcao):
            Caixa().fechar()
        elif regex.search("^cancelar", opcao):
            print(0)
        elif regex.search("^finalizar", opcao):
            print(0)
        elif regex.search("^vendas", opcao):
            print(0)
        elif regex.search("^pessoas", opcao):
            Pessoa().pessoas()
        elif regex.search("^pessoa", opcao):
            print(0)
        elif regex.search("^addpessoa", opcao):
            Pessoa().adicionar()
        elif regex.search("^rmpessoa", opcao):
            Pessoa().remover()
        else:
            Util.message('danger',
                         '\nDesculpe, sua opção não foi encontrada, tente novamente...\n')
            PDV(False)
        PDV(False)
    else:
        Util.message(
            'info', '\nAté logo... obrigado por usar nosso ponto de venda! =)')
        exit()


if __name__ == "__main__":
    PDV(True)
