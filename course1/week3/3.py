import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sc


def f(x):
    return np.sin(x/5) * np.exp(x/10) + 5 * np.exp(-x/2)

def h(x):
    return int(f(x))

x = np.arange(1, 30, 0.1)
h = np.vectorize(h)
y = h(x)

# 1
res1 = sc.minimize(h, [30], method='bfgs')
#print res1

# 2
res2 = sc.differential_evolution(h, [(1, 30)])
print res2

plt.plot(x, y)
plt.show()
