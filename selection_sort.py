import random
from utils import swap


def selection_sort(arr: list[int]):
    """Selection sort

    Example: 9 5 3 7 8

    On each iteration, find the minimum element in the array to the "right" and swap it with the current element if it is smaller.

    Iteration 1: (9) 5 "3"  7  8 -> "3" 5 (9)  7  8
    Iteration 2:  3 (5) 9  "7" 8 ->  3 (5) 9  "7" 8
    Iteration 3:  3  5 (9) "7" 8 ->  3  5 "7" (9) 8
    """

    arr_len = len(arr)
    for idx in range(arr_len - 1):
        min_idx_item = idx + 1
        for x in range(idx + 1, arr_len):
            if arr[x] < arr[min_idx_item]:
                min_idx_item = x

        left = arr[idx]
        right = arr[min_idx_item]
        if left > right:
            swap(arr, idx, min_idx_item)


if __name__ == "__main__":
    inp = [random.randint(0, 1000) for _ in range(10**4)]
    selection_sort(inp)
    print(inp)
