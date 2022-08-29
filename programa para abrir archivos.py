'''import pathlib
ruta = pathlib.Path('.')
for archivo in ruta.iterdir():
    print(archivo)'''

'''import pathlib

ruta = pathlib.Path('.')

for archivo in ruta.glob('*.pdf'):
    print(archivo)'''

'''import pathlib
ruta = pathlib.Path('.')

print('Programa que busca un archivo dentro de la carpeta de trabajo')
archivo = input('Nombre del archivo buscado: ')
archivo = ruta / archivo

if archivo.exists():
    print(f'El archivo existe y mide {archivo.stat().st_size} bytes.')
else:
    print('No existe el archivo.')'''

'''import pathlib

def main():
    ruta = pathlib.Path('/')

    extenciones = {archivo.suffix for archivo in ruta.iterdir()}
    print(f'exenciones: {extenciones}')

if __name__=='__maim__':
    main()'''
'''
import pathlib
from unittest.mock import patch
'''

'''def main():
    ruta = pathlib.Path('.')

    diccionario = {k : [v.name for v in ruta.glob(f'*{k}')]
                    for k in {archivo.suffix for archivo in ruta.iterdir()}}
    
    for extension, archivos in diccionario.items():
        print(f'extencion: {extension}')
        print(f'archivos: {archivos}')

if __name__=='__main__':
    main()'''

import pathlib

def main():
    ruta = pathlib.Path('.')
    diccionario = {k : [v for v in ruta.glob(f'{k}')]
                    for k in {archivo.suffix for archivo in ruta.iterdir()}}
    for extencion, archivo in diccionario.items():
        carpeta = ruta / extencion[1:]
        carpeta.mkdir()
        for archivo in archivo:
        
            archivo.replace(carpeta / archivo.name)

if __name__=='__main__':
    main()