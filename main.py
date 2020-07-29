from Util import Util
from setup import cliente as redis
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica
import re as regex

def PDV(error):
    #
    # Menu inicial de opções
    #
    if error:
        Util.danger('\nDesculpe, sua opção não foi encontrada, tente novamente...\n')
    else:
        Util.clear()
        Util.warning(
            '/***************************************************************************/\n' +
            '                               PONTO DE VENDA                                \n' +
            '                            ESCOLHA A OPÇÃO DESEJADA                         \n' +
            '                                                                             \n' +
            ' abrir - Abertura de caixa.                                                  \n' +
            ' fechar - Fechamento de caixa.                                               \n' +
            ' iniciar - Inicia uma venda.                                                 \n' +
            ' cancelar - Cancela a venda em andamento ou a venda informada.               \n' +
            ' finalizar - Finaliza a venda em andamento.                                  \n' +
            ' vendas - Lista as vendas por data.                                          \n' +
            ' pessoas - Lista os clientes cadastrados.                                    \n' +
            ' pessoa - Define o cliente da venda.                                         \n' +
            ' addpessoa - Adiciona uma pessoa aos registros.                              \n' +
            ' rmpessoa - Remove uma pessoa aos registros.                                 \n' +
            ' relatorios - Exibe as opções de relatórios                                  \n' +
            ' encerrar - Encerra o programa.                                              \n' +
            '/***************************************************************************/\n' +
            '                                                                             \n'
        )
    Util.warning(
        'Informe a opção desejada: '
    )
    opcao = input()

    #
    # Core das opções
    #
    while opcao != 'encerrar':
        if regex.search("^iniciar", opcao):
            print(0)
        elif regex.search("^cancelar", opcao):
            print(0)
        elif regex.search("^finalizar", opcao):
            print(0)
        elif regex.search("^vendas", opcao):
            print(0)
        elif regex.search("^pessoas", opcao):
            print(0)
        elif regex.search("^pessoa", opcao):
            print(0)
        elif regex.search("^addpessoa", opcao):
            print(0)
        elif regex.search("^rmpessoa", opcao):
            print(0)
        else:
            PDV('\nDesculpe, sua opção não foi encontrada, tente novamente...\n')
        return


if __name__ == "__main__":
    PDV(False)
