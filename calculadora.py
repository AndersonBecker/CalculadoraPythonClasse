class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    def somar(self):
        return self.numero1 + self.numero2
    def subtrair(self):
        return self.numero1 - self.numero2
    def multiplicar(self):
        return self.numero1 * self.numero2
    def dividir(self):
        return self.numero1 / self.numero2
    
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

calcula = Calculadora(numero1, numero2)

print(f'Valor da soma é {calcula.somar()}')
print(f'Valor da subtração é: {calcula.subtrair()}')
print(f'Valor da multiplicação é :{calcula.multiplicar()}')
print(f'Valor da divisão é :{calcula.dividir()}')

