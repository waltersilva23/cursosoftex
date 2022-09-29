from string import ascii_letters
validos = ascii_letters + ' áéíóú'
condicao = False
while condicao == False:
    try:
        nome = input('\nInforme o seu nome completo: ')
        if all(c in validos for c in nome):
            condicao = True
        else:
            print('\nPor favor digite um nome válido (somente letras e espaços)')
    except:
        print('\nVocê informou um dado inválido.')
while condicao == True:
    try:
        ano = int(input('\nInforme o ano em que nasceu: '))
        if 1922 <= ano <= 2021:
            idade = 2022 - ano
            print(f'\n{nome}, você completou, ou completará {idade} anos.')
            condicao = False
        else:
            print('\nVocê informou um dado inválido.')
    except:
        print('\nVocê informou um dado inválido.')