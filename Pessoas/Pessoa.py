import json

from Abstract.Util import Util
from Abstract.Redis import r


class Pessoa():

    def __init__(self):
        self.setPessoa(json.loads(r.get('pessoa')) if r.exists('pessoa') else {})

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

        selecionar = input('Selecionar ' + str(nome) + '? (s/n): ')
        if selecionar == 's':
            self.selecionar(email)

        Util.message('success', 'Pessoa adicionada com sucesso.')

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
        if not buscar:
            Util.message('info', 'Pessoa não encontrada.')
            self.remover()
            return False

        if buscar['email'] == self.getEmail():
            Util.message(
                'info', 'A pessoa o qual quer remover está selecionada.')
            return False
        if buscar['situacao'] == 'desativado':
            Util.message('info', 'A pessoa já está desativada.')
            return False

        buscar['situacao'] = 'desativado'
        r.lset('pessoas', buscar['id'], json.dumps(buscar))
        Util.message('success', 'Pessoa removida com sucesso.')

    def selecionar(self, email=None):
        if not email:
            email = input('Informe (email/x para cancelar): ')

        if email == 'x':
            return False

        buscar = self.buscar('email', email)
        if not buscar:
            Util.message('info', 'Pessoa não encontrada.')
            self.selecionar()
            return False

        if buscar['situacao'] == 'desativado':
            Util.message('info', 'A pessoa selecionada está desativada.')
            return False

        r.set('pessoa', json.dumps({'id': buscar['id'], 'nome': buscar['nome'], 'email': buscar['email']}, indent=4, default=str))
        self.setPessoa(buscar)
        
    def setPessoa(self, pessoa):
        self.pessoa = pessoa
        
    def setId(self, id):
        self.pessoa['id'] = id

    def setNome(self, nome):
        self.pessoa['nome'] = nome

    def setEmail(self, email):
        self.pessoa['email'] = email

    def getPessoa(self):
        return self.pessoa

    def getId(self):
        return self.pessoa['id']

    def getNome(self):
        return self.pessoa['nome']

    def getEmail(self):
        return self.pessoa['email']
