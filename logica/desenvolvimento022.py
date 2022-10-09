class Conta:

    total_contas = 0

    def __init__(self,saldo):
        self.saldo = saldo
        Conta.total_contas += 1

    def deposita(self,valor):
        self.saldo += valor


c1 = Conta(float(input('Digite o valor do saldo inicial: ')))
print(f'Conta de nº {c1.total_contas}')
c1.deposita(float(input('Quanto deseja depositar? ')))
print(c1.saldo)

c2 = Conta(float(input('Digite o valor do saldo inicial: ')))
print(f'Conta de nº {c2.total_contas}')
c2.deposita(float(input('Quanto deseja depositar? ')))
print(c2.saldo)

c3 = Conta(float(input('Digite o valor do saldo inicial: ')))
print(f'Conta de nº {c3.total_contas}')
c3.deposita(float(input('Quanto deseja depositar? ')))
print(c3.saldo)