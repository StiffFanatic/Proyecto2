import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
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

def show_covid_data_window(df):
    # Crear una nueva ventana para mostrar los datos
    result_window = tk.Toplevel()
    result_window.title("Datos de COVID")

    # Crear un Treeview para mostrar los datos en forma de tabla
    tree = ttk.Treeview(result_window)
    tree.pack(expand=True, fill=tk.BOTH)

    # Configurar las columnas
    columnas_mostrar = [col for col in df.columns if col in COLUMNAS_ESPANOL]
    tree["columns"] = columnas_mostrar
    for col in columnas_mostrar:
        tree.heading(col, text=COLUMNAS_ESPANOL[col])
        tree.column(col, anchor=tk.CENTER, width=130)
        
    # Insertar los datos en el Treeview
    for index, row in df.iterrows():
        tree.insert("", "end", values=[row[col] for col in columnas_mostrar])

    # Agregar barras de desplazamiento
    scrollbar_y = ttk.Scrollbar(result_window, orient="vertical", command=tree.yview)
    scrollbar_y.pack(side="right", fill="y")
    tree.configure(yscrollcommand=scrollbar_y.set)

    scrollbar_x = ttk.Scrollbar(result_window, orient="horizontal", command=tree.xview)
    scrollbar_x.pack(side="bottom", fill="x")
    tree.configure(xscrollcommand=scrollbar_x.set)

    # Centrar la ventana en la pantalla
    center_window(result_window)

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x_offset = (window.winfo_screenwidth() - width) // 2
    y_offset = (window.winfo_screenheight() - height) // 2
    window.geometry(f"{width}x{height}+{x_offset}+{y_offset}")

def show_covid_data(state_code):
    try:
        # Obtener los datos de la API y crear el DataFrame
        data = dacovid.get_covid_data(state_code)
        if data is not None:
            df = pd.DataFrame.from_dict(data)
            show_covid_data_window(df)
        else:
            messagebox.showerror("Error", "No se pudo obtener la información de COVID.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al obtener datos: {str(e)}")

def open_covid19_window():
    # Crear la ventana de ingreso de datos
    input_window = tk.Toplevel()
    input_window.title("Ingresar Código de Estado")

    state_code_label = tk.Label(input_window, text="Código de Estado:")
    state_code_label.grid(row=0, column=0, padx=10, pady=5)
    state_code_entry = tk.Entry(input_window)
    state_code_entry.grid(row=0, column=1, padx=10, pady=5)

    confirm_button = tk.Button(input_window, text="Mostrar Datos", command=lambda: process_input(state_code_entry.get(), input_window))
    confirm_button.grid(row=1, columnspan=2, padx=10, pady=10)

def process_input(state_code, input_window):
    if not state_code:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un código de estado para continuar.")
    else:
        show_covid_data(state_code)
        input_window.destroy()
