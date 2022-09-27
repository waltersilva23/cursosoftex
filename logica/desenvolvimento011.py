def calc(x,y,opcao):

    if opcao == 1:
        print(f'\nResultado: {x+y}')
    elif opcao == 2:
        print(f'\nResultado: {x-y}')
    elif opcao == 3:
        print(f'\nResultado: {x*y}')
    elif opcao == 4:
        print(f'\nResultado: {x/y}')


opcao = 1

#Programa
while opcao:
    print('\nEscolha a operação que deseja realizar:')
    print('1: Soma')
    print('2: Subtração')
    print('3: Multiplicação')
    print('4: Divisão')
    print('0: Sair')
    opcao = int(input('\nOpção: '))
    if opcao == 0:
        print('\nAté logo!')
        exit()
    elif 1 <= opcao <= 4:
        x = float(input('Digite o primeiro valor: '))
        y = float(input('Digite o segundo valor: '))

        calc(x, y, opcao)
    else:
        print('\nEssa opção não existe')
