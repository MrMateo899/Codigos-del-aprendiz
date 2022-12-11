## OPERADORES ##

print(3+4) # Suma
print(3-4) # Diferencia
print(3*4) # Producto
print(3/4) # Division
print(10%2) # Calcular residuo
print(10//3) # "Flordivision" (deja un entero siempre)
print(3**4) # Potencias

## Operaciones entre letras y números ##

print("Hola " + "Python, " + '¿Qué tal?')

'''
print("Hola" + 5) 
esto es un error
Forma correcta
    |
    v
'''
print('hola'+str(5)) #Tambien podemos cambiar su tipo a "string" simplemente poniendo el entero en comillas

print('Chau ' * 5)

my_float = 2.5*2
print('hola'*int(my_float))

## Operadores comparataivos ##

print(3<4) #TRUE
print(4<3) #FALSE
print(4>=3) 
print(4<=3)
print(0!=1)
print(1==2)
print(type(1==1))

#En base a esto puedo hacer una variable que...

my_bool = 4>=4

print('Lovly es gay: ' + str(my_bool))

# Podemos hacer lo mismo con letras
# Comprobacion alfabetica

print('Hola' >= 'Zola') 
print('Hola' > 'Bola')

# A menos de que no pongamos la funcion "len" se compbrobará en orden alfabetico

print(len('Hola')>=len('Bola'))

## OPERADORES LOGICOS ##

print(3>4 and 'Hola' >= 'Zola')
print(3<4 or 'Hola' < 'Zola' and 4==4)
print(not(3>4))

# Or: si es verdadero o hay verdedero sera verdadero
# And: Si es falso o hay falso sera falso
# Not: Niega cosas