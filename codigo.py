#Importamos bibliotecas:
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import  numpy as np
from PIL import Image

#Para que sea mostrado en Jupyter:-activar en tal caso-
#%matplotlib inline

#Importamos imagenes:
bienv=Image.open("imagen.jpg")

imag=np.array(bienv)

#Tipo de dato:
print(type(imag))
#Dimensión:
print(imag.ndim)
print(imag.shape)

#Ver imagen:
plt.figure(figsize=(8.8))
plt.imshow(imag)

#Abrimos el archivo:
libreria=open("libros.csv").readlines()
#Armamos diccionario:
header=libreria[0]
libros={}

#Obtenemos los nombres de las columnas como claves del diccionario
for columna in header.split(";"):
	columna=columna.strip().lower()
	libros[columna]=[]

#Convertimos todo a Nunpy (operador de vectores y matrices):
for elemento in libros:
	libros[elemento]=np.array(libros[elemento])

#Convertir a int los datos que sean necesarios:
precios= list (libros.keys())[3: ]
for elemento in precios:
	libros[elemento]=libros[elemento.astype(np.int)]
#A string:
autor= list (libros.keys())[1: ]
for elemento in autor:
	libros[elemento]=libros[elemento.astype(np.string)]

#Gráficamos:
plt.bar(libros["Autor"],libros["Precios"])
plt.xticks(rotation=90)
plt.title("Ventas")

#Ahora trabajamos dataframe:
libro2=pd.read_csv("libros.csv",sep=";")

#Separado por “;” lo muestra con:
libro2.head()

#Verificamos nombres de columnas:
libro2.columns

#Le damos un índice de selección:
libro2.iloc[:,[0,3,1]]

#1. Separamos por países:
paises=libro2.groupby("Nacionalidad")

#Vemos la separación:
paises.groups

#Ver lista separada/iterable:
for pais, libro in paises:
	print("======================")
	print(pais)
	print("======================")
	print(libro)
	print()

#Seleccionamos una columna para trabajar:
paises.max()

#2. Separamos por escritor:
escritor=libro2.groupby("Autor")

#Vemos la separación:
escritor.groups

#Ver lista separada/iterable:
for autor, libro in escritor:
 	print("======================")
	print(autor)
	print("======================")
	print(libro)
	print()

#Seleccionamos una columna para trabajar:
escritor.max()

type(libro2)
libro2.info()

%matplotlib inline

libro2.plot()
libro2.plot(kind="bar", x="Titulo")

# -------------------------------------------------------------------------------------
# Agregar columna de compras (randomizada)
import random
lista_compras = [1]

"Función:
def listaAleatorios(n):
	lista = [0]  * n
	for i in range(n):
		lista[i] = random.randint(0, 1000)
	return lista

lista_compras=listaAleatorios(20)
	print(lista_compras)

# Añadirla al df
import pandas as pd
libro2 = pd.DataFrame(lista_compras)
libro2['Cantidades compradas'] = lista_compras


#Fechas dataframe:
fechas=pd.read_csv("Fechas.csv",sep=";")

fechas.head()

#Función:
def listaAleatorios(n):
	lista = [0]  *n
	for i in range(n):
		lista[i] = random.randint(1, 12)
	return lista
fechas=listaAleatorios(20)
print(fechas)

libro2 = pd.DataFrame(libro2)
libro2['fechas'] = fechas
libro2.head()

#Imagen despedida:
im_R= imag.copy()
im_R[:,:,(1,2)]=0
im_G=imag.copy()
im_G[:,:,(0,2)]=0
im_B=imag.copy()
im_B=[:,:,(0,1)]=0

im_RGb=np.concatenate((im_R, im_G, im_B),axis=1)
plt.imshow(im_RGB);