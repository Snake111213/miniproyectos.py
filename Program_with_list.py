import os
from pickle import FALSE

AGREGAR = 1
INSERTAR = 2
MOSTRAR = 3
BUSCAR = 4
ELIMINAR = 5
ORDENAR = 6
LIMPIAR = 7
SALIR = 0

frutas = []

def imprimir_menu():
    os.system('cls')
    print(f'''
    {AGREGAR}) agregar
    {INSERTAR}) insertar
    {MOSTRAR}) mostrar
    {BUSCAR}) buscar
    {ELIMINAR}) eliminar
    {ORDENAR}) ordenar
    {LIMPIAR}) limpiar lista
    {SALIR}) salir''')

def agregar_registro():
    print('                           Agregar')
    nombre = input('Nombre: ')
    frutas.append(nombre)
    print('Registro agregado con exito. ')

def insertar_registro():
    print('                           Insertar')
    nombre = input('Nombre: ')
    pos = int(input('posicion: '))
    frutas.insert(pos, nombre)
    print('Registro insertedo en la posicion indicada')

def mostrar_registros():
    print('                                Mostrar')
    if len(frutas) > 0:
        for fruta in frutas:
            print(fruta)
        else:
            print('No se han agregado frutas a la lista.')

def buscar_registro():
    print('                                   Buscar')
    if len(frutas) > 0:
        nombre = input('Nombre a buscar: ')
        if nombre in frutas:
            cantidad = frutas.count(nombre)
            inicio = 0
            for i in range(cantidad):
                pos = frutas.index(nombre, inicio)
                print(f' {nombre} se encuentrea en la posicion {pos+1}')
                inicio = pos + 1

            else:
                print(f'{nombre} no se encuentra en la lista')
        else:
            print("no se han agregado frutas a la lista")
def eliminar_registro():
    print('                                Registros')
    if len(frutas) > 0:
        for i in range(len(frutas)):
            print(f'{i+1}. {frutas[i]}')
        print('0. Cancelar')
        pos = int(input(f'Posicion a eliminar (1 -{len(frutas)})'))
        if 0 < pos <= len(frutas):
            frutas.pop(pos-1)
            print('registro eliminado con exito')
        else:
            print('No se eliminara ningun registro.')
    else:
        print('no se han agregado frutas a la lista')

def ordenar_registros():
    print('                                     Ordenar')
    if len(frutas) > 0:
        frutas.sort()
        print('Registros ordenados alfabeticamente.')
    else:
        print('No se han agregado frutas a la lista')

def limpiar_registros():
    print('                                   Limpiar')
    frutas.clear()
    print('Los registros han sido borrados')

def main():
    continuar = True
    while continuar:
        imprimir_menu()
        opc = int(input('selecciona una opcion'))
        os.system('cls')
        if opc == AGREGAR:
            agregar_registro()
        elif opc == INSERTAR:
            insertar_registro()
        elif MOSTRAR:
            mostrar_registros()
        elif opc == BUSCAR:
            buscar_registro()
        elif opc == ELIMINAR:
            eliminar_registro()
        elif opc == LIMPIAR:
            limpiar_registros()
        elif opc == ORDENAR:
            ordenar_registros()
        elif opc == LIMPIAR:
            limpiar_registros()
        elif opc == SALIR:
            print(' Nos vemos...')
            continuar = False
        else:
            print('Opcion no valida')
        input('Presione enter para continuar...')

if __name__ =='__main__':
    main()