import tkinter as tk
from tkinter import messagebox
import DatosAcciones as da

def show_data_window(data):
    # Función para mostrar la ventana de datos con la información obtenida
    result_window = tk.Toplevel()
    result_window.title("Datos de acciones")

    # Crear un Text widget para mostrar la información
    result_text = tk.Text(result_window, wrap="word", height=20, width=80)
    result_text.pack(padx=10, pady=10)

    # Mostrar la información en el Text widget
    for fecha, valores in sorted(data.items(), reverse=True):  # Ordenar por fecha
        result_text.insert(tk.END, f"Fecha: {fecha}\n")
        result_text.insert(tk.END, f"Precio apertura: {valores['1. open']}\n")
        result_text.insert(tk.END, f"Precio máximo: {valores['2. high']}\n")
        result_text.insert(tk.END, f"Precio mínimo: {valores['3. low']}\n")
        result_text.insert(tk.END, f"Precio de cierre: {valores['4. close']}\n")
        result_text.insert(tk.END, f"Volumen: {valores['5. volume']}\n\n")

def show_stock_data(api_key, symbol, url):
    try:
        time_series = da.get_stock_data(api_key, symbol, url)
        
        if time_series:
            # Mostrar la ventana de datos con la información obtenida
            show_data_window(time_series)
        else:
            # Mostrar un mensaje de error si no se pudo obtener la información
            messagebox.showerror("Error", "No se pudo obtener la información de acciones.")
    except Exception as e:
        # Mostrar mensaje de error en caso de excepción
        messagebox.showerror("Error", f"Error al obtener datos: {str(e)}")

def get_input_and_show(root):
    # Función para obtener los datos de entrada y mostrar la ventana de datos
    input_window = tk.Toplevel(root)
    input_window.title("Ingrese los parámetros")

    api_key_label = tk.Label(input_window, text="Clave API:")
    api_key_label.grid(row=0, column=0, padx=10, pady=5)
    api_key_entry = tk.Entry(input_window, show="*")
    api_key_entry.grid(row=0, column=1, padx=10, pady=5)

    symbol_label = tk.Label(input_window, text="Símbolo de acción:")
    symbol_label.grid(row=1, column=0, padx=10, pady=5)
    symbol_entry = tk.Entry(input_window)
    symbol_entry.grid(row=1, column=1, padx=10, pady=5)

    url_label = tk.Label(input_window, text="URL API:")
    url_label.grid(row=2, column=0, padx=10, pady=5)
    url_entry = tk.Entry(input_window)
    url_entry.grid(row=2, column=1, padx=10, pady=5)

    confirm_button = tk.Button(input_window, text="Mostrar datos", command=lambda: process_input(api_key_entry.get(), symbol_entry.get(), url_entry.get(), input_window))
    confirm_button.grid(row=3, columnspan=2, padx=10, pady=10)

def process_input(api_key, symbol, url, input_window):
    if not api_key or not symbol or not url:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos para continuar.")
    else:
        show_stock_data(api_key, symbol, url)
        # Una vez que se procesan los datos, cerramos la ventana de diálogo
        input_window.destroy()

