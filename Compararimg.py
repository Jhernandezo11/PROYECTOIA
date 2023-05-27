import json
import mysql.connector
from deepface import DeepFace
import cv2


#print (DeepFace.verify('./tests/dataset/prue22.jpeg', './tests/dataset/Prueb1.jpeg')['verified'])

def verificarimg (path) :
    img = path.replace("ftp://20.121.53.224/ia/","")
    direccion = cv2.imread("./tests/dataset/" + img)
    resultado = DeepFace.verify('./tests/dataset/kate.jpg', direccion)['verified']
    print (resultado)
    return resultado
    #DeepFace.stream






