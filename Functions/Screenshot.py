import keyboard
import os

from PIL import ImageGrab
from datetime import datetime

def Create_File():

    #ALMACENAMOS EN UNA VARIABLE LA FECHA Y HORA DE LA REUNIÓN
    Fecha_hora = datetime.now().strftime('%Y-%m-%d %H;%M;%S')

    #CREAMOS LA CARPETA DONDE GUARDAREMOS LAS IMÁGENES DE LA REUNIÓN
    if os.path.exists('./Images/'+Fecha_hora):
        print("La carpeta ya existe")
    else:
        os.mkdir('./Images/'+Fecha_hora)
    
    return Fecha_hora

def Take_ss():

    x = 1
    imagenes = [] # Lista para guardar los nombres de las imágenes

    Fecha_hora = Create_File()

    while True:

        # Con keyboard.read_key() leeremos la tecla que se presiona
        if keyboard.read_key() == "imp pant":

            # Guardamos en una variable la ruta y nombre de la imagen
            save_path = './Images/'+Fecha_hora+'/ss_'+str(x)+'.png'
            ImageGrab.grab().save(save_path)  
            imagenes.append("ss_"+str(x)+".png") # Agregamos el nombre a la lista imagenes
            x += 1
            print("Imagen guardada") # Referencia para ver si la imagen se tomó

        elif keyboard.read_key() == "ctrl": # Salimos del while cuando presionamos la tecla ctrl
            break
    
    return imagenes, Fecha_hora