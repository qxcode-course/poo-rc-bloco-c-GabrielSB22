class Pessoa:
    def __int__(self, nome: str = ""):
        self.__nome = nome

    def getNome(self):
        return self.__nome
    
    def __str__(self):
        return f"{self.__nome}"
    
class Market:
    def __init__(self, caixas: int):
        self.espera: list[Pessoa] = []
        self.caixas: list[Pessoa | None ] = [None for _ in range(caixas)]

    def __str__(self):
        cx = ", " .join([str(x) if x else "-----" for x in self.caixas])
        wait = " , " .join([str(x) for x in self.espera])
        return f"Caixas: [{cx}]\nEspera: [{wait}]"
    
    def arrive(self, person: Pessoa):
        self.espera.append(person)

    def call(self, index: int):
        if self.espera == []:
            print("fail: sem clientes")
        

def main():
    mercado = Market(0)
    pers = Pessoa
    
    while True:
        line = input()
        print("$"+line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(mercado)
        elif args[0] == "init":
            q = int(args[1])
            mercado = Market(q)
        elif args[0] == "arrive":
            pb = Pessoa (args[1])
            mercado.arrive(pb)
main()