import copy
import random

from presenter import SinglePresenter

SIZE = 10
PAUSE_SEC = 0.3
IS_DISPLAY = True


def _swap(lst, i, t):
    v = lst[i]
    lst[i] = lst[t]
    lst[t] = v
    return lst


def insertion_sort(l, is_display=True):
    counter = 0
    if is_display:
        presenter = SinglePresenter(SIZE)

    for i in range(SIZE):
        idx = i
        for j in range(i):
            target = i - j - 1
            is_swapped = False
            counter += 1

            if is_display:
                before = copy.deepcopy(l)

            if l[target] > l[idx]:
                l = _swap(l, idx, target)
                is_swapped = True

            if is_display:
                presenter.show_swap(
                    index=idx,
                    target=target,
                    before_list=before,
                    after_list=l,
                    pause_sec=PAUSE_SEC,
                )

            if not is_swapped:
                break

            idx -= 1

    print(counter)


if __name__ == '__main__':
    lst = [e + 1 for e in range(SIZE)]
    random.shuffle(lst)
    insertion_sort(lst, is_display=IS_DISPLAY)
