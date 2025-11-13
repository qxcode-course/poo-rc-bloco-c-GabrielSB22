class Grafite:
    def __init__(self, calibre: float, dureza: str, tamanho: int):
        self.calibre = calibre
        self.dureza = dureza 
        self.tamanho = tamanho

    def escrevernafolha(self) -> int:
        if self.dureza == "HB":
            return 1
        if self.dureza == "2B":
            return 2
        if self.dureza == "4B":
            return 4
        if self.dureza == "6B":
            return 6
        else:
            return 0

    def __str__(self):
        return f"[{self.calibre}:{self.dureza}:{self.tamanho}]"
    


class Lapiseira:
    def __init__(self, calibre: float):
        self.calibre = calibre
        self.bico: Grafite | None = None
        self.tambor: list[Grafite] = []

    def __str__(self):
        bico = str(self.bico) if self.bico else "[]"
        tambor = "".join(str(g)for g in self.tambor)
        tambor = f"<{tambor}>"
        return f"calibre: {self.calibre}, bico: {bico}, tambor: {tambor}"
    
    def pull(self):
        if self.bico is not None:
            print("fail: ja existe grafite no bico")
            return
        if len(self.tambor) == 0:
            print("fail: tambor está vazio")
            return 
        
        self.bico = self.tambor.pop(0)

    def remove(self):
        self.bico = None

    def escrever(self):
        if self.bico is None:
            print("fail: nao existe grafite no bico")
            return
        custo = self.bico.escrevernafolha()

        if self.bico.tamanho <= 10:
            self.bico = None
            print("fail: tamanho insuficiente")
            return
        
        newsize = self.bico.tamanho - custo
        if newsize < 10:
            print("fail: folha incompleta")
            self.bico.tamanho = 10
            return
        
        self.bico.tamanho = newsize

    def inserir(self, graf: Grafite) -> bool :
        if self.calibre != graf.calibre:
            return False
     
        self.tambor.append(graf)
        return True


def main():
    lap = None

    while True:
        line = input()
        print("$"+line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(lap)
        elif args[0] == "init":
            z = float(args[1])
            lap = Lapiseira(z)
        elif args[0] == "insert":
            calibre = float(args[1])
            dureza = args[2]
            tamanho = int(args[3])

            gra = Grafite(calibre, dureza, tamanho)

            if lap is None:
                print("fail lapiseira não foi iniciada")
            elif not lap.inserir(gra):
                print("fail: calibre incompatível")

        elif args[0] == "pull":
            if lap is None:
                print("fail: lapiseira não iniciada")
            else:
                lap.pull()

        elif args[0] == "remove":
            lap.remove()

        elif args[0] == "write":
             lap.escrever()
main()