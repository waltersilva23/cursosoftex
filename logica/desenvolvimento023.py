class pessoa():
    def __init__(self,nome,peso):
        self._nome = nome
        self._peso = peso

    def imprimir(self):
        print('meu nome é ',self._nome)
        print('meu peso é ',self._peso)
    
    def set_peso(self,novo_peso):
        self._peso += novo_peso

    def get_nome(self):
        return self._nome

    def get_peso(self):
        return self._peso

    def set_nome(self,novo_nome):
        self._nome = novo_nome


n1 = pessoa(input('Qual o seu nome? '),float(input('Qual o seu peso ano passado? ')))
n1.get_nome()
n1.get_peso()
n1.imprimir()
n1.set_peso(float(input('Aumentou quantos kg nesse ano? ')))
n1.get_nome()
n1.get_peso()
n1.imprimir()
n1.set_nome(input('Qual o seu nome completo? '))
n1.get_nome()
n1.get_peso()
n1.imprimir()

n2 = pessoa(input('\nQual o seu nome? '),float(input('Qual o seu peso ano passado? ')))
n2.get_nome()
n2.get_peso()
n2.imprimir()
n2.set_peso(float(input('Aumentou quantos kg nesse ano? ')))
n2.get_nome()
n2.get_peso()
n2.imprimir()
n2.set_nome(input('Qual o seu nome completo? '))
n2.get_nome()
n2.get_peso()
n2.imprimir()