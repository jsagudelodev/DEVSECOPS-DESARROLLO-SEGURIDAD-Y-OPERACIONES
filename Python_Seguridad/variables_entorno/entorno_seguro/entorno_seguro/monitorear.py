import requests
import time

def monitorear_servidor():
    url="http://127.0.0.1:8000/"
    while True:
        try:
            response=requests.get(url)
            if response.status_code==200:
                print("El Servidor funciona correctamente")
            else:
                print("Respuesta Inesperada",response.status_code)    
        except:
            print("El Servidor no response , posibler caida o ataque")        
        time.sleep(10) #Espera 10 segundos antes de volver a probar    

monitorear_servidor()

"""
Libreria para monitorear
============================
logging =	Registrar eventos del sistema
psutil =	Medir uso de CPU, RAM y disco
requests =	Verificar si un sitio o API está activa
smtplib =	Enviar alertas por correo
schedule =	Ejecutar tareas automáticamente cada cierto tiempo
"""