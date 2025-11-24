import numpy as np

# 1. Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50
# randint(low, high, size) genera numeri in [low, high)
arr = np.random.randint(10, 51, size=20)
print("Array originale:")
print(arr)
print("-" * 40)

# 2. Slicing: primi 10 elementi
primi_10 = arr[:10]
print("Primi 10 elementi (arr[:10]):")
print(primi_10)
print("-" * 40)

# 3. Slicing: ultimi 5 elementi
ultimi_5 = arr[-5:]
print("Ultimi 5 elementi (arr[-5:]):")
print(ultimi_5)
print("-" * 40)

# 4. Slicing: elementi dall'indice 5 all'indice 15 (escluso)
da_5_a_15 = arr[5:15]
print("Elementi da indice 5 a 14 (arr[5:15]):")
print(da_5_a_15)
print("-" * 40)

# 5. Slicing: ogni terzo elemento dell'array
ogni_terzo = arr[::3]
print("Ogni terzo elemento (arr[::3]):")
print(ogni_terzo)
print("-" * 40)

# 6. Modifica tramite slicing gli elementi dall'indice 5 all'indice 10 (escluso)
#    assegnando loro il valore 99
arr[5:10] = 99
print("Array dopo modifica arr[5:10] = 99:")
print(arr)
print("-" * 40)

# 7. Stampa riepilogo di tutti i sotto-array ottenuti tramite slicing
print("Riepilogo sottoarray (attenzione: alcuni sono viste dell'originale):\n")
print("Primi 10 elementi:", primi_10)
print("Ultimi 5 elementi:", ultimi_5)
print("Da indice 5 a 14:", da_5_a_15)
print("Ogni terzo elemento:", ogni_terzo)
