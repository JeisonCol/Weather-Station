import random
import time
import requests

# Clave de escritura de ThingSpeak y URL de la API
THINGSPEAK_WRITE_API_KEY = "3ALJCF4JBHY3T2BS"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# Configuración de consumo promedio (en Wh) para cada dispositivo
device_consumption = {
    "nevera": (50, 150),  # Consumo en Wh para simular un rango
    "lavadora": (500, 1500),
    "ducha": (4000, 6000),
    "computadora": (50, 250),
    "televisor": (30, 100)
}

while True:
    # Generar valores aleatorios de consumo para cada dispositivo
    fridge_consumption = random.uniform(*device_consumption["nevera"])
    washer_consumption = random.uniform(*device_consumption["lavadora"])
    shower_consumption = random.uniform(*device_consumption["ducha"])
    computer_consumption = random.uniform(*device_consumption["computadora"])
    tv_consumption = random.uniform(*device_consumption["televisor"])

    # Crear el diccionario de datos para ThingSpeak
    data = {
        "api_key": THINGSPEAK_WRITE_API_KEY,
        "field1": fridge_consumption,
        "field2": washer_consumption,
        "field3": shower_consumption,
        "field4": computer_consumption,
        "field5": tv_consumption
    }

    # Enviar datos a ThingSpeak
    response = requests.post(THINGSPEAK_URL, data=data)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        print(f"Datos enviados correctamente:")
        print(f"  Nevera: {fridge_consumption:.2f} Wh")
        print(f"  Lavadora: {washer_consumption:.2f} Wh")
        print(f"  Ducha: {shower_consumption:.2f} Wh")
        print(f"  Computadora: {computer_consumption:.2f} Wh")
        print(f"  Televisor: {tv_consumption:.2f} Wh")
    else:
        print(f"Error al enviar datos: {response.status_code} - {response.text}")

    # Esperar 15 minutos antes de la siguiente iteración para simular lecturas cada 15 minutos
    time.sleep(20)
