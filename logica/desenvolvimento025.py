nome = str(input('\nDigite seu nome completo: ')).strip()
print('\nAnalisando seu nome...')
sem_espaço = len(nome) - nome.count(' ')
print(f'\nSeu nome tem ao todo {sem_espaço} letras')
primeiro = nome.split()
print(f'\nSeu primeiro nome tem {len(primeiro[0])} letras')
letra = str(input('\nQual letra você deseja saber quantas vezes aparece em seu nome? '))
print(f'\nA letra {letra.upper()} foi escolhida e aparece {nome.count(letra)} vezes')
