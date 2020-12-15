from televisao import Televisao
from contador_letras import contador_letras, teste
import primos

if __name__ == '__main__':

    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    lista = ['cachorro', 'gato', 'elefante']
    print(contador_letras(lista))
    print(teste())
