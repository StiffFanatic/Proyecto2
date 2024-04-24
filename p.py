import tkinter as tk
import Acciones_GUI as ac
import Covid19_GUI as C19

root = tk.Tk()
root.title("Consulta de datos")

# Funciones para abrir las ventanas correspondientes
def open_c19_window():
    C19.open_covid19_window()

def open_input_window():
    ac.get_input_and_show(root)

# Estilo para la interfaz
fondo = '#FFFFE0'  # Color de fondo
highlight_color = '#98FB98'  # Color botón
highlight_color2 = '#87CEFA'#Color botón 2
font_style = ("slant", 10)  # Estilo de fuente

root.configure(bg=fondo)  
welcome_label = tk.Label(root, text="Bienvenido\nSeleccione el tipo de dato a consultar:", bg=fondo, font=("Arial", 12))
welcome_label.grid(row=0, columnspan=2, padx=10, pady=20)

acciones_button = tk.Button(root, text="Acciones", command=open_input_window, font=font_style, bg=highlight_color)
acciones_button.grid(row=1, column=0, padx=10, pady=10)

epidemiologia_button = tk.Button(root, text="Epidemiología", command=open_c19_window, font=font_style, bg=highlight_color2)
epidemiologia_button.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
