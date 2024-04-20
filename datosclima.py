import requests

def obtener_datos(lat, lon,time):
    
    API_key = "20628fc3610bd5741706c0bdf251e03d"
    
    url = f"https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid={API_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        datos = response.json()
        print(datos)
    else:
        print("Error al obtener los datos. Código de estado:", response.status_code)



