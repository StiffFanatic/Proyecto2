import requests

def obtener_datos(lat,lon,part,API_key):
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API_key}"
    
try:
    response = requests.get()
    
    if response.status_code == 200:
        datos = response.json()
        print()
    else:
        print("Error al obtener los datos. Código de estado: ",response.status_code)
        
except requests.RequestException as e:
    print("Error al realizar la solicitud",e)
    
    