import json
import datetime

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
            data = datetime.datetime.now().strftime('%d/%m/%Y')
            Util.message('info',
                         '-------------------------------\n' +
                         '       ABERTURA DE CAIXA       \n' +
                         '-------------------------------\n' +
                         'DATA\n' +
                         str(data) + '\n' +
                         '-------------------------------\n' +
                         'ASSINATURA\n' +
                         str(assinatura) + '\n' +
                         '-------------------------------\n')
            r.set('caixa', json.dumps({'total': 0, 'data': data, 'assinatura': assinatura}, indent=4, default=str))

    def fechar(self):
        if self.getCaixa():
            data = datetime.datetime.now().strftime('%d/%m/%Y')
            Util.message('danger', 'O caixa já foi aberto em {data} por {assinatura}, encerre o caixa e tente novamente.'.format(
                data=self.getData(), assinatura=self.getAssinatura()))
            Util.message('info',
                         '-------------------------------\n' +
                         '       FECHAMENTO DE CAIXA     \n' +
                         '-------------------------------\n' +
                         'DATA\n' +
                         str(data) + '\n' +
                         '-------------------------------\n' +
                         'ASSINATURA\n' +
                         str(self.getAssinatura()) + '\n' +
                         '-------------------------------\n')
            r.delete('caixa')
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
