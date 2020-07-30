from Pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, cpf, nome, idade):
        super().__init__(nome, idade)
        self.cpf = cpf
        
    def setCpf(self, cpf): 
        self.cpf = cpf 

    def getCpf(self): 
        return self.cpf