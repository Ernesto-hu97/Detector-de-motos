# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 10:04:20 2023
UNIVERSIDA ATONOMA DEL ESTADO DE MÉXICO
CU ZUMPANGO 
SISTEMAS EXPERTOS
PROYECTO EXTRAORDINARIO 
DETECTOR DE MOTOS 
JOSE ERNESTO HUITZILT GONZALEZ 
@author: all
"""
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from tensorflow.keras.utils import load_img, img_to_array
from keras.models import load_model


"""creacion de una ventana"""

ventana = tk.Tk()
ventana.title("Test TB")
ventana.geometry("800x600")
ventana. resizable(0,0)

"""Etiquetas"""

cabezera = tk.Label(ventana, text= " Welcome ").pack()
label = tk.Label(ventana)
label_2 = tk.Label(ventana)


"""importamos los pesos"""
longitud, altura = 100,100
modelo='./modelo/modelo.h5'
pesos='./modelo/pesos.h5'

cnn = load_model(modelo)
cnn.load_weights(pesos)


"""Predecimos la imagen"""
def predict(file):
  x = load_img(file, target_size=(longitud, altura))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  areglo = cnn.predict(x) #[1,0,0]
  resultado = areglo[0]
  respuesta = np.argmax(resultado)
  
  if respuesta == 0:
      print("Es una moto de Aventura")
      print("Alcanza una velocidad de 150 Km/h")
      print("Tiene un motor 250cc")
      label_2.config(text="Es una moto de Aventura\n Alcanza una velocidad de 150 Km/h 180Km/h\n Tiene un motor 250cc a 300cc\n Es apta para vias primarias")
    
  elif respuesta == 1:
       print("Es una motocicleta Chooper")
       print("Alcanza una velocidad de 130 a 150 Km/h")
       print("Tiene un motor 200cc a 250cc")
       label_2.config(text="Es una motocicleta Chooper\n Alcanza una velocidad de 130 a 150 Km/h\n Tiene un motor 200cc a 250cc\n Algunas son aptas para vias primarias")
       
  elif respuesta == 2:
      print("Es una motocicleta de Ciudad")
      print("Alcanza una velocidad de 90 a 110 Km/h")
      print("Tiene un motor 125 a 150cc")
      label_2.config(text="Es una motocicleta de ciudad \n Alcanza una velocidad de 90 a 110 Km/h\n Tiene un motor 125cc a 150cc\n No es apta para vias primarias")
  
  elif respuesta == 3:
     print("Es una motocicleta Doble Proposito")
     print("Alcanza una velocidad de 130 a 150 Km/h")
     print("Tiene un motor 200cc a 250cc")
     label_2.config(text="Es una motocicleta Docle Proposito\n Alcanza una velocidad de 130 a 150 Km/h\n Tiene un motor 200cc a 250cc\n Algunas son aptas para vias primarias")
  
  elif respuesta == 4:
      print("Es una motoneta")
      print("Alcanza una velocidad de 90 a 110 Km/h")
      print("Tiene un motor 125 a 150cc")
      label_2.config(text="Es una motoneta \n Alcanza una velocidad de 90 a 110 Km/h\n Tiene un motor 125cc a 150cc\n No es apta para vias primarias")
      
  elif respuesta == 5:
       print("Es una motocicleta Sport")
       print("Alcanza una velocidad de 150 a 170 Km/h")
       print("Tiene un motor 250cc a 280cc")
       label_2.config(text="Es una motocicleta Sport\n Alcanza una velocidad de 150 a 170 Km/h\n Tiene un motor 250cc a 280cc\n Es aptas para vias primarias")
       
       
  elif respuesta == 6:
      print("Es una motocicleta de Trabajo")
      print("Alcanza una velocidad de 90 a 110 Km/h")
      print("Tiene un motor 125 a 150cc")
      label_2.config(text="Es una motocicleta de Trabajo \n Alcanza una velocidad de 90 a 110 Km/h\n Tiene un motor 125cc a 150cc\n No es apta para vias primarias")
  
  return respuesta



"""Comando de Botones"""

       

def salir():
    ventana.destroy()
    
def limpiar():
    label_2.config(text="")
    
def abrirArchivos ():
    
    # Muestra un diálogo para seleccionar el archivo
      
      global file_path 
      file_path = filedialog.askopenfilename(title="Abrir")
     
      # Carga la imagen en una variable
      image = Image.open(file_path)
      
      image = ImageTk.PhotoImage(image)
      
      # Asigna la imagen al label
      label.config(image=image)
      label.image = image
      label.pack()
      label.place(x=10,y=30, height=400, width = 500)
      
def saludo():
   archivo_img = file_path
   predict(archivo_img)
   
   label_2.pack()
   label_2.place(x=550,y=10,height=400, width = 250)

"""Botones para la consola """
boton = tk.Button(ventana, text="Escanear", command = saludo, fg='black')
boton.pack()
boton.place(x=200, y= 500, height= 50, width= 100)

boton2 = tk.Button(ventana, text="Salir", command = salir, fg='red')
boton2.pack()
boton2.place(x=440, y= 500, height= 50, width= 100)

boton3 = tk.Button(ventana, text="Buscar Archivo", command = abrirArchivos, fg='blue')
boton3.pack()
boton3.place(x=80, y= 500, height= 50, width= 100)

boton4 = tk.Button(ventana, text="Limpiar", command = limpiar, fg='black')
boton4.pack()
boton4.place(x=320, y= 500, height= 50, width= 100) 

"""Mostramos la ventana """
ventana.mainloop()






