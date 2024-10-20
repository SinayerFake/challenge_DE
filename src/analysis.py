import time
from memory_profiler import memory_usage

def analysis_t_m(func, file_path: str, *args, **kwargs):

    # Medir el tiempo de ejecución
    start_time = time.time()
    
    # Medir el uso de memoria
    mem_usage, result = memory_usage((func, (file_path, *args), kwargs), retval=True)

    end_time = time.time()
    exec_time = end_time - start_time

    print(f"Tiempo de ejecución: {exec_time:.4f} segundos")
    print(f"Uso de memoria máximo: {max(mem_usage):.2f} MB")

    return result

