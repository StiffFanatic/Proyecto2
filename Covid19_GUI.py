import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import DatosCovid19 as dacovid
import matplotlib.pyplot as plt

# Definir nombres en español para las columnas
COLUMNAS_ESPANOL = {
    "date": "Fecha",
    "day": "Día",
    "month": "Mes",
    "year": "Año",
    "cases": "Casos",
    "deaths": "Fallecidos",
    "country": "País",
    "code": "Código",
    "population": "Población",
    "continent": "Continente",
    "cases_cum": "Casos acumulados",
    "deaths_cum": "Fallecidos acumulados"
}

def show_covid_data(country_codes):
    try:
        country_data = {}
        for code in country_codes:
            # Obtener los datos de la API para cada país
            data = dacovid.get_covid_data(code)
            if data is not None:
                df = pd.DataFrame.from_dict(data)
                country_data[df["country"].iloc[0]] = df["cases"]

        if country_data:
            plot_covid_data(country_data)
        else:
            messagebox.showerror("Error", "No se pudo obtener información de COVID para los países ingresados.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al obtener datos: {str(e)}")

def plot_covid_data(country_data):
    plt.figure(figsize=(10, 6))
    for country, cases in country_data.items():
        plt.plot(cases, label=country)

    plt.xlabel("Días desde el primer caso")
    plt.ylabel("Casos")
    plt.title("Evolución de Casos de COVID-19")
    plt.legend()
    plt.grid(True)
    plt.show()

def open_covid19_window():
    # Crear la ventana de ingreso de cantidad de países
    input_window = tk.Toplevel()
    input_window.title("Ingresar Cantidad de Países")

    countries_label = tk.Label(input_window, text="Cantidad de Países:")
    countries_label.pack(padx=10, pady=5)

    countries_entry = tk.Entry(input_window)
    countries_entry.pack(padx=10, pady=5)

    confirm_button = tk.Button(input_window, text="Siguiente", command=lambda: process_countries(countries_entry.get(), input_window))
    confirm_button.pack(padx=10, pady=10)

def process_countries(num_countries, input_window):
    if not num_countries.isdigit():
        messagebox.showwarning("Advertencia", "Por favor, ingrese un número válido para la cantidad de países.")
    else:
        num_countries = int(num_countries)
        input_window.destroy()
        enter_codes_window(num_countries)

def enter_codes_window(num_countries):
    # Crear la ventana para ingresar los códigos
    codes_window = tk.Toplevel()
    codes_window.title("Ingresar Códigos de Países")

    code_label = tk.Label(codes_window, text="Ingrese los códigos de los países separados por comas:")
    code_label.pack(padx=10, pady=5)

    code_entry = tk.Entry(codes_window)
    code_entry.pack(padx=10, pady=5)

    confirm_button = tk.Button(codes_window, text="Mostrar Gráfica", command=lambda: process_codes(code_entry.get(), codes_window))
    confirm_button.pack(padx=10, pady=10)

def process_codes(codes_str, codes_window):
    codes = [code.strip() for code in codes_str.split(",") if code.strip()]  # Obtener códigos de países como lista
    if not codes:
        messagebox.showwarning("Advertencia", "Por favor, ingrese al menos un código de país.")
    else:
        show_covid_data(codes)
        codes_window.destroy()

