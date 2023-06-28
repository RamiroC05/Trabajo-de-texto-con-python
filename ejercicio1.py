abrir = open ('texto.txt', 'r')  

texto = abrir.read()

espacios_blancos = texto.count(' ')


print (f'La cantidad de caracteres que posee el texto es igual a {len(texto) - espacios_blancos}')


abrir.close()

#Trabajo-de-texto-con-python
#Resoluciones-algoritmicas-con-python



