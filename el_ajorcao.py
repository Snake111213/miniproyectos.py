import random

import os

MAX_FALLOS = 5
paises = ['Antigua y Barbuda', 'Argentina','Bahamas','Barbados',
'Belice','Bolivia','Brasil','Canada','Chile','Colombia',
'Costa Rica','Cuba','Dominica','Ecuador','El salvador',
'Estados Unidos','Granada','Guatemala','Guyana','Haiti',
'Honduras','Jamaica','Mexico','Nicaragua','Panama','paraguay',
'Peru','Republica Dominicana','San cristobal y Nieves',
'San Vicente y las Granadinas','Santa Lucia','Surinam',
'Trinidad y Tobago','Uruguay','Venezuela']

def crear_cadenas():
    pais = random.choice(paises)
    secreto = '_' *len(pais)
    return pais, secreto

def reemplazar_simbolo(original, secreto, simbolo):
    cantidad = original.count(simbolo)
    inicio = 0
    for i in range(cantidad):
        pos = original.find(simbolo, inicio)
        secreto = secreto[:pos] + simbolo + secreto[pos+1:]
        inicio = pos + 1
    return secreto

def ahorcado():
    print(f'Hola, vamos a jugar el juego del ahorcado. La \
        palabra secreta sera el nombre de uno de los {len(paises)} \
        paises del continente americano. Tienes oportunidad de fallar\
        hasta {MAX_FALLOS} veces. !Comenzemos!' )
    input('Presiona enter para comenzar...')
    original, secreto = crear_cadenas()
    fallos = 0
    while secreto != original and fallos < MAX_FALLOS:
        os.system('cls')
        print(f'Palabra:{secreto}')
        s = input('cual simbolo quieres destapar? ')
        if s in original:
            secreto = reemplazar_simbolo(original, secreto, s)
            print('!Bien hecho! El simbolo es parte de la palabra')
        else:
            print('Lo siento, el simbolo es parte de la palabra')
            fallos += 1
        input('Presiona enter para continuar...')
    os.system('cls')
    if secreto == original:
    
        print(f'Felicidades, el pais el {secreto}')
    else:
        print(f'Lo siento, el pais era {original}')
    print('Nos vemos...')

def main():
    ahorcado()

if __name__=='__main__':
    main()