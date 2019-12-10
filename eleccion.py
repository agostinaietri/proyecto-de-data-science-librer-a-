# Entrada (parte 1)
opcion = input("Qué desea leer? (inserte género)")

# Salida: recomendaciones en función de género
if opcion == "ciencia ficción":
    print("Te recomendamos Harry Potter: Las Reliquias de la Muerte de J.K Rowling o Foundation de Isaac Asimov")

if opcion == "terror":
    print("Te recomendamos Necronomicón de H.P Lovecraft o The Stand de Stephen King")

if opcion == "drama":
    print("Te recomendamos Comer, Rezar y Amar de Elizabeth Gilbert")

if opcion == "policial":
    print("Te recomendamos Muerte en el Nilo de Agatha Christie o El Túnel de Ernesto Sabato")

if opcion == "drama":
    print("Te recomendamos The Portrait of Dorian Gray de Oscar Wilde o Los Ojos del Perro Siberiano de Antonio Santana")

if opcion == "ciencia":
    print("Te recomendamos The Chemical Basis of Morphogenesis de Alan Turing o La Historia del Tiempo de Stephen Hawking")

# Librerías (parte 2)
libreria=open("libros.csv").readlines()
import random
import numpy as num
header=libreria[0]
libros={}

#Obtenemos los nombres de las columnas como claves del diccionario
for columna in header.split(";"):
	columna=columna.strip().lower()
	libros[columna]=[]

#Convertimos todo a Nunpy (operador de vectores y matrices):
for elemento in libros:
	libros[elemento]=np.array(libros[elemento])

# Convertir a string la columna
titulos= list (libros.keys())[2: ]
for elemento in titulos:
	librosC=libros[elemento.astype(np.string)]

# Hacemos el random
veces = random.randint(1,5)
hoy_leo = titulos[veces]

# Salida: título random
if opcion == upper(si) and lower(si):
    print("Te recomendamos leer", hoy_leo)
else:
    print("Gracias por visitarnos")
