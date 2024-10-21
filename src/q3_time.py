import pandas as pd

def q3_time(file_path: str):
    # Carga los datos
    df = pd.read_json(file_path, lines=True)
    
    # Explode a la columna de usuarios mencionados para descomponer en filas
    df['mentionedUsers'] = df['mentionedUsers'].apply(lambda x: [user['username'] for user in x] if x else [])
    df_exploded = df.explode('mentionedUsers')

    # Cuenta los usuarios más comunes
    mention_counts = df_exploded['mentionedUsers'].value_counts().nlargest(10)

    # Convierte el resultado
    result = list(mention_counts.items())

    return result
