class pessoa():
    def __init__(self,nome,peso):
        self._nome = nome
        self.peso = peso

    def imprimir(self):
        print('meu nome é ',self._nome)
        print('meu peso é ',self.peso)
    
    def alimentar(self,comida):
        self.peso += comida

    def get_nome(self):
        return self._nome

    def set_nome(self,novo_nome):
        self._nome = novo_nome


n1 = pessoa(input('Qual o seu nome? '),float(input('Qual o seu peso ano passado? ')))
n1.get_nome()
n1.imprimir()
n1.alimentar(float(input('Aumentou quantos kg nesse ano? ')))
n1.get_nome()
n1.imprimir()
n1.set_nome(input('Qual o seu apelido? '))
n1.get_nome()
n1.imprimir()