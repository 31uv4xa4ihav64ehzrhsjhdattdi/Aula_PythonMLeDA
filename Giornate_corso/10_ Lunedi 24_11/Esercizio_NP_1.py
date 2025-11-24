import numpy as np

# 1. Usa np.arange per creare un array di numeri interi da 10 a 49
arr = np.arange(10, 50)
print("Array originale:")
print(arr)

# 2. Verifica il tipo di dato (dtype) dell'array
print("\nDtype originale:")
print(arr.dtype)

# 3. Cambia il tipo di dato dell'array in float64
arr_float = arr.astype(np.float64)

print("\nArray convertito in float64:")
print(arr_float)

print("\nNuovo dtype:")
print(arr_float.dtype)

# 4. Stampa la forma (shape) dell'array
print("\nShape dell'array:")
print(arr_float.shape)
