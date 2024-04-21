import requests

def get_covid_data(api_url, state_code):
    try:
        # Realizar la solicitud GET a la API
        response = requests.get(f"{api_url}/v1/states/{state_code}/current.json")
        response.raise_for_status()  # Lanzar una excepción si hay un error en la solicitud
        data = response.json()  # Convertir la respuesta a JSON
        return data
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error al obtener datos de COVID: {e}")
