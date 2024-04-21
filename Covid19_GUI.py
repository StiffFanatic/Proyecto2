import tkinter as tk
from tkinter import messagebox
import DatosCovid19 as dacovid

def show_covid_data_window(data):
    result_window = tk.Toplevel()
    result_window.title("Datos de COVID")

    result_text = tk.Text(result_window, wrap="word", height=20, width=80)
    result_text.pack(padx=10, pady=10)

    result_text.insert(tk.END, f"Estado: {data['state']}\n")
    result_text.insert(tk.END, f"Casos positivos: {data['positive']}\n")
    result_text.insert(tk.END, f"Fallecidos: {data['death']}\n")
    result_text.insert(tk.END, f"Pruebas realizadas: {data['totalTestResults']}\n")

def show_covid_data(api_url, state_code):
    try:
        covid_data = dacovid.get_covid_data(api_url, state_code)
        if covid_data:
            show_covid_data_window(covid_data)
        else:
            messagebox.showerror("Error", "No se pudo obtener la información de COVID.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al obtener datos: {str(e)}")

def open_covid19_window():
    input_window = tk.Toplevel()
    input_window.title("Epidemiología")

    state_code_label = tk.Label(input_window, text="Código de Estado:")
    state_code_label.grid(row=0, column=0, padx=10, pady=5)
    state_code_entry = tk.Entry(input_window)
    state_code_entry.grid(row=0, column=1, padx=10, pady=5)

    confirm_button = tk.Button(input_window, text="Mostrar datos", command=lambda: process_input(state_code_entry.get(), input_window))
    confirm_button.grid(row=1, columnspan=2, padx=10, pady=10)

def process_input(state_code, input_window):
    if not state_code:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un código de estado para continuar.")
    else:
        api_url = "https://api.covidtracking.com"
        show_covid_data(api_url, state_code)
        input_window.destroy()
