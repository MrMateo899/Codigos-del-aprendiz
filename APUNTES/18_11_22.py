# Variables

my_string_variable = 'My String Variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str = str(my_int_variable)
print(my_int_variable)
print(type(my_int_to_str))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables en un print
print(my_string_variable, str(my_int_variable), my_bool_variable)
print('Este es el valor de:', my_bool_variable)

# Funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea (No recomendable por la mantencion del codigo)
name, surname, alias, edad = 'Mateo', 'Lopez', 'MrMateo899/Yamamoto', 13
print('Me llamo:', name, surname + '. Mi alias es: ', alias, 'y tengo', edad, 'años')

# Inputs y Variables que cambian

'''
name = input('¿Cuál es tu nombre?')
edad = input('¿Qué edad tienes?')
print(name)+
print(edad)
'''

name = 123
age = 'Pepe'
print(name)
print(age)

#Forzar tipo
address: str= 'Mi direccion'
address = 13
print(type(address))