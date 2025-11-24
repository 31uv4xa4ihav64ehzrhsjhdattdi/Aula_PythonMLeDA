import numpy as np

# Array di esempio
arr = np.array([10, 20, 30, 40, 50, 60, 70])

print("Array originale:", arr)

# Slicing: arr[start:stop]
print("\nElementi dal 2° al 5° elemento (indice 1→4):")
print(arr[1:5])   # 20, 30, 40, 50

# Slicing con step
print("\nElementi ogni 2 posizioni:")
print(arr[0:7:2])  # 10, 30, 50, 70

# Slicing negativo
print("\nUltimi 3 elementi:")
print(arr[-3:])    # 50, 60, 70


# Array di esempio
arr = np.array([100, 200, 300, 400, 500, 600, 700])

print("Array originale:", arr)

# Fancy indexing: selezione di indici specifici
print("\nElementi negli indici [0, 3, 5]:")
print(arr[[0, 3, 5]])   # 100, 400, 600

# Fancy indexing con array booleano
maschera = np.array([True, False, True, False, True, False, False])

print("\nElementi selezionati tramite maschera booleana:")
print(arr[maschera])  # 100, 300, 500
