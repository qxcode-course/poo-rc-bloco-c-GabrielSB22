class Muleke:
    def __init__(self, name: str, age: str):
        self.name = name
        self.age = age
    
    def getname(self):
        return self.name
    
    def getage(self):
        return self.age
    
    def setname(self, name: str):
        self.name = name

    def setage(self, age: str):
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}:{self.age}" 

class Trampolim:
    def __init__(self):
        self.brincando: list[Muleke] = []
        self.perando: list[Muleke] = []

    def __str__(self) -> str:
        wait =", ".join(str(x)for x in self.perando)
        brinca =", ".join(str(x)for x in self.brincando)
        
        return f"[{wait}] => [{brinca}]"

    def arrive(self, kid: Muleke):
        self.perando.insert(0, kid)

    def enter(self):
        if self.perando:
            kid = self.perando.pop()
            self.brincando.insert(0, kid)
        else:
            print("Não tem ninguem")

    def leave(self):
        if len(self.brincando) > 0:
            kid = self.brincando.pop()
            self.perando.insert(0, kid)

    def removerdalista(self, name: str, list_m: list[Muleke]) -> Muleke | None:
        for i, m in enumerate(list_m):
            if m.getname() == name:
                return list_m.pop(i)
        return None
        
    def removermuleke(self, name: str) -> Muleke | None:
        kid = self.removerdalista(name, self.perando)
        if kid is not None:
            return kid
        return self.removerdalista(name, self.brincando)



def main():
    jump = Trampolim()

    while True:
        line = input()
        print("$"+line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(jump)
        elif args[0] == "arrive":
            c  = args[1]
            r = int(args[2])
            jump.arrive(Muleke(c, r))
        elif args[0] == "enter":
            jump.enter()
        elif args[0] == "leave":
            jump.leave()
        elif args[0] == "remove":
            p = args[1]
            k = jump.removermuleke(p)
            if k is None:
                print(f"fail: {p} nao esta no pula-pula")
main()       

        