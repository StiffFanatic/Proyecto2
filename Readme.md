# Proyecto 2 Fundamentos Informática Electrónica

## Autores
- Luis Enrique
- Andrés David Nazarith

## Módulo Acciones

Este módulo permite obtener datos de acciones de diferentes compañías utilizando la API de Alpha Vantage.

### Pasos para Utilizar el Módulo de Acciones

1. **Obtener Clave API de Alpha Vantage:**
   - Solicita tu clave API en [Alpha Vantage API](https://www.alphavantage.co/support/#api-key).
   - La clave API es necesaria para realizar consultas a la API de Alpha Vantage.
   - API-EJEMPLO: 7NL2I0ECZZR0RCFA

2. **Consultar Datos de Acciones:**
   - Utiliza la siguiente URL para realizar consultas:
    ```
     https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={api_key}
    ```
   - Reemplaza `{symbol}` con el símbolo de la acción que deseas consultar (por ejemplo, `AAPL` para Apple).
   - Reemplaza `{api_key}` con tu clave API de Alpha Vantage.

## Módulo Epidemiología

Este módulo permite obtener datos epidemiológicos de diferentes países utilizando la API de Statworx.

### Pasos para Utilizar el Módulo de Epidemiología

1. **Consultar Datos Epidemiológicos:**
   - Utiliza la siguiente URL para realizar consultas:
     ```
     https://api.statworx.com/covid
     ```
   - Los datos disponibles incluyen información de varios países.
   - Para obtener datos de un país específico, agrega el código del país al final de la URL (por ejemplo, `https://api.statworx.com/covid?country=US` para Estados Unidos).

2. **Utilizar la Interfaz Gráfica de Usuarios:**
   - Ejecuta el programa y sigue las instrucciones en pantalla para ingresar los parámetros requeridos.

## Interfaz Gráfica de Usuarios (GUI)

El proyecto incluye una interfaz gráfica de usuarios para interactuar con los módulos de Acciones y Epidemiología.

### Pasos para Utilizar la Interfaz Gráfica

1. **Abrir la Ventana de Acciones o Epidemiología:**
   - Ejecuta el programa y elige la opción correspondiente en la ventana principal.
   - Para Acciones, ingresa la clave API, símbolo de acción y URL API.
   - Para Epidemiología, elige la cantidad de países y/o códigos de los países.

2. **Visualizar Datos:**
   - Una vez ingresados los parámetros, podrás visualizar tablas de datos y gráficas según el módulo seleccionado.

## Ejecución del Programa

Para ejecutar el programa:
- Asegúrate de tener instalado Python en tu sistema.
- Ejecuta el archivo principal del proyecto.
- Tener instaladas las siguientes librerias.
    - Request
    - Matplotlib
    - Pandas
    - Tkinter
    