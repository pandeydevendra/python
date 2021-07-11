import matplotlib.pyplot as plt
from random_walk import RandomWalk
import ipdb

# Keep making new walks, as long as the program is active.
print("l1")
while True:
    print("l11")
    # Make a random walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()
    print("l2")
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none', s=1)
    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    print("l3")
    plt.show()
    print("l4")
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

# 
