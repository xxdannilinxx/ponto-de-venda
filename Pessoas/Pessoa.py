import json

from Abstract.Util import Util
from Abstract.Redis import r

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
        id = r.llen('pessoas')
        nome = input('Informe o (nome/x para cancelar): ')
        email = input('Informe o (email/x para cancelar): ')

        if nome == 'x' or email == 'x':
            return False
        
        buscar = self.buscar('email', email)
        if buscar:
            Util.message('danger', 'Email já cadastrado.')
            self.adicionar()
            return True

        r.rpush('pessoas', json.dumps(
            {'id': id, 'nome': nome, 'email': email, 'situacao': 'ativo'}, indent=4, default=str))
        Util.message('success', 'Pessoa adicionada com sucesso.')
        selecionar = input('Selecionar ' + str(nome) + '? (s/n): ')
        if selecionar == 's':
            self.selecionar(email)

    def buscar(self, campo, email):
        pessoas = self.lista()
        for pessoa in pessoas:
            if pessoa[campo] == email:
                return pessoa
        return False

    def remover(self, email=None):
        if not email:
            email = input('Informe (email/x para cancelar): ')

        if email == 'x':
            return False

        buscar = self.buscar('email', email)
        if buscar:
            if buscar['situacao'] == 'desativado':
                Util.message('info', 'A pessoa já está desativada.')
                return False
            buscar['situacao'] = 'desativado'
            r.lset('pessoas', buscar['id'], json.dumps(buscar))
            Util.message('success', 'Pessoa removida com sucesso.')
            return True
        Util.message('info', 'Pessoa não encontrada.')
        self.remover()

    def selecionar(self):
        email = input('Informe (email/x para cancelar): ')

        if email == 'x':
            return False

        buscar = self.buscar('email', email)
        if buscar:
            if buscar['situacao'] == 'desativado':
                Util.message('info', 'A pessoa selecionada está desativada.')
                return False
            self.setId(buscar['id'])
            self.setNome(buscar['nome'])
            self.setEmail(buscar['email'])
            Util.message('success', 'Pessoa selecionada com sucesso.')
            return True
        Util.message('info', 'Pessoa não encontrada.')
        self.remover()

    def setId(self, id):
        self.id = id

    def setNome(self, nome):
        self.nome = nome

    def setEmail(self, email):
        self.email = email

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def getEmail(self):
        return self.email
