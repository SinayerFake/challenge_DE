import pandas as pd

# Solución enfocada en optimización de tiempo con uso de pandas

def q1_time(file_path: str):
    # Carga de datos
    df = pd.read_json(file_path, lines=True)
    
    # Extracción del campo 'username'
    df['user'] = df['user'].apply(lambda x: x['username'])
    
    # Manipulación de la columna 'date'
    df['date'] = pd.to_datetime(df['date']).dt.date

    # Conteo de tweets por usuario por fecha
    date_user_counts = df.groupby(['date', 'user']).size().reset_index(name='counts')

    # 10 fechas con más tweets
    top_10_dates = df['date'].value_counts().nlargest(10).index.tolist()

    result = []
    for date in top_10_dates:
        most_active_user = date_user_counts[date_user_counts['date'] == date].sort_values(by='counts', ascending=False).iloc[0]['user']
        result.append((date, most_active_user))

    return result