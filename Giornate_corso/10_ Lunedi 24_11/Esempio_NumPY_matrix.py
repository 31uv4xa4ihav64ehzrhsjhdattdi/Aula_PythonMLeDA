import numpy as np

# np.eye è utilizzato per creare una matrice identità, ovvero una matrice quadrata con 1 lungo la diagonale principale e 0 negli altri elementi.
# Matrice identità 3x3
identity_matrix = np.eye(3)
print("Matrice identità 3x3:\n", identity_matrix)

# Matrice identità 4x4 con offset di 1 sulla diagonale
identity_offset = np.eye(4, k=1)
print("Matrice identità 4x4 con offset:\n", identity_offset)


# np.diag è usata per estrarre una diagonale o per creare una matrice diagonale.
# Creazione di una matrice e estrazione della sua diagonale
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
diagonal = np.diag(matrix)
print("Diagonale estratta:", diagonal)


#La funzione np.random.rand genera array di numeri casuali distribuiti uniformemente tra 0 e 1.
#  Array 1D di numeri casuali
random_1d = np.random.rand(5)
print("Array 1D di numeri casuali:", random_1d)

# Array 2D di numeri casuali (3 righe, 2 colonne)
random_2d = np.random.rand(3, 2)
print("Array 2D di numeri casuali:\n", random_2d)
