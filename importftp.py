
import ftplib

def descargar_imagen_ftp (path):
    img = path.replace("ftp://20.121.53.224/ia/","")
    ftp = ftplib.FTP("20.121.53.224") 
    ftp.login("ftp2", "ftp2") 
    ftp.cwd("ia/")
    ftp.retrbinary("RETR " + img , open("./tests/dataset/" + img, 'wb').write) 
    ftp.quit()
# Llamar a la función para descargar la imagen
# descargar_imagen_ftp()


