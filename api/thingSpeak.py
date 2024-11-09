import random
import time
import requests

# Clave de escritura de ThingSpeak y URL de la API
THINGSPEAK_WRITE_API_KEY = "78NHK2NHNDWAU5MV"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# Variables para almacenar los últimos valores generados
last_temperature = -10  # Iniciar por debajo del límite mínimo
last_humidity = 0       # Iniciar en el mínimo valor de humedad

while True:
    # Generar valores aleatorios para temperatura y humedad
    temperature = random.uniform(-10, 100)
    humidity = random.uniform(0, 100)

    # Verificar si el nuevo valor supera al último registrado
    if temperature > last_temperature or humidity > last_humidity:
        # Actualizar los últimos valores registrados
        last_temperature = temperature
        last_humidity = humidity

        # Crear el diccionario de datos para ThingSpeak
        data = {
            "api_key": THINGSPEAK_WRITE_API_KEY,
            "field1": temperature,
            "field2": humidity
        }

        # Enviar datos a ThingSpeak
        response = requests.post(THINGSPEAK_URL, data=data)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            print(f"Datos enviados correctamente: Temperatura={temperature:.2f}°C, Humedad={humidity:.2f}%")
        else:
            print(f"Error al enviar datos: {response.status_code} - {response.text}")

    # Esperar 3 segundos antes de la siguiente iteración
    time.sleep(3)
