import email
import pathlib
import os

SALIR = 0
AGREGAR = 1
MOSTRAR = 2 
BUSCAR = 3

def mostra_menu():
    os.system('cls')
    print(f'''                                        Mi agenda
    {AGREGAR} Agragar contacto
    {MOSTRAR} Mostrar contactos
    {BUSCAR} buscar contacto
    {SALIR} Salir''')

def cargar_agenda(agenda,nombre_archivo):
    if pathlib.Path(nombre_archivo).exists():
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                contacto, telefono, email = linea.strip().split(',')
                agenda.setdefaul(contacto, (telefono, email))

    else:
        with open(nombre_archivo, 'w') as archivo:
            pass

def agregar_contacto(agenda, nombre_archivo):
    os.system('cls')
    print('                                         Agregar Contacto')
    nombre = input('Nombre: ')
    if agenda.get(nombre):
        print('El contacto ya existen.')
    else:
        telefono = input('Telefono: ')
        email = input('Email: ')
        agenda.setdefault(nombre,(telefono, email))
        with open(nombre_archivo, 'a') as archivo:
            archivo.write(f'{nombre},{telefono},{email}')
        print('contacto agregado con exito.')

def mostrar_contactos(agenda):
    os.system('cls')
    print('                                             Mis contactos')
    if len(agenda) > 0:
        for contactos, datos in agenda.items():
            print(f'Nombre: {contactos}')
            print(f'Telefono: {datos[0]}')
            print(f'Email: {datos[1]}')
            print('/'*50)
    else:
        print('No hay contactos registrados.')

def buscar_contactos(agenda):
    os.system('cls')
    print('                                       Buscar contactos')
    if len(agenda) > 0:
        nombre = input('Nombre: ')
        coincidencias = 0
        for contacto, datos in agenda.items():
            if nombre in contacto:
                print(f'Nombre: {contacto}')
                print(f'Telefono: {datos[0]}')
                print(f'Email : {datos [1]}')
                coincidencias += 1
                print('*'*50)
        if coincidencias == 0:
            print('No se encontro el contacto')
        else:
            print('No hay contactos registrados')
    else:
        print('No hay contactos registrados')

def main():
    continuar = True
    agenda = dict()
    nombre_archivo = 'agenda.txt'
    cargar_agenda(agenda, nombre_archivo)

    while continuar:
        mostra_menu()
        opc = int(input('Selecciona una opcion: '))

        if opc == AGREGAR:
            agregar_contacto(agenda, nombre_archivo)
        elif opc == MOSTRAR:
            mostrar_contactos(agenda)
        elif opc == BUSCAR:
            buscar_contactos
        elif opc == SALIR:
            continuar = False
        else:
            print('Opcion no valida')
        print('Preciona enter para continuar....')
    print('Nos vemos...')

if __name__=='__main__':
    main()