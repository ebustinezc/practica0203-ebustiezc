# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña 
# hasta que introduzca la contraseña correcta.
n = input('Dime tu contraseña:')
m = input('Escribe tu contraseña:')
while n != m:
    print('CONTRASEÑA INCORRECTA')
    m = input('Vuelve a introducir la contraseña:')
print('CONTRASEÑA CORRECTA:)')