from matplotlib import animation
import algorithms as ag
import random
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


array = list(range(1, 301))
check = array.copy()
random.shuffle(array)
x = [i for i in range(1, len(array)+1)]

generator = ag.selection_sort(array)

fig, ax = plt.subplots(figsize=(15, 8.43))
ax.set_title('test')
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('auto')

bar = ax.bar(x, array, width=0.7, align='edge', color='green')
iteration = [0]


def update_fig(arr, rects, iteration_arr):
    for rect, y in zip(rects, array):
        rect.set_height(y)
    iteration_arr[0] += 1
    if arr == check:
        plt.pause(1)
        plt.close(fig)


ani = animation.FuncAnimation(fig,
                              update_fig,
                              fargs=(bar, iteration),
                              # blit=False,
                              frames=generator,
                              interval=1,
                              repeat=False,
                              )
plt.gca().set_position([0, 0, 1, 0.95])
plt.show()
