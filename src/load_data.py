# Manejo de los datos desde el archivo JSON a una lista.

import os
import json

# Carga el archivo JSON si existe, si no, arroja un error
def f_load_data(file_path):
    if os.path.exists(file_path):
        print(f"Cargando datos desde '{file_path}'...")
        with open(file_path, 'r') as f:
            data = [json.loads(line) for line in f]
        print(f"Datos cargados correctamente.")
        return data
    else:
        print(f"Error: El archivo '{file_path}' no existe en la carpeta 'src'.")
        return None