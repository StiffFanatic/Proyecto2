import requests
import json
import pandas as pd

def get_covid_data(state_code):
    try:
        # POST to API
        payload = {'code': state_code}
        URL = 'https://api.statworx.com/covid'
        response = requests.post(url=URL, data=json.dumps(payload))

        # Convert to data frame
        df = pd.DataFrame.from_dict(json.loads(response.text))
        df = df.iloc[:, :12]

        return df
    except Exception as e:
        raise Exception(f"Error al obtener datos de COVID: {str(e)}")
