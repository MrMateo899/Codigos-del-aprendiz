edad = input ('Inserte cuantos años tiene: ')
import time
import sys

def mecanografiar(texto):

 lista = texto.split()

 for palabra in lista:
    sys.stdout.write(palabra + " ")
    sys.stdout.flush()
    time.sleep(2)

print("\n")
mecanografiar("Calculando . . .")
print("\n")

print('Tienes', edad, 'años :)')
