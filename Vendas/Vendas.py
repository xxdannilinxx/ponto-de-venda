import json

from Abstract.Util import Util
from Abstract.Redis import r
from Caixa.Caixa import Caixa
from Pessoas.Pessoa import Pessoa


class Vendas():
    def lista(self):
        listaVendas = []
        produtos = r.lrange('vendas', 0, -1)
        for venda in vendas:
            listaVendas.append(json.loads(venda))
        return listaVendas

    def listaProdutos(self):
        listaProdutos = []
        produtos = r.lrange('produtos', 0, -1)
        for produto in produtos:
            listaProdutos.append(json.loads(produto))
        return listaProdutos

    def informacoesVenda(self):
        total = 0
        Util.message('info',
                     '-------------------------------------\n' +
                     '          VENDA EM ANDAMENTO         \n' +
                     '-------------------------------------\n' +
                     'ABERTURA DO CAIXA                    \n' +
                     str(Caixa().getData()) + '\n' +
                     '-------------------------------------\n' +
                     'ASSINATURA\n' +
                     str(Caixa().getAssinatura()) + '\n' +
                     '-------------------------------------\n' +
                     'CLIENTE\n' +
                     str(Pessoa().getNome()) + '\n' +
                     '-------------------------------------\n' +
                     '  QTD CODIGO      PRODUTO       PREÇO  ')
        for produto in self.listaProdutos():
            preco = (float(produto['preco']) * float(produto['quantidade']))
            total += preco
            Util.message('info',
                         ' ' + str(produto['quantidade']) + ' x ' + str(produto['codigo']) + ' - ' + str(produto['nome']) + '   R$ ' + str(Util.moeda(preco)))
        Util.message('info',
                     '-------------------------------------\n' +
                     'TOTAL DA VENDA:             R$ ' + Util.moeda(total) + '\n' +
                     '-------------------------------------\n'
                     )

    def adicionarProduto(self, produto, quantidade):
        if produto == False or quantidade == False:
            Util.message('danger', 'Produto não encontrado.')
            return False

        if not Caixa().getCaixa():
            Util.message('danger', 'O caixa ainda não está aberto.')
            return False

        r.rpush('produtos', json.dumps(
            {'codigo': produto, 'nome': 'Produto teste', 'quantidade': quantidade, 'preco': 10.00}, indent=4, default=str))
        self.informacoesVenda()
    
    def cancelar(self):
        if not r.exists('produtos'):
            Util.message('info', 'Não existe venda em andamento.')
            return False

        r.delete('produtos')
        Pessoa().selecionar('clientepadrao@site.com')
        Util.message('success', 'Venda cancelada com sucesso.')
    
    def finalizar(self):
        if not r.exists('pessoa'):
            Util.message('info', 'Nenhuma pessoa selecionada.')
            return False

        if not r.exists('produtos'):
            Util.message('info', 'Não existe venda em andamento.')
            return False

        r.rpush('vendas', json.dumps(
            {'pessoa': Pessoa().getPessoa(), 'produtos': self.listaProdutos(), 'assinatura': Caixa().getAssinatura(), 'data': Util.dataAtual()}, indent=4, default=str))
        r.delete('produtos')
        Pessoa().selecionar('clientepadrao@site.com')
        Util.message('success', 'Venda finalizada com sucesso.')
