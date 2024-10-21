import pandas as pd
import re
from collections import defaultdict

def q2_memory(file_path: str):
    # Se utilizan chunks para administrar mejor el espacio 
    chunk_size=1000
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
    
    # Creación del defaultdict
    emoji_counter = defaultdict(int)

    # Se lee y procesa el archivo en chunks
    with pd.read_json(file_path, lines=True, chunksize=chunk_size) as reader:
        for chunk in reader:
            chunk['emojis'] = chunk['content'].apply(lambda x: emoji_re.findall(x))
            for emojis in chunk['emojis']:
                for emoji in emojis:
                    emoji_counter[emoji] += 1

    # 10 emojis más comunes
    sorted_emojis = sorted(emoji_counter.items(), key=lambda x: x[1], reverse=True)[:10]

    return sorted_emojis
