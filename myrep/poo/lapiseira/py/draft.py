class Grafite:
    def __init__(self, calibre: float, dureza: str, tamanho: int):
        self.calibre = calibre
        self.dureza = dureza 
        self.tamanho = tamanho

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
main()