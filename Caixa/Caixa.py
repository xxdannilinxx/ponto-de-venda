from Abstract.Util import Util
from Abstract.Redis import r
import json
import datetime


class Caixa():

    def __init__(self):
        self.setCaixa(json.loads(r.get('caixa')) if r.exists('caixa') else {})

    def abrir(self):
        if self.getCaixa():
            Util.message('danger', 'O caixa já foi aberto em {data} por {assinatura}, encerre o caixa e tente novamente.'.format(
                data=self.getData(), assinatura=self.getAssinatura()))
        else:
            assinatura = input('Assinatura: ')
            r.set('caixa', json.dumps({'total': 0, 'data': datetime.datetime.now(
            ), 'assinatura': assinatura}, indent=4, default=str))
            Util.message('success', 'Caixa aberto com sucesso!')

    def fechar(self):
        if self.getCaixa():
            r.delete('caixa')
            Util.message('success', 'Caixa fechado sucesso!')
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
