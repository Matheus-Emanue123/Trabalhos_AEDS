import numpy as np

N = np.random.randint(2, 10)

matriz = np.random.randint(0, 3, size=(N, N))

matriz[matriz == 2] = 1

np.savetxt('../datasets/input.mps', matriz, fmt='%d')