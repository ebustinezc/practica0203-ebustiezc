# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra 
# introducida empezando por la última.
Palabra = input('Escribe una palabar:')
m = -1
for x in range(len(Palabra)):
    print(Palabra[m])
    m = m-1