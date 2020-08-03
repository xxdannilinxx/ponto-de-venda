from Abstract.Util import Util
from Abstract.Redis import r
import json
import datetime

class Pessoa():

    # def __init__(self, id, nome, idade): 
    #     self.id = id 
    #     self.nome = nome 
    #     self.idade = idade 

    def lista(self):
        pessoas = r.lrange('pessoas', 0, -1)
        if not pessoas:
            Util.message('info', 'Nenhuma pessoa cadastrada até o momento.')
        for pessoa in pessoas:
            print(pessoa)
    
    def adicionar(self):
        r.lpush('pessoas', *json.dumps({'nome': 'Danilo', 'email': 'xx@gmail.com'}, indent=4, default=str))

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
