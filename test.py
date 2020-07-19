import matplotlib.pyplot as plt
import numpy as np

left = np.array([1, 2, 3, 4, 5])

fig = plt.figure()

while True:
    ax1 = fig.add_subplot(1, 1, 1)
    height = np.array([100, 500, 400, 300, 200])
    ax1.bar(left, height, color=['blue', 'blue', 'blue', 'blue', 'blue'])
    plt.pause(1)

    ax1 = fig.add_subplot(1, 1, 1)
    height = np.array([100, 500, 400, 300, 200])
    ax1.set_xlabel('showwin2')
    ax1.bar(left, height, color=['blue', 'red', 'red', 'blue', 'blue'])
    plt.pause(1)
    plt.clf()
    height = np.array([100, 400, 500, 300, 200])
    plt.bar(left, height, color=['blue', 'red', 'red', 'blue', 'blue'])
    plt.pause(1)
    plt.clf()
    height = np.array([100, 400, 500, 300, 200])
    plt.bar(left, height, color=['blue', 'blue', 'blue', 'blue', 'blue'])
    plt.pause(1)
    plt.clf()

    ax1.set_title('showwin3')
    height = np.array([100, 400, 500, 300, 200])
    plt.bar(left, height, color=['blue', 'blue', 'red', 'red', 'blue'])
    plt.pause(1)
    plt.clf()
    height = np.array([100, 400, 300, 500, 200])
    plt.bar(left, height, color=['blue', 'blue', 'red', 'red', 'blue'])
    plt.pause(1)
    plt.clf()
    height = np.array([100, 400, 300, 500, 200])
    plt.bar(left, height, color=['blue', 'blue', 'blue', 'blue', 'blue'])
    plt.pause(1)
    plt.clf()

    height = np.array([100, 400, 300, 200, 500])
    plt.bar(left, height, color=['blue', 'blue', 'blue', 'red', 'red'])
    plt.pause(1)
    plt.clf()

    height = np.array([100, 300, 400, 200, 500])
    plt.bar(left, height, color=['blue', 'red', 'red', 'blue', 'blue'])
    plt.pause(1)
    plt.clf()

    height = np.array([100, 300, 200, 400, 500])
    plt.bar(left, height, color=['blue', 'blue', 'red', 'red', 'blue'])
    plt.pause(1)
    plt.clf()

    height = np.array([100, 200, 300, 400, 500])
    plt.bar(left, height, color=['blue', 'red', 'red', 'blue', 'blue'])
    plt.pause(1)
    plt.clf()
