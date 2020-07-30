class Pessoa():

    def __init__(self, id, nome, idade): 
        self.id = id 
        self.nome = nome 
        self.idade = idade 
        
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
