import copy
import random

from presenter import SinglePresenter

SIZE = 10
PAUSE_SEC = 0.2
IS_DISPLAY = True


def _swap(lst, i, t):
    v = lst[i]
    lst[i] = lst[t]
    lst[t] = v
    return lst


def shaker_sort(l, is_display=True):
    finished = False
    is_reverse = False
    counter = 0
    if is_display:
        presenter = SinglePresenter(SIZE)

    while not finished:
        finished = True
        index_list = []
        if is_reverse:
            index_list = [e + 1 for e in range(len(l) - 1)]
            index_list.reverse()
        else:
            index_list = list(range(len(l) - 1))
        for i in index_list:
            counter += 1
            before = copy.deepcopy(l)
            if is_reverse:
                target = i - 1
                if l[i] < l[target]:
                    l = _swap(l, i, target)
                    finished = False
            else:
                target = i + 1
                if l[i] > l[target]:
                    l = _swap(l, i, target)
                    finished = False
            if is_display:
                presenter.show_swap(
                    index=i,
                    target=target,
                    before_list=before,
                    after_list=l,
                    pause_sec=PAUSE_SEC,
                )
        is_reverse = not is_reverse
    print(counter)


if __name__ == '__main__':
    lst = [e + 1 for e in range(SIZE)]
    random.shuffle(lst)
    shaker_sort(lst, is_display=IS_DISPLAY)
