import requests
import json
import pandas as pd

def get_covid_data(state_code):
    try:
        # POST to API
        payload = {'code': state_code}
        URL = 'https://api.statworx.com/covid'
        response = requests.post(url=URL, data=json.dumps(payload))

        # Convertir la respuesta a DataFrame
        df = pd.DataFrame.from_dict(json.loads(response.text))
        df = df.iloc[:, :12]

        # Verificar si la columna 'Casos acumulados' está presente
        

        return df
    except Exception as e:
        raise Exception(f"Error al obtener datos de COVID: {str(e)}")
