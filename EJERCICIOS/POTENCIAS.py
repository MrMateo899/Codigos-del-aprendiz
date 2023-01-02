base = int(input("Inserte una base: "))
expo = int(input("Inserte un exponente: "))
resul = base**expo

if expo == 2 :
    print(base, 'al cuadrado es igual a', resul)
elif expo == 3 :
    print(base, 'al cubo es igual a', resul)
elif expo > 3 : 
    print(base, 'elevado a', expo, 'es igual a', resul)