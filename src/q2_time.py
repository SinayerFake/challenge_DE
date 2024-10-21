import pandas as pd
import re

def q2_time(file_path: str):
    # Cargar los datos
    df = pd.read_json(file_path, lines=True)
    
    # Se utilizan expresiones regulares para encontrar emojis    
    emoji_re = re.compile(
        "["                               
        "\U0001F600-\U0001F64F"  # Emojis
        "\U0001F300-\U0001F5FF"  # Símbolos
        "\U0001F680-\U0001F6FF"  # Transporte y símbolos
        "\U0001F1E0-\U0001F1FF"  # Banderas
        "\U00002702-\U000027B0"  # Otros símbolos
        "\U000024C2-\U0001F251"  # Símbolos adicionales
        "]", flags=re.UNICODE
    )
    
    # Solo emojis
    df['emojis'] = df['content'].apply(lambda x: emoji_re.findall(x))
    
    # Genera una sola lista de emojis
    all_emojis = [emoji for sublist in df['emojis'] for emoji in sublist]
    
    # Cuenta los emojis más comunes
    emoji_counts = pd.Series(all_emojis).value_counts().nlargest(10)

    result = list(emoji_counts.items())

    return result