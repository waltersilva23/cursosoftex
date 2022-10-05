class num_complexo:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

z1 = num_complexo(5,2)
z2 = num_complexo(6,3)
somareal = z1.real + z2.real
somaimag = z1.imag + z2.imag

print(f'{somareal} + {somaimag}i')