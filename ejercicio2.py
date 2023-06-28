abrir = open ('texto.txt' , 'r', encoding = 'utf-8')

texto = abrir.read()

palabras = texto.split(" ")

diccionario ={}

for i in palabras:
    if i in diccionario:

        diccionario[i] += 1
    else: 
        diccionario[i] = 1

for i in diccionario: 
    veces= diccionario[i]
    print (f'La palabra {i} se encuentra {veces} veces')