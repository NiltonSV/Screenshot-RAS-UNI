from Functions.Screenshot import Take_ss
from Functions.Upload import Upload_ss

imagenes, Fecha_hora = Take_ss()

print(Upload_ss(imagenes, Fecha_hora))