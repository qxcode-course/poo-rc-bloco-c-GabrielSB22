class Ciente:
    def __init__(self, nome: str):
        self.__nome = nome

    def getNome(self):
        return self.__nome
    
    def __str__(self):
        return f'Nome: {self.__nome}'
    
    
