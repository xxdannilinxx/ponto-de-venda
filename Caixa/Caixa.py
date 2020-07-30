from Abstract.Util import Util

class Caixa():

    def __init__(self):
        self.id = 1
        self.total = 0
        self.data = ''

    # data
    # total
    # id
    # assinatura
    # operacao
    def abrir(self, id):
        if self.getId() > 0:
            Util.message('danger', 'O caixa [{id}] já foi aberto anteriormente, encerre o caixa e tente novamente.'.format(id=self.getId()))
        else:
            Util.message('success', 'Caixa aberto com sucesso!')

    def setId(self, id):
        self.id = id

    def setTotal(self, total):
        self.total = total

    def setData(self, data):
        self.data = data

    def setAssinatura(self, assinatura):
        self.assinatura = assinatura

    def setOperacao(self, operacao):
        self.operacao = operacao

    def getId(self):
        return self.id

    def getTotal(self):
        return self.total

    def getData(self):
        return self.data

    def getAssinatura(self):
        return self.assinatura

    def getOperacao(self):
        return self.operacao
