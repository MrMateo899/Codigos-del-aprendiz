## STRINGS ##

my_string_variable = 'My String Variable'
my_other_string = "My other string variable"

print(len(my_string_variable))
print(len(my_other_string))

print(my_string_variable + " " + my_other_string)

my_new_line_string = 'Este es un string \nCon salto de linea'
print(my_new_line_string)

my_tab_string = '\tEste es un string con tabulacion'
print(my_tab_string)

my_escape_string = '\\tEste es un string \\nescapado'
print(my_escape_string)

## FORMATEO ##

name, surname, age = 'Mateo', 'Yamamoto', 13

print('Mi nombre es {} {} y mi edad es {} años.'.format(name, surname, age))
print('Mi nombre es %s %s y mi edad es %d años.' %(name, surname, age))
print('Mi nombre es', name, surname, 'y mi edad es', str(age), 'años.')
print(f'Mi nombre es {name} {surname} y mi edad es {age} años.' )

# Desemparquetado de caracteres
language = 'python'
a, b , c, d, e, f= language
print(a)
print(e)

# Division

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

#Reverse

reversed_language = language[:: -1]
print(reversed_language)

# FUNCIONES

print(language.capitalize())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.upper())
print(language.lower())
print(language.lower().isupper())
print(language.startswith('Py'))
