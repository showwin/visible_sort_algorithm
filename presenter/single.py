import copy

import matplotlib.pyplot as plt
import numpy as np


class SinglePresenter:
    def __init__(self, list_size):
        self.size = list_size
        self.x = np.array([e + 1 for e in range(list_size)])
        self.base_color = ['blue'] * list_size

    def show_swap(self, index, target, before_list, after_list, pause_sec):
        y = np.array(before_list)
        colors = copy.deepcopy(self.base_color)
        colors[index] = 'red'
        self._print(y, colors, pause_sec)

        if before_list == after_list:
            return

        # 変化がある場合
        # 入れ替え先を表示
        y = np.array(before_list)
        colors = copy.deepcopy(self.base_color)
        colors[index] = 'red'
        colors[target] = 'green'
        self._print(y, colors, pause_sec)

        # 入れ替えた後を表示
        y = np.array(after_list)
        colors = copy.deepcopy(self.base_color)
        colors[target] = 'red'
        colors[index] = 'green'
        self._print(y, colors, pause_sec)

    def show_compare_and_swap(self, index, target, before_list, after_list, pause_sec):
        y = np.array(before_list)
        colors = copy.deepcopy(self.base_color)

        # 変化がある場合
        # 入れ替え先を表示
        y = np.array(before_list)
        colors = copy.deepcopy(self.base_color)
        colors[index] = 'pink'
        colors[target] = 'pink'
        self._print(y, colors, pause_sec)

        if before_list == after_list:
            return

        y = np.array(before_list)
        colors = copy.deepcopy(self.base_color)
        colors[index] = 'green'
        colors[target] = 'red'
        self._print(y, colors, pause_sec)

        # 入れ替えた後を表示
        y = np.array(after_list)
        colors = copy.deepcopy(self.base_color)
        colors[index] = 'red'
        colors[target] = 'green'
        self._print(y, colors, pause_sec)

    def _print(self, y, colors, pause_sec):
        plt.bar(self.x, y, color=colors)
        plt.pause(pause_sec)
        plt.clf()
