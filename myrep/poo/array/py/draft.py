import numpy as np #necessario pra gerar elementos aleatorios

fruta = ["maça", "banana", "uva"]
numeros = []
chacha = ["gato", "fofa", "cinza"]
abc = ["a", "b", "c"]

primeiro = chacha[1] #torna o elemento de uma lista em uma variavel de acordo com seu indice
randola = np.random.randint(1, 10, 9) #cria elementos aleatorios em uma lista

for i in range (0, 11): #cria elementos em um array vazio (apenas numeros) 
    numeros.append(i)

fruta.append("pera") #adiciona no ultimo
fruta.remove("banana") #remove 
fruta.insert(0, "caju") #coloca em uma posição 
valor = fruta.pop(1) #ele retorna o "removido", podendo pegar ele dps
aiai = "".join(fruta) #separa os elementos da lista com algo ou junto tudo
del fruta[1] #remove um elemento de uma lista em determinada posição

print(aiai)
print(valor)
print (fruta)
print(numeros)
print(randola)
print(primeiro)

#-------------------------------------------------------------------------------#
for i in chacha:
    print(i) #print cada elemento da lista

for i, letra in enumerate(abc):
    print(f"indice: {i}, letra: {letra}") #percorre a lista com o indice dos elementos

#-----------------------------------------------------------------------------#
achado = [10, 20, 30, 40, 50]
elemento_procurado = 40
encontrado = False

for e in achado:
    if e == elemento_procurado:
        print(f'elemento {elemento_procurado} encontrado') #busca um valor em cada indice usando um laço
        encontrado = True
        break
    else:
        print("elemento não encontrado")
#-------------------------------------------------------------------------------#
cinema = ["pipopca", "cadeira", "telão", "luzes"]

if "cadeira" in cinema:
    print("tem isso no cinema")

if "arma" not in cinema:
    print("não tem isso no cinema")
#-------------------------------------------------------------------------------#