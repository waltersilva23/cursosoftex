class num_complexo:
    def __init__(self, real, imag):
        self.r = real
        self.i = imag

    def printar(self):
        if self.i < 0:
            print(f'{self.r}{self.i}i')
            print(f'Parte real: {self.r} e parte imaginária: {self.i}')
        else:
            print(f'{self.r}+{self.i}i')
            print(f'Parte real: {self.r} e parte imaginária: {self.i}')

    def soma(self, comp2, comp3):
        num = num_complexo(self.r+comp2.r+comp3.r, self.i+comp2.i+comp3.i)
        print('\nResultado da soma')
        num.printar()

    def sub(self, comp2, comp3):
        num = num_complexo(self.r-comp2.r-comp3.r, self.i-comp2.i-comp3.i)
        print('\nResultado da subtração')
        num.printar()

    def mult1(self, comp2, comp3):
        num1 = num_complexo(self.r*comp2.r-self.i*comp2.i, self.r*comp2.i+self.i*comp2.r)
        print('\nResultado da multiplicação')
        num2 = num_complexo(num1.r*comp3.r-num1.i*comp3.i, num1.r*comp3.i+num1.i*comp3.r)
        num2.printar()

    def div(self, comp2, comp3):
        sr, si, c2r, c2i, c3r, c3i = self.r, self.i, comp2.r, comp2.i, comp3.r, comp3.i
        r = c2r**2 + c2i**2
        num1 = num_complexo((sr*c2r+si*c2i)/r, (si*c2r-sr*c2i)/r)
        print('\nResultado da divisão')
        w = c3r**2 + c3i**2
        num2 = num_complexo((num1.r*c3r+num1.i*c3i)/w, (num1.i*c3r-num1.r*c3i)/w)
        num2.printar()


z1 = num_complexo(5, -2)
z2 = num_complexo(6, -3)
z3 = num_complexo(2, -4)

z1.soma(z2, z3)
z1.sub(z2, z3)
z1.mult1(z2, z3)
z1.div(z2, z3)

