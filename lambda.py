# Lambda é uma função anônima
contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

print(soma(5, 10))
print(subtracao(10, 5))

#Dicionário em Python
calculadora = {
    'soma' : lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}

soma = calculadora['soma']
multiplicacao = calculadora['multiplicacao']
subtracao = calculadora['subtracao']
divisao = calculadora['divisao']
print('A soma é : {}'.format(soma(10, 5)))
print('A multiplicação é: {}'.format(multiplicacao(9, 3)))