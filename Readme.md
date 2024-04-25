# Proyecto 2 Fundamentos Informática Electrónica
##  Autores
- Luis Enrique Sandoval
- Andrés David Nazarith
## Descripción
- Este proyecto implementa una interfaz gráfica de usuarios para interactuar con los módulos de Acciones y Epidemiología. Permite obtener datos de acciones de diferentes compañías utilizando la API de Alpha Vantage, datos epidemiológicos de diferentes países utilizando la API de Statworx y proporcionar un analisis básico de los datos epidemiológicos.

## Requisitos
- Python
- Librerías:
   -requests
   -matplotlib
   -pandas
   -tkinter
   -tkcalendar
### Instalación de librerias
   -Puedes instalar las librerias necesarias ejecutando el siguiente comando:

```bash
pip install requests matplotlib pandas tkinter tkcalendar
```

## Uso
## Interfaz Gráfica de Usuarios (GUI)

El proyecto incluye una interfaz gráfica de usuarios para interactuar con los módulos de Acciones y Epidemiología.

### Pasos para Utilizar la Interfaz Gráfica

1. **Abrir la Ventana de Acciones o Epidemiología:**
   - Ejecuta el programa y elige la opción correspondiente en la ventana principal.
   - Para Acciones, ingresa la clave API, símbolo de acción y URL API.
   - Para Epidemiología, elige la cantidad de países y/o códigos de los países.

2. **Visualizar Datos:**
   - Una vez ingresados los parámetros, podrás visualizar tablas de datos y gráficas según el módulo seleccionado.


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

## Ejemplos de Parámetros
### Países
1. US - Estados Unidos
2. CN - China
3. IN - India
4. JP - Japón
5. DE - Alemania
6. FR - Francia
7. IT - Italia
8. UK - Reino Unido
9. BR - Brasil
10. MX - México
11. CA - Canadá
12. AU - Australia
13. KR - Corea del Sur
14. ES - España
15. RU - Rusia
16. NL - Países Bajos
17. ID - Indonesia
18. SA - Arabia Saudita
19. TR - Turquía
20. AR - Argentina
    
### Símbolos de Acciones
1. AAPL - Apple Inc.
2. MSFT - Microsoft Corporation
3. AMZN - Amazon.com Inc.
4. GOOG - Alphabet Inc. (Google)
5. FB - Meta Platforms Inc. (Facebook)
6. TSLA - Tesla Inc.
7. JPM - JPMorgan Chase & Co.
8. V - Visa Inc.
9. BABA - Alibaba Group Holding Limited
10. BAC - Bank of America Corporation
11. NVDA - NVIDIA Corporation
12. WMT - Walmart Inc.
13. KO - The Coca-Cola Company
14. PFE - Pfizer Inc.
15. JNJ - Johnson & Johnson
16. NFLX - Netflix Inc.
17. DIS - The Walt Disney Company
18. CRM - Salesforce.com Inc.
19. ORCL - Oracle Corporation
20. CSCO - Cisco Systems Inc.
    
## Ejecución del Programa
- Para ejecutar el programa:

   - Asegúrate de tener instalado Python en tu sistema.
   - Ejecuta el archivo principal del proyecto.
