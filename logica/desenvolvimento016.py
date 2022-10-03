import random

def insertionSort(vetor):
    
    for passo in range(1, len(vetor)):
        chave = vetor[passo]
        j = passo - 1

        while j >= 0 and chave < vetor[j]:
            vetor[j + 1] = vetor[j]
            j = j - 1
        
        vetor[j + 1] = chave

lista = []
for i in range(0,30,1):
    lista.append(random.randint(1,1000))
    if lista[i] %2 == 1:
        lista[i] = lista[i]
    else:
        lista[i] = lista[i] + 1
print(lista)
insertionSort(lista)
print('\nVetor em ordem crescente:')
print(lista)