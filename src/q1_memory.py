import json
from collections import defaultdict
from datetime import datetime
from typing import List, Tuple

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Carga de datos
    with open(file_path, 'r') as f:
        tweets = [json.loads(line) for line in f]

    # Creación del defaultdict
    date_counter = defaultdict(lambda: defaultdict(int))

    for tweet in tweets:
        tweet_date = datetime.strptime(tweet['date'], "%Y-%m-%dT%H:%M:%S%z").date()
        user = tweet['user']['username']
        date_counter[tweet_date][user] += 1

    # 10 fechas con más tweets
    top_10_dates = sorted(date_counter.keys(), key=lambda d: sum(date_counter[d].values()), reverse=True)[:10]

    # Comprehensive list del resultado:
    result = [(date, max(date_counter[date], key=date_counter[date].get)) for date in top_10_dates]

    return result
