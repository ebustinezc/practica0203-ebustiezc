# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que 
# tributar o no.
edad = int(input('Dime tu edad:'))
sueldo = int(input('cuales son tus ingresos mensuales:'))
if edad > 16 and (sueldo >= 1000):
    print('tienes que tribitar')
else:
    print('No tienes que tributar')