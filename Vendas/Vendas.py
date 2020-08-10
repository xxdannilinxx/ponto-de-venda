import json
import datetime

from Abstract.Util import Util
from Abstract.Redis import r


class Vendas():

    def adicionarProduto(self, produto=123, quantidade=1):
        if produto == False or quantidade == False:
            Util.message('danger', 'Produto não encontrado.')
        r.rpush('produtos', json.dumps(
            {'codigo': produto, 'nome': 'Produto teste', 'quantidade': quantidade}, indent=4, default=str))
        #infos da venda