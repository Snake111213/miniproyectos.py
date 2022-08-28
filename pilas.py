def validar_exprecion(expresion):
    pila = []
    for simbolo in expresion:
        if simbolo == '(':
            pila.append('(')
        elif simbolo == ')':
            if len(pila) > 0:
                pila.pop()
            else:
                return False
    return len(pila) == 0

def main():
    print('Escribe una exprecion aritmetica y te indicara con respecto a parantesis')
    e = input('Exprecion: ')
    valida = validar_exprecion(e)
    if valida:
        print('La exprecion esta balanceadad')
    else:
        print('La expresion no esta balanceada')

    print('Nos vemos...')

if __name__=='__main__':
    main()