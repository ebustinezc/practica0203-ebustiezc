# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar 
# un error.
n1 = float(input('Dime un Nº:'))
n2 = float(input('Dime un Nº:'))
if n2 == 0:
    print('Error')
else:
    print(n1/n2)