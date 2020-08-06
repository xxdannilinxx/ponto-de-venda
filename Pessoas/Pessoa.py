import json
import datetime

from Abstract.Util import Util
from Abstract.Redis import r
# //https://www.dailysmarty.com/posts/redis-lists


class Pessoa():
    def lista(self):
        listaPessoas = []
        pessoas = r.lrange('pessoas', 0, -1)
        for pessoa in pessoas:
            listaPessoas.append(json.loads(pessoa))
        return listaPessoas

    def pessoas(self):
        pessoas = self.lista()
        if not pessoas:
            Util.message('info', 'Nenhuma pessoa cadastrada até o momento.')
        for pessoa in pessoas:
            Util.message('success' if pessoa['situacao'] == 'ativo' else 'danger', str(
                pessoa['id']) + ' - ' + str(pessoa['nome']) + ' <' + str(pessoa['email']) + '>')

    def adicionar(self):
        id = (r.llen('pessoas') + 1)
        nome = input('Informe o (nome/x para cancelar): ')
        email = input('Informe o (email/x para cancelar): ')

        if nome == 'x' or email == 'x':
            return False

        r.lpush('pessoas', json.dumps(
            {'id': id, 'nome': nome, 'email': email, 'situacao': 'ativo'}, indent=4, default=str))

    def buscar(self, email):
        #//https://gist.github.com/89465127/5776892
        d3 = {k : v for k,v in d.iteritems() if k in [2,3]}
        return d3
        # pessoas = self.lista()
        # def filtrar(email):
        #     # pessoa = json.loads(pessoa)
        #     for pessoa in pessoas:
        #         # pessoa = json.loads(pessoa)
        #         # print(pessoa.values())
        #         print(email)
        #         print(pessoa.values())
        #         if email in pessoa.values():
        #             print('tem')
        #             return True
        #         # if pessoa['email'] == email:
        #         #     return pessoa
        #     return False

        # return filter(filtrar, pessoas)

            # def filter_set(aquarium_creatures, search_string):
        # pessoas = self.lista()
        # teste = []
        # for pessoa in pessoas:
        #         pessoa = json.loads(pessoa)
        #         teste.append(pessoa)
        # print(teste)
        pessoas = self.lista()
        def filter_set(pessoas, search_string):
            def iterator_func(x):
                for v in pessoas:
                    # print(search_string)
                    # print(v)
                    if search_string in v.values():
                        print(search_string)
                        print(v.values())
                        return v.values()
                return False
            return filter(iterator_func, pessoas)

        return filter_set(pessoas, email)
    # return filter(filtrar, [email])

    def remover(self):
        email = input('Informe (email/x para cancelar): ')

        if email == 'x':
            return False
        r = self.buscar(email)
        print('####')
        print(r)
        print('####')
        for pessoa in r:
            print('-----')
            print(pessoa)
            print('-----')
            Util.message('success', 'Pessoa removida com sucesso.')
            return True
        Util.message('info', 'Pessoa não encontrada.')
        self.remover()

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
