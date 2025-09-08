import random


def merge_two_sorted_arrays(arr1, arr2):
    """
    Merging two sorted arrays
    Example:
        inp1 = [1, 4, 8]
        inp2 = [2, 3, 5, 6]

    Algorithm: Place a pointer at the zero index of each array, and sequentially compare the elements at these indices. If one element is greater, move its pointer one step to the right.
    """

    arr1_len = len(arr1)
    arr2_len = len(arr2)
    result_sorted_array = [None] * (arr1_len + arr2_len)

    left = 0
    right = 0

    cnt = 0
    while left < arr1_len and right < arr2_len:
        arr1_left_val = arr1[left]
        arr2_right_val = arr2[right]

        if arr1_left_val < arr2_right_val:
            result_sorted_array[cnt] = arr1_left_val
            left += 1
        else:
            result_sorted_array[cnt] = arr2_right_val
            right += 1

        cnt += 1

    if left >= arr1_len:
        for i in range(arr2_len - right):
            result_sorted_array[i + left + right] = arr2[i + right]
    elif right >= arr2_len:
        for j in range(arr1_len - left):
            result_sorted_array[j + left + right] = arr1[j + left]

    return result_sorted_array


def merge_sort(arr):
    center = len(arr) // 2
    arr_left = arr[center:]
    arr_right = arr[:center]

    if len(arr_left) > 1:
        arr_left = merge_sort(arr_left)
    if len(arr_right) > 1:
        arr_right = merge_sort(arr_right)

    return merge_two_sorted_arrays(arr_left, arr_right)


if __name__ == "__main__":
    inp = [random.randint(0, i) for i in range(1000000)]
    print(merge_sort(inp))
