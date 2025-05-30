hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos) "))
mins = mins + dura
hour = hour + mins // 60
mins = mins % 60
hour = hour % 24

print(f"Salida: {hour}:{mins}")
