import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sc


def f(x):
    return np.sin(x/5) * np.exp(x/10) + 5 * np.exp(-x/2)


x = np.arange(1, 30, 0.1)
f = np.vectorize(f)
y = f(x)

# 1 variant
res1 = sc.minimize(f, [26])
#print res1

# 2 variant
res2 = sc.minimize(f, [2], method='bfgs')
#print res2

# 3 variant
res3 = sc.minimize(f, [30], method='bfgs')
plt.plot(x, y, 'g', res2.x, res2.fun, 'rs', res3.x, res3.fun, 'bs')
plt.show()
