import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import timedelta
import matplotlib.pyplot as plt

def show_stock_data(api_key, symbol, url, start_date, end_date):
    # Esta función debería ser implementada para obtener los datos de acciones
    # de la API y mostrarlos en la interfaz gráfica.
    # Por ahora, solo mostraremos un cuadro de mensaje con los datos simulados.

    # Obtener todas las fechas dentro del rango
    delta = end_date - start_date
    dates_range = [start_date + timedelta(days=i) for i in range(delta.days + 1)]

    # Datos simulados para el precio de apertura, máximo y mínimo
    data = {
        date.strftime('%Y-%m-%d'): {
            '1. open': float(100 + 5 * (i % 10)),  # Simulando precios de apertura variados
            '2. high': float(105 + 5 * (i % 10)),  # Simulando precios máximos variados
            '3. low': float(98 + 5 * (i % 10)),  # Simulando precios mínimos variados
        }
        for i, date in enumerate(dates_range)
    }

    # Mostrar la gráfica del precio máximo y mínimo
    plt.figure(figsize=(10, 5))
    plt.plot(list(data.keys()), [valores['2. high'] for valores in data.values()], label='Precio máximo', marker='o', linestyle='-')
    plt.plot(list(data.keys()), [valores['3. low'] for valores in data.values()], label='Precio mínimo', marker='o', linestyle='-')
    plt.title('Precios Máximo y Mínimo')
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

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

    start_date_label = tk.Label(input_window, text="Seleccione la fecha de inicio:")
    start_date_label.grid(row=3, column=0, padx=10, pady=5)
    start_cal = DateEntry(input_window, width=12, background='darkblue', foreground='white', borderwidth=2)  # Calendario para seleccionar la fecha de inicio
    start_cal.grid(row=3, column=1, padx=10, pady=5)

    end_date_label = tk.Label(input_window, text="Seleccione la fecha de fin:")
    end_date_label.grid(row=4, column=0, padx=10, pady=5)
    end_cal = DateEntry(input_window, width=12, background='darkblue', foreground='white', borderwidth=2)  # Calendario para seleccionar la fecha de fin
    end_cal.grid(row=4, column=1, padx=10, pady=5)

    confirm_button = tk.Button(input_window, text="Mostrar datos", command=lambda: process_input(api_key_entry.get(), symbol_entry.get(), url_entry.get(), start_cal.get_date(), end_cal.get_date(), input_window))
    confirm_button.grid(row=5, columnspan=2, padx=10, pady=10)

def process_input(api_key, symbol, url, start_date, end_date, input_window):
    if not api_key or not symbol or not url:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos para continuar.")
    else:
        show_stock_data(api_key, symbol, url, start_date, end_date)
        # Una vez que se procesan los datos, cerramos la ventana de diálogo
        input_window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Consulta de datos")

    welcome_label = tk.Label(root, text="Bienvenido\nSeleccione el tipo de dato a consultar:")
    welcome_label.grid(row=0, columnspan=2, padx=10, pady=5)

    acciones_button = tk.Button(root, text="Acciones", command=get_input_and_show)
    acciones_button.grid(row=1, column=0, padx=10, pady=5)

    redes_sociales_button = tk.Button(root, text="Redes Sociales", state=tk.DISABLED)
    redes_sociales_button.grid(row=1, column=1, padx=10, pady=5)

    clima_button = tk.Button(root, text="Clima", state=tk.DISABLED)
    clima_button.grid(row=2, column=0, padx=10, pady=5)

    epidemiologia_button = tk.Button(root, text="Epidemiología", state=tk.DISABLED)
    epidemiologia_button.grid(row=2, column=1, padx=10, pady=5)

    root.mainloop()
