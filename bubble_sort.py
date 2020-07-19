import copy
import random

from presenter import SinglePresenter

SIZE = 10
PAUSE_SEC = 0.2
IS_DISPLAY = True


def bubble_sort(l, is_display=True):
    finished = False
    counter = 0
    if is_display:
        presenter = SinglePresenter(SIZE)
    while not finished:
        finished = True
        for i in range(len(l) - 1):
            counter += 1
            before = copy.deepcopy(l)
            if l[i] > l[i + 1]:
                t = l[i]
                l[i] = l[i + 1]
                l[i + 1] = t
                finished = False
            if is_display:
                presenter.show(
                    index=i,
                    target=i + 1,
                    before_list=before,
                    after_list=l,
                    pause_sec=PAUSE_SEC,
                )
    print(counter)


if __name__ == '__main__':
    lst = [e + 1 for e in range(SIZE)]
    random.shuffle(lst)
    bubble_sort(lst, is_display=IS_DISPLAY)
