from Authorization.Google import Create_Service
from googleapiclient.http import MediaFileUpload

def Upload_file(service, Fecha_hora):
    carpetas = [Fecha_hora]

    file_metadata = {
        "name" : carpetas,
        "parents" : ['1gLvuTA0ptlZRQBGq9tLNjoDJDjQJNaWH'],
        "mimeType" : "application/vnd.google-apps.folder"
    }

    file = service.files().create(body=file_metadata).execute()

    carpeta_id = file.get('id')
    print('File ID: %s' % carpeta_id)

    return carpeta_id

def Upload_ss(imagenes, Fecha_hora):
    x = 1

    service = Create_Service()
    print(service)

    carpeta_id = Upload_file(service, Fecha_hora)

    for i in range(len(imagenes)):

        file_metadata = {
            "name"    : 'ss_'+str(i+1)+'.png',
            "parents" : [carpeta_id]
        }

        media = MediaFileUpload('./Images/'+Fecha_hora+'/ss_'+str(i+1)+'.png', mimetype='image/png')

        service.files().create(body = file_metadata, media_body = media).execute()

    return "Uploaded images"
