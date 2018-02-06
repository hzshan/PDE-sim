import numpy as np
import matplotlib.pyplot as plt

initial = np.array([-2, -3])
rho = 0
n = 20
t_max = -0.92388


pic, axes = plt.subplots(1, 1)


for t in np.linspace(0, t_max, 10):
    axes.clear()

    update_1 = initial.copy().transpose()
    update_2 = update_1.copy().transpose()
    axes.axvline(0)
    axes.axhline(0)
    axes.scatter(initial[0], initial[1], color='k')
    rho += t_max / 10
    mat_p = np.array([[1, -2 * rho], [0, -1]])
    mat_m = np.array([[-1, 0], [-2 * rho, 1]])

    for i in range(n):

        if i % 2 == 0:
            update_1 = np.matmul(mat_p, update_1)
            update_2 = np.matmul(mat_m, update_2)
        else:
            update_1 = np.matmul(mat_m, update_1)
            update_2 = np.matmul(mat_p, update_2)

        axes.set_xlim(-5, 5)
        axes.set_ylim(-5, 5)
        axes.scatter(update_1[0], update_1[1], color='r')
        axes.scatter(update_2[0], update_2[1], color='b')

    axes.text(1.5, 2, 'rho='+str(np.round(rho, 5)))
    pic.canvas.draw()
    plt.pause(0.01)


