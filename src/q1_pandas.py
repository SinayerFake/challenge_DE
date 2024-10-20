import pandas as pd

def q1_time_p(file_path: str):
    # Cargar los datos como un DataFrame
    df = pd.read_json(file_path, lines=True)
    
    # Extraer el campo 'username' del diccionario en la columna 'user'
    df['user'] = df['user'].apply(lambda x: x['username'])
    
    # Convertir la columna 'date' a un formato datetime y extraer solo la fecha (sin la hora)
    df['date'] = pd.to_datetime(df['date']).dt.date

    # Contar tweets por usuario en cada fecha
    date_user_counts = df.groupby(['date', 'user']).size().reset_index(name='counts')

    # Obtener las 10 fechas con más tweets
    top_10_dates = df['date'].value_counts().nlargest(10).index.tolist()

    result = []
    for date in top_10_dates:
        # Encontrar el usuario con más tweets en esa fecha
        most_active_user = date_user_counts[date_user_counts['date'] == date].sort_values(by='counts', ascending=False).iloc[0]['user']
        result.append((date, most_active_user))

    return result





