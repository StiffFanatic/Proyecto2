import tkinter as tk
from tkinter import messagebox
import DatosAcciones as da  # Importa la función desde el módulo DatosAcciones

def show_stock_data():
    symbol = symbol_entry.get().upper()
    api_key = api_key_entry.get()

    time_series = da.get_stock_data(api_key, symbol)

    if time_series:
        # Crear una nueva ventana para mostrar la información
        result_window = tk.Toplevel(root)
        result_window.title("Datos de acciones")

        # Crear un Text widget para mostrar la información
        result_text = tk.Text(result_window, wrap="word", height=20, width=80)
        result_text.pack(padx=10, pady=10)

        # Mostrar la información en el Text widget
        for fecha, valores in sorted(time_series.items(), reverse=True):  # Ordenar por fecha
            result_text.insert(tk.END, f"Fecha: {fecha}\n")
            result_text.insert(tk.END, f"Precio apertura: {valores['1. open']}\n")
            result_text.insert(tk.END, f"Precio máximo: {valores['2. high']}\n")
            result_text.insert(tk.END, f"Precio mínimo: {valores['3. low']}\n")
            result_text.insert(tk.END, f"Precio de cierre: {valores['4. close']}\n")
            result_text.insert(tk.END, f"Volumen: {valores['5. volume']}\n\n")


root = tk.Tk()
root.title("Consulta de datos de acciones")

# Etiqueta y entrada para la clave API
api_key_label = tk.Label(root, text="Clave API:")
api_key_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
api_key_entry = tk.Entry(root, show="*")
api_key_entry.grid(row=0, column=1, padx=10, pady=5)

# Etiqueta y entrada para el símbolo de la acción
symbol_label = tk.Label(root, text="Símbolo de acción:")
symbol_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
symbol_entry = tk.Entry(root)
symbol_entry.grid(row=1, column=1, padx=10, pady=5)

# Botón para mostrar los datos de las acciones
show_button = tk.Button(root, text="Mostrar datos", command=show_stock_data)
show_button.grid(row=2, columnspan=2, padx=10, pady=10)

root.mainloop()
