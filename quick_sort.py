import random


def quick_sort(arr):
    len_arr = len(arr)
    if len_arr <= 1:
        return arr
    # procedure for choosing the pivot element
    pivot = arr[random.randint(0, len_arr) - 1]

    less = []
    equal = []
    more = []

    for item in arr:
        if item < pivot:
            less.append(item)
        elif item > pivot:
            more.append(item)
        else:  # item == pivot
            equal.append(item)

    return quick_sort(less) + equal + quick_sort(more)


if __name__ == "__main__":
    inp = [random.randint(0, i) for i in range(1000000)]
    print(quick_sort(inp))
