import numpy as np
import matplotlib.pyplot as plt

plt.style.use("bmh")

# Globals
x_f = np.pi
x_i =  0
x   = np.linspace(x_i ,x_f, 100001)
f = [3.0/4.0] *  6

index = 0
for t in np.arange(0, 4.4, 0.8):
    for n in range(1, 201):
        f[index] -= ((8.0 * np.sin((n*np.pi)/4.00)**2) / (n**2 * np.pi**2)) * np.exp(-(n**2) * t) * np.cos(n*x)
    index += 1

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.title(r"$u_{201}(x,t)$")
plt.xlabel(r"\texttt{length}")
plt.ylabel(r"\texttt{time}")
[a, b, c, d, e, f] = plt.plot(x, f[0], 'r-', x, f[1], 'b-', x, f[2], 'y-', x, f[3], 'm-', x, f[4], 'c-', x, f[5], 'g-')
plt.legend([a, b, c, d, e, f], ["t=0.0","t=0.8", "t=1.6", "t=2.4", "t=3.2", "t=4.0"], loc="lower right")
plt.show()
