import tkinter as tk
from tkinter import messagebox
import Acciones_GUI as ac

root = tk.Tk()
root.title("Consulta de datos")

def open_input_window():
    ac.get_input_and_show(root)

# Etiqueta de bienvenida y selección de tipo de dato
welcome_label = tk.Label(root, text="Bienvenido\nSeleccione el tipo de dato a consultar:")
welcome_label.grid(row=0, columnspan=2, padx=10, pady=5)

# Botones para seleccionar el tipo de dato
acciones_button = tk.Button(root, text="Acciones", command=open_input_window)
acciones_button.grid(row=1, column=0, padx=10, pady=5)

redes_sociales_button = tk.Button(root, text="Redes Sociales", state=tk.DISABLED)
redes_sociales_button.grid(row=1, column=1, padx=10, pady=5)

clima_button = tk.Button(root, text="Clima", state=tk.DISABLED)
clima_button.grid(row=2, column=0, padx=10, pady=5)

epidemiologia_button = tk.Button(root, text="Epidemiología", state=tk.DISABLED)
epidemiologia_button.grid(row=2, column=1, padx=10, pady=5)

root.mainloop()
