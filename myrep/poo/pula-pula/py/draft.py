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
        if len(self.perando) == 0:
            return
        if len(self.brincando) > 0:
            s = self.brincando.pop(0)
            self.perando.append(s)
            
            e = self.perando.pop(0)
            self.brincando.append(e)



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
main()       

        