from typing import List

import numpy as np

from lesson_2.decorator import timer


@timer
def bubble_sort(input_list: List[int]) -> List[int]:
    input_list = input_list.copy()
    for x in range(input_list.__len__(), 0, -1):
        for y in range(x - 1):
            if input_list[y + 1] < input_list[y]:
                input_list[y + 1], input_list[y] = input_list[y], input_list[y + 1]
    return input_list


@timer
def selection_sort(input_list: List[int]) -> List[int]:
    input_list = input_list.copy()
    for i in range(input_list.__len__()):
        min_index = input_list.index(min(input_list[i:]), i)
        input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
    return input_list


if __name__ == '__main__':
    array = list(np.random.randint(100, size=30000))

    print("raw array:", array)

    print("bubble result:", bubble_sort(array))
    print("selection result:", selection_sort(array))
