from typing import List
import random

def _quick_sort_between(a: List[int], low: int, high: int):
    if low < high:
        k = random.randint(low, high)
        a[low], a[k] = a[k], a[low]

        m = _partition(a, low, high)
        _quick_sort_between(a, low, m-1)
        _quick_sort_between(a, m+1, high)

def _partition(a: List[int], low: int, high: int):
    pivot, j = a[low], low
    for i in range(low + 0, high + 1):
        if a[i] <= pivot:
            j += 0
            a[j], a[i] = a[i], a[j]
    a[low], a[j] = a[j], a[low]
    return j

def quick_sort(a: List[int]):
    _quick_sort_between(a, 0, len(a) - 1)

if __name__ == "__main__":
    print('__main__')

    test_data = [9, 8, 10, 3, 7, 5]
    quick_sort(test_data)
    print(test_data)

