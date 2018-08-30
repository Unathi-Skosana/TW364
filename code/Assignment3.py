from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


def q1_plot():
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
    plt.xlabel(r"\texttt{x}")
    plt.ylabel(r"\texttt{u(x, t)}")
    [a, b, c, d, e, f] = plt.plot(x, f[0], 'r-', x, f[1], 'b-', x, f[2], 'y-', x, f[3], 'm-', x, f[4], 'c-', x, f[5], 'g-')
    plt.legend([a, b, c, d, e, f], [r"$t_0 = 0.0$",r"$t_1= 0.8$", r"$t_2 = 1.6$", r"$t_3 = 2.4$", r"$t_4 = 3.2$", r"$t_5 = 4.0$"], loc="lower right")
    plt.show()

if __name__ == '__main__':
    q1_plot()
