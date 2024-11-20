import serial
import requests
import time
from datetime import datetime

# Configuración de Supabase
SUPABASE_URL = "https://hxjikbhvthqfipuacmxb.supabase.co"  # Reemplaza con la URL de tu proyecto
SUPABASE_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh4amlrYmh2dGhxZmlwdWFjbXhiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzAxNjY2MjEsImV4cCI6MjA0NTc0MjYyMX0.mOZBSgGzTDBSuWSo26sEIpIdQDhfU1RlFRT_B7-8q1A"  # Reemplaza con tu clave API
SUPABASE_TABLE = "sensores"  # Reemplaza con el nombre de tu tabla

HEADERS = {
    "apikey": SUPABASE_API_KEY,
    "Authorization": f"Bearer {SUPABASE_API_KEY}",
    "Content-Type": "application/json"
}

# Configuración del puerto serial
SERIAL_PORT = 'COM5'  # Cambia esto al puerto donde está conectado tu Arduino (e.g., COM3 en Windows o /dev/ttyUSB0 en Linux)
BAUD_RATE = 9600

# Conecta al puerto serial
arduino = serial.Serial(SERIAL_PORT, BAUD_RATE)
time.sleep(2)  # Espera para que se estabilice la conexión serial

# Función para enviar datos a Supabase
def send_data_to_supabase(humidity, temperature):
    data = {
        "temperature": temperature,
        "humidity": humidity,
        "timestamp": datetime.now().isoformat()  # Agrega un timestamp
    }
    response = requests.post(f"{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}", headers=HEADERS, json=data)
    if response.status_code == 201:
        print(f"Datos enviados a Supabase: Humedad={humidity}, Temperatura={temperature}")
    else:
        print("Error al enviar datos a Supabase:", response.status_code, response.text)

# Bucle principal para leer datos del Arduino y enviarlos a Supabase
while True:
    if arduino.in_waiting > 0:
        line = arduino.readline().decode('utf-8').strip()
        if "temperatura" in line:
            # Extrae la temperatura de la línea
            temperature = float(line.split(":")[1].strip())
        elif "Humendad" in line:
            # Extrae la humedad de la línea y envía ambos datos
            humidity = float(line.split(":")[1].strip())
            send_data_to_supabase(humidity, temperature)
    
    # Espera 15 segundos antes de la próxima lectura y envío
    time.sleep(2)
