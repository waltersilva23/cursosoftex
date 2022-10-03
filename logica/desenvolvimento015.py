import random

def bubble_sort(valores):
    print('')
    elementos = len(valores) - 1
    ordem = False
    troca = 0
    while ordem == False:
        for i in range(elementos):
            if valores[i] > valores[i+1]:
                troca = valores[i]
                valores[i] = valores[i+1]
                valores[i+1] = troca 
                print(valores)
    return valores

valores = []
for i in range(0,10,1):
    valores.append(random.randint(0,100))
print('')
print(valores)
bubble_sort(valores)
