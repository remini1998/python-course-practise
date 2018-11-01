from typing import List

import numpy as np

from lesson_2.decorator import timer


@timer
def bubble_sort(input_list: List[int]):
    input_list = input_list.copy()
    for x in range(input_list.__len__(), 0, -1):
        for y in range(x - 1):
            if input_list[y + 1] < input_list[y]:
                input_list[y + 1], input_list[y] = input_list[y], input_list[y + 1]
    return input_list


@timer
def insert_sort(input_list: List[int]):
    input_list = input_list.copy()
    result = []
    while input_list.__len__() > 0:
        min_index = 0
        for i in range(1, input_list.__len__()):
            if input_list[i] < input_list[min_index]:
                min_index = i
        result.append(input_list[min_index])
        input_list.pop(min_index)
    return result


if __name__ == '__main__':

    array = list(np.random.randint(100, size=1000))

    print("raw array:", array)

    print("bubble result:", bubble_sort(array))
    print("insert result:", insert_sort(array))
