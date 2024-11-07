import numpy as np

def DCT(x):
    N = len(x)
    X = np.zeros(N)

    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.cos(np.pi * (n + 0.5) * k / N)

        if k == 0:
            X[k] *= 1 / np.sqrt(N)
        else:
            X[k] *= np.sqrt(2 / N)

    return X

