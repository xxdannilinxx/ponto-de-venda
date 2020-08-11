import json

from Abstract.Util import Util
from Abstract.Redis import r


class Caixa():

    def __init__(self):
        self.setCaixa(json.loads(r.get('caixa')) if r.exists('caixa') else {})

    def abrir(self):
        if self.getCaixa():
            Util.message('danger', 'O caixa já foi aberto em ' + str(self.getData()) +
                         ' por ' + str(self.getAssinatura()) + ', encerre o caixa e tente novamente.')
        else:
            assinatura = input('Informe (assinatura/x para cancelar): ')
            if assinatura == 'x':
                return False

            if not assinatura:
                assinatura = input('Informe (assinatura/x para cancelar): ')
                if assinatura == 'x':
                    return False
                return

            r.set('caixa', json.dumps(
                {'total': 0, 'data': Util.dataAtual(), 'assinatura': assinatura}, indent=4, default=str))
            Util.message('info',
                         '-------------------------------\n' +
                         '       ABERTURA DE CAIXA       \n' +
                         '-------------------------------\n' +
                         'DATA\n' +
                         str(Util.dataAtual()) + '\n' +
                         '-------------------------------\n' +
                         'ASSINATURA\n' +
                         str(assinatura) + '\n' +
                         '-------------------------------\n')

    def fechar(self):
        if self.getCaixa():
            Util.message('danger', 'O caixa já foi aberto em ' + str(self.getData()) + ' por ' + str(self.getAssinatura()) + ', encerre o caixa e tente novamente.')
            r.delete('caixa')
            Util.message('info',
                         '-------------------------------\n' +
                         '       FECHAMENTO DE CAIXA     \n' +
                         '-------------------------------\n' +
                         'DATA\n' +
                         str(Util.dataAtual()) + '\n' +
                         '-------------------------------\n' +
                         'ASSINATURA\n' +
                         str(self.getAssinatura()) + '\n' +
                         '-------------------------------\n')
        else:
            Util.message(
                'danger', 'O caixa já encontra-se fechado no momento.')

    def setCaixa(self, caixa):
        self.caixa = caixa

    def setTotal(self, total):
        self.caixa['total'] = total

    def setData(self, data):
        self.caixa['data'] = data

    def setAssinatura(self, assinatura):
        self.caixa['assinatura'] = assinatura

    def getCaixa(self):
        return self.caixa

    def getTotal(self):
        return self.caixa['total']

    def getData(self):
        return self.caixa['data']

    def getAssinatura(self):
        return self.caixa['assinatura']
