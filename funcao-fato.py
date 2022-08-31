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

