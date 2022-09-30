x = 0
y = 0
z = 0
b = 0
nulo = 0
opcao = 2
eleicao = False
while eleicao == False:
    condicao = False
    while eleicao == False:
        try:
            print('\nEscolha um dos três candidatos abaixo:'
                  '\ncandidato_X => 889'
                  '\ncandidato_Y => 847'
                  '\ncandidato_Z => 515'
                  '\nbranco => 0')
            voto = int(input('\nNúmero do Candidato: '))
            if voto == 889:
                print('\nVocê votou no candidato_X')
                x = x + 1
                eleicao = True
            elif voto == 847:
                print('\nVocê votou no candidato_Y')
                y = y + 1
                eleicao = True
            elif voto == 515:
                print('\nVocê votou no candidato_Z')
                z = z + 1
                eleicao = True
            elif voto == 0:
                print('\nVocê votou branco')
                b = b + 1
                eleicao = True
            else:
                print('\nVoto nulo')
                nulo = nulo + 1
                eleicao = True
        except:
            print('\nVote novamente!(Use só números)')
    while condicao == False:
        try:
            print('\nDeseja finalizar a eleição?'
                  '\n1 - sim'
                  '\n2 - não')
            opcao = int(input('\nOpção: '))
            if opcao == 1:
                eleicao = True
                condicao = True
            elif opcao == 2:
                eleicao = False
                condicao = True
            else:
                print('\nEscolha apenas as opções 1 e 2.')
        except:
            print('\nEscolha apenas as opções 1 e 2.')
if x > y and x > z:
    candidato = 'Candidato_X'
elif y > x and y > z:
    candidato = 'Candidato_Y'
elif z > x and z > y:
    candidato = 'Candidato_Z'
else:
    candidato = 'Empate'
print('\nResultado da eleição:'
      f'\ncandidato_X: {x} votos.'
      f'\ncandidato_Y: {y} votos.'
      f'\ncandidato_Z: {z} votos'
      f'\nBrancos: {b} votos'
      f'\nNulos: {nulo} votos')
print(f'\nTotal de votos: {x+y+z+b+nulo}')
if candidato == 'Empate':
    print('Aconteceu um empate...')
else:
    print(f'\nO vencedor foi o {candidato}.')