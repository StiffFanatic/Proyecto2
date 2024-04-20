# main.py
import datosclima as dc

def main():
    simbolo = 'GOOG'
    lon = '1.0'  # Puedes modificar estos valores según sea necesario
    time = '2024-04-19'  # Puedes modificar estos valores según sea necesario
    dc.obtener_datos(simbolo, lon, time)

if __name__ == "__main__":
    main()
