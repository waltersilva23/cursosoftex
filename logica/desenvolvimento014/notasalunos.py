import pandas as pd

df = pd.read_csv("notas_alunos.csv")
df = df.set_index('aluno')
media = (df["nota_1"] + df["nota_2"])/2
df['media'] = media

df.loc[df['media'] >= 7,"situação"] = 'Aprovado'
df.loc[df['media'] < 7,"situação"] = 'Reprovado'
df.loc[df['faltas'] > 5,"situação"] = 'reprovado'

maior_faltas = df['faltas'].max()
media_geral = df['media'].sum()
maior_media = df['media'].max()

print(f'O maior número de faltas de um aluno: {maior_faltas}')
print(f'A média geral das notas: {media_geral/4}')
print(f'A maior média entre os alunos: {maior_media}')

df.to_csv('alunos_situacao.csv')
