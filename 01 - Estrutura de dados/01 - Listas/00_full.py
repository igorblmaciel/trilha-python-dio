frutas = ["laranja", "maca", "uva"]
frutas = []

letras = list("python")

numeros = list(range(10))

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]

##############  01 Acessando elementos ############## 
frutas = ["maçã", "laranja", "uva", "pera"]

print(frutas[0])  # maçã
print(frutas[2])  # uva

############## 02 indices negativos ############## 
frutas = ["maçã", "laranja", "uva", "pera"]

print(frutas[-1])  # pera
print(frutas[-3])  # laranja

############## 03 Matriz ############## 
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])  # [1, "a", 2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

############## 04 Fatiamento ############## 

lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]

############## 05 iterar listas ############## 
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


############## 06  compreensao de listas ############## 
# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
#comprehension [valor(retorno) iteravel(for) filtro(if)] 

print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)

#pratica
precos = [-12.20 , 12.99, -49.99, 497.00, -5.99, -221.00]
custos = [valor for valor in precos if valor <0]
print(custos)
print(precos)

############## 07  Appends ############## 
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)  # [1, "Python", [40, 30, 20]]
lista[2].append(10)

lista[1]+=(" Curso")
print(lista)  # [1, "Python", [40, 30, 20]]

############## 08 clear ############## 
lista.clear()

############## 09 copy ############## 
#Retorna uma copia da lista com instancia diferente 

lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print("***** 09 Copy *********")
print(lista)  # [1, "Python", [40, 30, 20]]
print(id(l2),id(lista))
l2[0] = 2
print(l2)
print(lista)

############## 10 count ############## 
cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1
print(lista.count(1))

############## 11 Extends ############## 
#Junta uma lista em outros sem eliminar valores duplicados
print("############## 11 Extends ##############" )
linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "c"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]

############## 12 Index ############## 
# Encontra a primeira ocorrencia
linguagens = ["python", "java", "c", "java", "csharp"]

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0

############## 13 Pop ############## 
# Remove o último elemento da lista / Pilha  
print("############## 13 Pop ############## ")
linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens)
print(linguagens.pop())  # csharp
print(linguagens)
print(linguagens.pop())  # java
print(linguagens)
print(linguagens.pop())  # c
print(linguagens.pop(0))  # python

############## 14 Remove ##############
# Remove um elemento especifico
print("############## 14 Remove ############## ")

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens)  # ["python", "js", "java", "csharp"]


############## 15 Reverse ##############
# Coloca a lista em ordem contrária
print("############## 15 Reverse ############## ")

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.reverse()

print(linguagens)  # ["csharp", "java", "c", "js", "python"]

############## 16 Sort ##############
# Coloca a lista em ordem 
print("############## 16 Sort ############## ")

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)

############## 17 Len ##############
# Tamanho da lista em ordem 
print("############## 17 Len ############## ")
linguagens = ["python", "js", "c", "java", "csharp"]

print(len(linguagens))  # 5


############## 18 sorted ##############
# Função sorted()
linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]
