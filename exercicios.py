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


