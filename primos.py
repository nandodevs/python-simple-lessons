# a = input('Entre o número: ')
# b = input('Entre o número: ')
#
# print('{}.{}'.format(a, b))


# a = int(input('Digite um número: '))
# while a % 2 != 0:
#     a = int(input('Digite um número: '))


# a = int(input('Nota 1: '))
# while a > 10:
#     a = int(input('Digite a correta. Nota 1: '))

# b = int(input('Nota 2: '))
# while b > 10:
#     b = int(input('Digite a correta. Nota 2: '))
#
# c = int(input('Nota 3: '))
# while c > 10:
#     c = int(input('Digite a correta. Nota 3: '))
#
# media = a + b + c / 3
# print("A média do aluno é {}".format(media))


# nota = float(input('Entre com a nota: '))
# while nota > 10:
#     nota = int(input('Nota inválida. Digite a nota correta: '))
# print('Nota: {}'.format(nota))

# a = 0
# while a <= 10:
#     print(a)
#     a += 1

# a = int(input('Digite yum valor: '))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         # print(x, resto)
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(num)

a = int(input('Digite um número: '))

div = 0
for x in range(1, a + 1):
    resto = a % x
    print('Valor: ' + str(x), '/ Resto: ' + str(resto))
    if resto == 0:
        div += 1

if div == 2:
    print('Número {} é primo'.format(a))
else:
    print('Número {} não é primo'.format(a) )