import tkinter as tk
import Acciones_GUI as ac
import Covid19_GUI as C19

root = tk.Tk()
root.title("Consulta de datos")

def open_c19_window():
    C19.open_covid19_window()

def open_input_window():
    ac.get_input_and_show(root)

welcome_label = tk.Label(root, text="Bienvenido\nSeleccione el tipo de dato a consultar:")
welcome_label.grid(row=0, columnspan=2, padx=10, pady=5)

acciones_button = tk.Button(root, text="Acciones", command=open_input_window)
acciones_button.grid(row=1, column=0, padx=10, pady=5)

redes_sociales_button = tk.Button(root, text="Redes Sociales", state=tk.DISABLED)
redes_sociales_button.grid(row=1, column=1, padx=10, pady=5)

clima_button = tk.Button(root, text="Clima", state=tk.DISABLED)
clima_button.grid(row=2, column=0, padx=10, pady=5)

epidemiologia_button = tk.Button(root, text="Epidemiología", command=open_c19_window)
epidemiologia_button.grid(row=2, column=1, padx=10, pady=5)

root.mainloop()
