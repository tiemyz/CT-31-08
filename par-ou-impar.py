################## EXERCÍCIOS ##################

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