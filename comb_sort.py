import copy
import random

from presenter import SortPresenter

SIZE = 10
PAUSE_SEC = 0.3
IS_DISPLAY = True


def _swap(lst, i, t):
    v = lst[i]
    lst[i] = lst[t]
    lst[t] = v
    return lst


def comb_sort(l, is_display=True):
    interval = int(SIZE // 1.3)
    counter = 0
    is_swapped = True
    if is_display:
        presenter = SortPresenter(SIZE)

    while not (interval == 1 and not is_swapped):
        is_swapped = False
        for i in range(SIZE - interval):
            counter += 1
            target = i + interval
            if is_display:
                before = copy.deepcopy(l)

            if l[i] > l[target]:
                l = _swap(l, i, target)
                is_swapped = True

            if is_display:
                presenter.show_compare_and_swap(
                    index=i,
                    target=target,
                    before_list=before,
                    after_list=l,
                    pause_sec=PAUSE_SEC,
                )

        if interval > 1:
            interval = int(interval // 1.3)

    print(counter)


if __name__ == '__main__':
    lst = [e + 1 for e in range(SIZE)]
    random.shuffle(lst)
    comb_sort(lst, is_display=IS_DISPLAY)
