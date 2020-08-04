import json
import datetime

from Abstract.Util import Util
from Abstract.Redis import r
#//https://www.dailysmarty.com/posts/redis-lists

class Pessoa():

    # def __init__(self, id, nome, idade):
    #     self.id = id
    #     self.nome = nome
    #     self.idade = idade

    def lista(self):
        pessoas = r.lrange('pessoas', 0, -1)
        # pessoas = r.keys('pessoas:*')
        if not pessoas:
            Util.message('info', 'Nenhuma pessoa cadastrada até o momento.')
        for pessoa in pessoas:
            x = json.loads(pessoa) 
            Util.message('success' if x['situacao'] == 'ativo' else 'danger', str(x['id']) + ' - ' + str(x['nome']) + ' <' + x['email'] + '>')

    def adicionar(self):
        id = (r.llen('pessoas') + 1)
        r.lpush('pessoas', json.dumps({'id': id, 'nome': 'José', 'email': 'jose@gmail.com', 'situacao': 'ativo'}, indent=4, default=str))

    def setId(self, id):
        self.id = id

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade
