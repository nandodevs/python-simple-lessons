# conjunto = {1,2,3,4}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)

conjunto = {1,2,3,4,5}
conjunto2 = {5,6,7,8}
conjunto_uniao = conjunto.union(conjunto2) #União dos elementos dos conjuntos
print('União: {}'.format(conjunto_uniao))
conjunto_interseccao = conjunto.intersection(conjunto2) #intersecção dos elementos dos conjuntos
print('Intersecção: {}'.format(conjunto_interseccao))

conjunto_diferenca = conjunto.difference(conjunto2) #Elementos que tem no conj A e não tem no B
print('Diferença entre 1 e 2 {}'.format(conjunto_diferenca))

conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença Simétrica {}'.format(conjunto_diff_simetrica)) #Elementos em comum

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
conjunto_subset = conjunto_b.issubset(conjunto_a)
print(conjunto_subset) #Todos os elementos de A pertencentes a B

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(conjunto_superset)

lista = ['cachorro', 'gato', 'gato', 'elefante']
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)
