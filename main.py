import numpy as np
import matplotlib.pyplot as plt
import time

s_0 = 2  # starting position
mu = 5  # drift velocity
y_range = 0.1  # y_lim of the plot
var = 10  # variance of diffusion

def solution(s_0, mu, x, t, var=var):
    """
    Free-space solution of the PDE.
    :param s_0: starting position
    :param mu: drift velocity
    :param x: location
    :param t: time
    :param var: variance of diffusion
    :return:
    """
    result = 1/np.sqrt(6.28 * t * var) * np.exp(-(x-mu * t -s_0)**2/(2 * t * var))
    return result


mul_factor = np.exp(-2 * mu * s_0 / var)  # compute the multiplicative factor for the image

x_axis = np.linspace(-20, 20, 2001)

monitor, axes = plt.subplots(2, 1)
axes = axes.ravel()
plt.tight_layout()

for t in np.linspace(0.001, 2, 10):

    update = np.zeros_like(x_axis)
    image = np.zeros_like(update)
    for i in range(len(x_axis)):
        update[i] = solution(s_0, mu, x_axis[i], t)
        image[i] = -mul_factor * solution(-s_0, mu, x_axis[i], t)
    axes[0].clear()
    axes[0].set_xlim(-20, 20)
    axes[0].set_ylim(-y_range, y_range)
    axes[0].plot(x_axis, update, label='original')
    axes[0].plot(x_axis, image, label='image')
    axes[0].text(-10, 0.5 * y_range, 't='+str(t))
    axes[0].legend()

    axes[1].clear()
    axes[1].set_xlim(-20, 20)
    axes[1].set_ylim(-y_range, y_range)
    axes[1].plot(x_axis, update + image)
    axes[1].text(10, 0.5 * y_range, 'p(0)='+str(np.round(update[1000] + image[1000], 20)))
    axes[1].set_title('Image + original')

    monitor.canvas.draw()
    plt.pause(0.01)




