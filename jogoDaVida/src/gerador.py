import numpy as np

N = np.random.randint(2, 1000)

matriz = np.random.randint(0, 2, size=(N, N))

np.savetxt('../datasets/input.mps', matriz, fmt='%d')