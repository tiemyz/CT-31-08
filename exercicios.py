n = 5
fatorial = 1

for i in range(1,n+1): 
    fatorial = fatorial * i 
print ("O fatorial de 5 é : ", fatorial)

numeros = [4,3,2,4,5,7,2,4,6]
def fatorial(lista_numero):
    lista_fatorial = []
    for num in lista_numero:
        fat = 1
        for i in range(2,num+1):
            fat*=i
        lista_fatorial.append(fat)
    return lista_fatorial
print(fatorial(numeros))

def par_ou_impar(lista_numeros):
    resultado = []
    for num in numeros:
        if num%2==0:
            resultado.append("é par")
        else:
            resultado.append("é ímpar")
    return resultado

numeros = [4,3,2,4,5,7,2,4,6]
resposta = par_ou_impar([])
print(resposta)

def acha_media(lista_numeros):
    soma = 0
    for num in lista_numeros:
        soma+=num
    media = soma/len(numeros)
    return media

def desvio_padrao(lista_numeros):
    subtracao = []
    media = acha_media(lista_numeros)
    for num in lista_numeros:
        sub = (num - media)**2
        subtracao.append(sub)
    soma = 0
    for elem in subtracao:
        soma+=elem
    soma /=len(lista_numeros)
    soma = soma**0.5
    return soma
print(desvio_padrao(numeros))
print(numeros) 

#8 - Escreva uma função para encontrar elementos  em comum em uma lista de listas. Por exemplo, nessa lista contendo 3 listas cada uma tem os elementos 12 e 18. 
#Original: [[12,18,23,25,45], [7,12,18,24,28], [1,5,8,12,15,16,18]] 
#Elementos em comum: [18,12]

lista = [[12,18,23,25,45], [7,12,18,24,28], [1,5,8,12,15,16,18]]
print(len(lista))
print(lista[0])
print(12 in lista[1] and 12 in lista[2])

def acha_comum(lista):
    lista_comum = []
    for elem in lista[0]:
        for i in range(1,len(lista)-1):
            if elem not in lista[i]:
                break
            if i == len(lista)-2:
                lista_comum.append(elem)
    return lista_comum
print(acha_comum(lista))

def subtrai(lista):
    

