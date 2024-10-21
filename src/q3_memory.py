import pandas as pd
from collections import defaultdict

def q3_memory(file_path: str, chunk_size=1000):
    # Crea el defaultdict
    mention_counter = defaultdict(int)

    # Procesa el archivo en chunks
    with pd.read_json(file_path, lines=True, chunksize=chunk_size) as reader:
        for chunk in reader:
            # Extraer los nombres de usuario
            chunk['mentionedUsers'] = chunk['mentionedUsers'].apply(lambda x: [user['username'] for user in x] if x else [])
            
            for mentioned in chunk['mentionedUsers']:
                for user in mentioned:
                    mention_counter[user] += 1

    # 10 usuarios más mencionados
    sorted_mentions = sorted(mention_counter.items(), key=lambda x: x[1], reverse=True)[:10]

    return sorted_mentions
