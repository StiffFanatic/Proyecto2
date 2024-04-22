import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import DatosCovid19 as dacovid

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

def open_data_options_window(country_data):
    data_options_window = tk.Toplevel()
    data_options_window.title("Opciones de Datos")

    table_button = tk.Button(data_options_window, text="Mostrar Tabla de Datos", command=lambda: show_covid_table(country_data, data_options_window))
    table_button.pack(padx=10, pady=5)

    plot_button = tk.Button(data_options_window, text="Mostrar Gráfica", command=lambda: plot_covid_data(country_data))
    plot_button.pack(padx=10, pady=5)
    
def show_covid_table(country_data, parent_window):
    table_window = tk.Toplevel(parent_window)
    table_window.title("Datos COVID-19 - Tabla")

    columns = list(COLUMNAS_ESPANOL.values())
    table = ttk.Treeview(table_window, columns=columns, show="headings")

    for col in columns:
        table.heading(col, text=col)
        table.column(col, anchor='center')

    for country, cases in country_data.items():
        try:
            # Obtener los datos de la API para cada país
            data = dacovid.get_covid_data(country)
            if data is not None:
                df = pd.DataFrame.from_dict(data)
                row_values = []
                for col in columns:
                    # Obtener el valor correspondiente o cadena vacía si no existe
                    value = df[COLUMNAS_ESPANOL.get(col.lower(), "")].iloc[0]
                    row_values.append(value)
                table.insert("", "end", values=row_values)
            else:
                print(f"No se encontraron datos para {country}")
        except Exception as e:
            print(f"Error al obtener datos para {country}: {str(e)}")

    table.pack(padx=10, pady=10)



def plot_covid_data(country_data):
    plot_window = tk.Toplevel()
    plot_window.title("Datos COVID-19 - Gráfico")

    fig, ax = plt.subplots(figsize=(8, 6))
    for country, cases in country_data.items():
        ax.plot(cases, label=country)

    ax.set_xlabel("Días desde el primer caso")
    ax.set_ylabel("Casos")
    ax.set_title("Evolución de Casos de COVID-19")
    ax.legend()
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=plot_window)
    canvas.draw()
    canvas.get_tk_widget().pack(padx=10, pady=10)

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
            open_data_options_window(country_data)
        else:
            messagebox.showerror("Error", "No se pudo obtener información de COVID para los países ingresados.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al obtener datos: {str(e)}")

def enter_codes_window(num_countries):
    # Crear la ventana para ingresar los códigos
    codes_window = tk.Toplevel()
    codes_window.title("Ingresar Códigos de Países")

    code_label = tk.Label(codes_window, text="Ingrese los códigos de los países separados por comas:")
    code_label.pack(padx=10, pady=5)

    code_entry = tk.Entry(codes_window)
    code_entry.pack(padx=10, pady=5)

    confirm_button = tk.Button(codes_window, text="Siguiente", command=lambda: process_codes(code_entry.get(), codes_window))
    confirm_button.pack(padx=10, pady=10)

def process_codes(codes_str, codes_window):
    codes = [code.strip() for code in codes_str.split(",") if code.strip()]  # Obtener códigos de países como lista
    if not codes:
        messagebox.showwarning("Advertencia", "Por favor, ingrese al menos un código de país.")
    else:
        show_covid_data(codes)
        codes_window.destroy()

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

