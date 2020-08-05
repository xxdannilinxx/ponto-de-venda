import json
import datetime

from Abstract.Util import Util
from Abstract.Redis import r
# //https://www.dailysmarty.com/posts/redis-lists


class Pessoa():
    def lista(self):
        pessoas = r.lrange('pessoas', 0, -1)
        return pessoas

    def pessoas(self):
        pessoas = self.lista()
        if not pessoas:
            Util.message('info', 'Nenhuma pessoa cadastrada até o momento.')
        for pessoa in pessoas:
            pessoa = json.loads(pessoa)
            Util.message('success' if pessoa['situacao'] == 'ativo' else 'danger', str(
                pessoa['id']) + ' - ' + str(pessoa['nome']) + ' <' + str(pessoa['email']) + '>')

    def adicionar(self):
        id = (r.llen('pessoas') + 1)
        nome = input('Informe o nome: ')
        email = input('Informe o email: ')
        r.lpush('pessoas', json.dumps(
            {'id': id, 'nome': nome, 'email': email, 'situacao': 'ativo'}, indent=4, default=str))

    def buscar(self, email):
        pessoas = self.lista()
        def filtrar(email):
            for pessoa in pessoas:
                pessoa = json.loads(pessoa)
                if pessoa['email'] == email:
                    return True
            return False

        return filter(filtrar, [email])

    def remover(self):
        email = input('Informe o email: ')
        
        for pessoa in self.buscar(email): 
            print(pessoa)
            Util.message('success', 'Pessoa removida com sucesso.')
            return True
        Util.message('info', 'Pessoa não encontrada.')
        self.remover()
        # if buscar(email):
        #     print('achou')
        # else:
        #     print('n achou')



#####



# COLOCAR OPÇAO X PARA CANCELAR


###


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
