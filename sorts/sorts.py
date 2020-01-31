from typing import List

def bubble_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return
    for i in range(length):
        flag = False
        for j in range(length - i -1):
            if a[j] > a[j+1]:
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
                flag = True
        if not flag:
            break

def insertion_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return

    for i in range(1, length):
        value = a[i]
        j = i - 1
        while j >= 0 and a[j] > value:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = value

def selection_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return
    for i in range(length):
        min_index = i
        min_val = a[i]
        for j in range(i, length):
            if a[j] < min_val:
                min_val = a[j]
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]

if __name__ == "__main__":
    test_array = [2, 3, 1, 4, 8, 7, 6]
    bubble_sort(test_array)
    print(test_array)
    test_array = [2, 3, 1, 4, 8, 7, 6]
    insertion_sort(test_array)
    print(test_array)
    test_array = [2, 3, 1, 4, 8, 7, 6]
    selection_sort(test_array)
    print(test_array)
