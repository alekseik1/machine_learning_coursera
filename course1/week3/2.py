import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sc


def f(x):
    return np.sin(x/5) * np.exp(x/10) + 5 * np.exp(-x/2)


x = np.arange(1, 30, 0.1)
f = np.vectorize(f)
y = f(x)

res = sc.differential_evolution(f, [(1, 30)])
print res
