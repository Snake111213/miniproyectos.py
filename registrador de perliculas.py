import os
import csv

def registrar_peliculas(nombre_archivo):
    cantidad = int(input('cuantas peliculas deseas registrar?'))
    with open(nombre_archivo, 'a', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv, delimiter=',')
        for i in range(cantidad):
            os.system('cls')
            titulo = input('Titulo: ')
            duracion = input('Duracion: ')
            anio = input('Anio: ')
            writer.writerow([titulo, duracion, anio])
        
def recuperar_peliculas(nombre_archivo):
    os.system('cls')
    print('Peliculas registradas: ')
    with open(nombre_archivo, 'r', newline='') as archivo_csv:
        reader = csv.reader(archivo_csv)
        for linea in reader:
            print(f'Titulo: {linea[0]}')
            print(f'Duracion: {linea[1]}')
            print(f'Anio: {linea[2]}')
            print('-'*50)

def main():
    archivo = 'peliculas.csv'
    registrar_peliculas(archivo)
    recuperar_peliculas(archivo)

if __name__=='__main__':
    main()