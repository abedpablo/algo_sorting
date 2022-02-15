from matplotlib import animation
import algorithms as ag
import random
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


graphs = {'Selection Sort': {'n': 126,
                             'function': ag.selection_sort},
          'Insertion Sort': {'n': 126,
                             'function': ag.insertion_sort},
          'Quick Sort': {'n': 126,
                         'function': ag.quick_sort},
          'Merge Sort': {'n': 129,
                         'function': ag.merge_sort},
          'Heap Sort': {'n': 201,
                        'function': ag.heap_sort},
          'Radix Sort (LSD)': {'n': 201,
                               'function': ag.radix_sort_l},
          'Radix Sort (MSD)': {'n': 301,
                               'function': ag.radix_sort_m},
          'Shell Sort': {'n': 129,
                         'function': ag.shell_sort},
          'Bubble Sort': {'n': 51,
                          'function': ag.bubble_sort},
          'Cocktail Sort': {'n': 201,
                            'function': ag.cocktail_sort},
          'Gnome Sort': {'n': 51,
                         'function': ag.gnome_sort},
          'Bitonic Sort': {'n': 129,
                           'function': ag.bitonic_sort},
          'Bogo Sort': {'n': 126,
                        'function': ag.bogo_sort}}

for algo, params in graphs.items():
    params = graphs[algo]
    n = params['n']

    array = list(range(1, n))
    check = array.copy()
    random.shuffle(array)
    x = [i for i in range(1, len(array)+1)]

    generator = params['function'](array)

    fig, ax = plt.subplots(figsize=(15, 8.43))
    ax.set_title(algo)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('auto')

    bars = ax.bar(x, array, width=0.7, align='edge', color='green')
    iteration = [0]


    def update_fig(arr, rects, iteration_arr):
        for rect, y in zip(rects, array):
            rect.set_height(y)
        iteration_arr[0] += 1
        if arr == check:
            plt.pause(1)
            ax.cla()
            plt.close(fig)


    ani = animation.FuncAnimation(fig,
                                  update_fig,
                                  fargs=(bars, iteration),
                                  frames=generator,
                                  interval=1,
                                  repeat=False,
                                  save_count=1500
                                  )

    plt.gca().set_position([0, 0, 1, 0.95])
    plt.show()
