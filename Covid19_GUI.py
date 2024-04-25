import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import DatosCovid19 as dacovid  # Asumiendo que este módulo tiene la función get_covid_data

fondo = '#FFFFE0'  # Color de fondo
highlight_color = '#98FB98'  # Color botón
highlight_color2 = '#87CEFA'#Color botón 2
highlight_color3 = '#EC4F4F' #Color botón 3

def open_data_options_window(country_data):
    data_options_window = tk.Toplevel()
    data_options_window.title("Opciones de Datos")
    data_options_window.configure(bg=fondo)

    table_button = tk.Button(data_options_window, text="Mostrar Tabla de Datos", command=lambda: show_covid_table(country_data, data_options_window), bg=highlight_color)
    table_button.pack(padx=10, pady=5)

    plot_button = tk.Button(data_options_window, text="Mostrar Gráfica", command=lambda: plot_covid_data(country_data),bg=highlight_color2)
    plot_button.pack(padx=10, pady=5)
    
    Analisis_button = tk.Button(data_options_window, text="Analisis Basico", command=lambda:show_analisis(country_data,data_options_window),bg=highlight_color3)
    Analisis_button.pack(padx=10, pady=5)
    
def show_analisis(country_data, parent_window):
    analysis_window = tk.Toplevel(parent_window)
    analysis_window.title("Análisis Básico de Datos")
    analysis_window.configure(bg=fondo)
    
    # Crear widgets para ingresar parámetros de análisis
    analysis_label = tk.Label(analysis_window, text="Seleccione el tipo de análisis:")
    analysis_label.pack(padx=10, pady=5)

    analysis_options = ttk.Combobox(analysis_window, values=["Promedio", "Máximo", "Mínimo"])
    analysis_options.pack(padx=10, pady=5)

    column_label = tk.Label(analysis_window, text="Seleccione la columna de interés:")
    column_label.pack(padx=10, pady=5)

    columns = country_data[0].columns.tolist()
    column_options = ttk.Combobox(analysis_window, values=columns)
    column_options.pack(padx=10, pady=5)

    # Función para realizar el análisis
    def perform_analysis():
        analysis_type = analysis_options.get()
        selected_column = column_options.get()

        # Obtener datos del país seleccionado
        country_df = country_data[0]  # Por ahora solo tomamos el primer país
        column_data = country_df[selected_column]

        # Realizar el análisis seleccionado
        if analysis_type == "Promedio":
            result = column_data.mean()
        elif analysis_type == "Máximo":
            result = column_data.max()
        elif analysis_type == "Mínimo":
            result = column_data.min()

        # Mostrar resultado del análisis
        messagebox.showinfo("Resultado", f"El {analysis_type.lower()} de la columna '{selected_column}' es: {result}")

    # Botón para realizar el análisis
    analyze_button = tk.Button(analysis_window, text="Realizar Análisis", command=perform_analysis)
    analyze_button.pack(padx=10, pady=5)
     
def show_covid_table(country_data, parent_window):
    table_window = tk.Toplevel(parent_window)
    table_window.title("Datos COVID-19 - Tabla")

    notebook = ttk.Notebook(table_window)

    for df in country_data:
        country = df["country"].iloc[0]
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=country)
        columns = df.columns.tolist()  # Obtener todas las columnas del DataFrame
        table = ttk.Treeview(frame, columns=columns, show="headings")

        for col in columns:
            table.heading(col, text=col)
            table.column(col, anchor='center')

        if not df.empty:
            try:
                data = df.values.tolist()  # Convertir el DataFrame a una lista de listas
                for row in data:
                    table.insert("", "end", values=row)
            except Exception as e:
                print(f"Error al procesar datos para {country}: {str(e)}")
        else:
            label = tk.Label(frame, text="No hay datos disponibles para este país.")
            label.pack(padx=10, pady=10)

        # Crear y configurar la barra de desplazamiento vertical
        y_scrollbar = ttk.Scrollbar(frame, orient="vertical", command=table.yview)
        table.configure(yscrollcommand=y_scrollbar.set)
        y_scrollbar.pack(side="right", fill="y")

        # Crear y configurar la barra de desplazamiento horizontal
        x_scrollbar = ttk.Scrollbar(frame, orient="horizontal", command=table.xview)
        table.configure(xscrollcommand=x_scrollbar.set)
        x_scrollbar.pack(side="bottom", fill="x")

        table.pack(side="left", padx=10, pady=10, fill="both", expand=True)  # Empaquetar la tabla en el frame

    if not notebook.tabs():
        label = tk.Label(table_window, text="No se encontraron datos para ningún país.")
        label.pack(padx=10, pady=10)
    else:
        notebook.pack(padx=10, pady=10, fill="both", expand=True)  # Empaquetar el notebook en la ventana

def plot_covid_data(country_data):
    plot_window = tk.Toplevel()
    plot_window.title("Datos COVID-19 - Gráfico")

    fig, ax = plt.subplots(figsize=(8, 6))
    for df in country_data:
        ax.plot(df["cases"], label=df["country"].iloc[0])

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
        country_data = []
        for code in country_codes:
            # Obtener los datos de la API para cada país
            data = dacovid.get_covid_data(code)
            if data is not None:
                df = pd.DataFrame.from_dict(data)
                print(f"Datos obtenidos para {code}:")
                print(df.head())  # Mostrar primeras filas para verificar datos
                country_data.append(df)

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
    codes_window.configure(bg=fondo)
    

    code_label = tk.Label(codes_window, text="Ingrese los códigos de los países separados por comas:")
    code_label.pack(padx=10, pady=5)

    code_entry = tk.Entry(codes_window)
    code_entry.pack(padx=10, pady=5)

    confirm_button = tk.Button(codes_window, text="Siguiente", command=lambda: process_codes(code_entry.get(), codes_window))
    confirm_button.pack(padx=10, pady=10)
    confirm_button.configure(bg=highlight_color)

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
    input_window.configure(bg=fondo)

    countries_label = tk.Label(input_window, text="Cantidad de Países:")
    countries_label.pack(padx=10, pady=5)

    countries_entry = tk.Entry(input_window)
    countries_entry.pack(padx=10, pady=5)

    confirm_button = tk.Button(input_window, text="Siguiente", command=lambda: process_countries(countries_entry.get(), input_window))
    confirm_button.pack(padx=10, pady=10)
    confirm_button.configure(bg=highlight_color)

def process_countries(num_countries, input_window):
    if not num_countries.isdigit():
        messagebox.showwarning("Advertencia", "Por favor, ingrese un número válido para la cantidad de países.")
    else:
        num_countries = int(num_countries)
        input_window.destroy()
        enter_codes_window(num_countries)

