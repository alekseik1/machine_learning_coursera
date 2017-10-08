import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as sc


def f(x):
    return np.sin(x/5) * np.exp(x/10) + 5 * np.exp(-x/2)


n = 3
fin = 15.
df = 1./n
#x = np.arange(1., fin+df, (fin-1.)/n)
x = [1., 4., 10., 15.]
#print x

f = np.vectorize(f)
x_all = np.arange(1, fin, 0.1)
y = f(x_all)

A = np.array([[np.power(i, k) for k in np.arange(n+1)] for i in x])
B = np.array(f(x))
B = np.reshape(B, (len(B), 1))
#print A
#print B
#print f(1), f(4), f(10), f(15)
w = sc.solve(A, B)
print w


def f_a(x):
    res = 0
    for i in range(len(w)):
        res += w[i] * x**i
    return res


f_a = np.vectorize(f_a)
plt.plot(x_all, y, 'g--', x_all, f_a(x_all))
plt.show()
