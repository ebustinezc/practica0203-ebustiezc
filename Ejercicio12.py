# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que 
# aparece la letra en la frase.
frase = input('Escribe una frase:')
letra = input('Escribe una letra:')
contar = 0
for i in frase:
    if i == letra:
        contar +=1
print('La letra', letra ,'aparece' , contar , 'veces en la frase escrita.')