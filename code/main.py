import numpy as np
import matplotlib.pyplot as plt

plt.style.use("bmh")

# Globals
N   = 200
x_f =  10
x_i =  -x_f
x   = np.linspace(x_i ,x_f, 100001)

e = np.pi**2 / 3
for n in range(1, N):
    an = 4.00 * (-1)**n / n**2
    e = e + an * np.cos(n*x)

o = 0
for n in range(1, N):
    bn = 4.00 * ((-1)**n - 1) / (n**3 * np.pi) - 2 * np.pi*(-1)**n / n
    o = o + bn * np.sin(n*x)

f = np.pi**2 / 3
for n in range(1, N):
    an = (2 + 2*(-1)**n) / n**2
    bn = (np.pi + np.pi*(-1)**n) / n
    f = f + an * np.cos(n*x) - bn * np.sin(n*x)

[f] = plt.plot(x, f)
plt.title("Partial sums of different expansions for N = " + str(N))
plt.legend([f], ["Fourier Series"], loc="lower right")
plt.show()
