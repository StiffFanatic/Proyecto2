import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar

def show_data_window(data):

    result_window = tk.Toplevel()
    result_window.title("Datos de acciones")

   
    result_text = tk.Text(result_window, wrap="word", height=20, width=80)
    result_text.pack(padx=10, pady=10)

  
    for fecha, valores in sorted(data.items(), reverse=True):  
        result_text.insert(tk.END, f"Fecha: {fecha}\n")
        result_text.insert(tk.END, f"Precio apertura: {valores['1. open']}\n")
        result_text.insert(tk.END, f"Precio máximo: {valores['2. high']}\n")
        result_text.insert(tk.END, f"Precio mínimo: {valores['3. low']}\n")
        result_text.insert(tk.END, f"Precio de cierre: {valores['4. close']}\n")
        result_text.insert(tk.END, f"Volumen: {valores['5. volume']}\n\n")

def show_stock_data(api_key, symbol, url, selected_date):
 
    data = {
        selected_date: {
            '1. open': '100.00',
            '2. high': '105.00',
            '3. low': '98.00',
            '4. close': '102.50',
            '5. volume': '1000000'
        }
    }
    show_data_window(data)

def get_input_and_show(root):
   
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

    date_label = tk.Label(input_window, text="Seleccione la fecha:")
    date_label.grid(row=3, column=0, padx=10, pady=5)
    cal = Calendar(input_window, selectmode='day',
                   year=2024, month=4, day=21)  
    cal.grid(row=3, column=1, padx=10, pady=5)

    confirm_button = tk.Button(input_window, text="Mostrar datos", command=lambda: process_input(api_key_entry.get(), symbol_entry.get(), url_entry.get(), cal.get_date(), input_window))
    confirm_button.grid(row=4, columnspan=2, padx=10, pady=10)

def process_input(api_key, symbol, url, selected_date, input_window):
    if not api_key or not symbol or not url:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos para continuar.")
    else:
        show_stock_data(api_key, symbol, url, selected_date)
    
        input_window.destroy()
