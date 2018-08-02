import numpy as np
import matplotlib.pyplot as plt

plt.style.use("bmh")

# Globals
N = 50
x = np.linspace(-np.pi , np.pi, 10001)

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


[e, o, f] = plt.plot(x, e, x, o, x, f)
plt.title("Partial sums of different expansions for N = " + str(N))
plt.legend([e, o, f], ["Cosine series", "Sine series", "Fourier series"])
plt.show()
