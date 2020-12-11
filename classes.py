class Calculadora:
    #Este método é onde inicia a chamada da classe
    # def __init__(self2):
    #     pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()
print(calculadora.soma(10, 2))
print(calculadora.subtracao(8,3))
print(calculadora.multiplicacao(3, 8))
print(calculadora.divisao(8,2))