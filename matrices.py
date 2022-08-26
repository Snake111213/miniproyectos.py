from random import random
import random

N = 3

print(f'programa que calcula la suma de matrices de tamano {N}x{N}')

m1 = [[random.randint(1, 50) for J in range(N)] for i in range(N)]
m2 = [[random.randint(1, 50) for j in range(N)] for i in range(N)]
resultado = [[0]*N for i in range(N)]

for renglon in range(N):
    for columna in range(N):
        resultado[renglon][columna] = m1[renglon][columna]+m2[renglon][columna]

for i in range(N):
    if i == N//2:
        print(f'{m1[i]} + {m2[i]} = {resultado[i]}')
    else:
        print(f'{m1[i]} + {m2[i]} = {resultado[i]}')