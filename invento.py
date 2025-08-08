import pywhatkit as kit
from datetime import datetime

def enviar_whatsapp(numero: str,
                    mensaje: str,
                    hora: int,
                    minuto: int):
    
    kit.sendwhatmsg(
        "+{numero}",
        mensaje,
        hora,
        minuto,
        wait_time=20,
    )
    
if __name__== "__main__":
    numero = "50685179043"
    mensaje = "Despierta profe ya lo hice"
    hora = 7
    minuto = 54
    
    enviar_whatsapp(numero,mensaje,hora,minuto)
    print("")
