import os
import queue

AGENDAR = 1
ATENDER = 2
SALIR = 0

def mostrar_menu():
    os.system('cls')
    print(f'''                                                 Mi agenda
    {AGENDAR} Agendar evento
    {ATENDER} Atender evento
    {SALIR} Salir''')

def agendar_evento(ag):
    print('                                                 agendar evento')
    evento = input('Evento: ')
    ag.put(evento)

def atender_evento(ag):
    print('                                                  Atender evento')
    if ag.empty():
        print('No hay eventos por atender')
    else:
        evento = ag.get()
        print(f'Evento: {evento}')

def main():
    agenda = queue.PriorityQueue()
    continuar = True
    while continuar:
        mostrar_menu()
        opc = int(input('selecciona una opcion: '))
        if opc == AGENDAR:
            agendar_evento(agenda)
        elif opc == ATENDER:
            atender_evento(agenda)
        elif opc == SALIR:
            continuar = False
        else:
            print('Opcion no valida...')
        input('presiona enter para continuar....')
    print('Nos vemos....')

if __name__=='__main__':
    main()