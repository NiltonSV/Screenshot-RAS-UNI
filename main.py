import keyboard
import os

from datetime import datetime
from PIL import ImageGrab
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

# x = 1
# imagenes = [] # Lista para guardar los nombres de las imágenes

# #ALMACENAMOS EN UNA VARIABLE LA FECHA Y HORA DE LA REUNIÓN
# Fecha_hora = datetime.now().strftime('%Y-%m-%d %H;%M;%S')

# #CREAMOS LA CARPETA DONDE GUARDAREMOS LAS IMÁGENES DE LA REUNIÓN
# if os.path.exists('/Users/PC/Desktop/Screenshot_RAS_UNI/'+Fecha_hora):
#    print("La carpeta ya existe")
# else:
#    os.mkdir('/Users/PC/Desktop/Screenshot_RAS_UNI/'+Fecha_hora)

# while True:
#    # Con keyboard.read_key() leeremos la tecla que se presiona
#     if keyboard.read_key() == "imp pant":
#         # Guardamos en una variable la ruta y nombre de la imagen
#         save_path = '/Users/PC/Desktop/Screenshot_RAS_UNI/'+Fecha_hora+'/ss_'+str(x)+'.png'
#         ImageGrab.grab().save(save_path)  
#         imagenes.append("ss_"+str(x)+".png") # Agregamos el nombre a la lista imagenes
#         x += 1
#         print("Imagen guardada") # Referencia para ver si la imagen se tomó

#     elif keyboard.read_key() == "ctrl": # Salimos del while cuando presionamos la tecla ctrl
#         break

# print(imagenes)


#*********************

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']


def create_service():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credenciales.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)
        return service
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')

service = create_service()

file_metadata = {
   "name" : "ss1",
   "parents" : ['1j0gjXt8RLsJskdE2-hmJIHKmtH39ScNg'],
}

media = MediaFileUpload("Imagen1.png", mimetype='image/png')

file = service.files().create(body = file_metadata, media_body = media).execute()