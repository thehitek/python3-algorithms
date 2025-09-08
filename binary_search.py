def binary_search(arr, item) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (right + left) // 2

        if arr[mid] == item:
            return mid
        if arr[mid] < item:
            left = mid + 1
        if arr[mid] > item:
            right = mid - 1

    return -1


"""
idx = 0. 1. 2. 3. 4. 5.
arr = 11 12 13 15 16 17
item = 17


left = 0
right = 5
mid = 5 - 0 // 2 = 2.5 = 2

arr[mid] = 13
17 > 13 -> left = 3

left = 3
right = 5
mid = 5 + 3 // 2 = 4

arr[mid] = 16
17 > 16 -> left = 5

left = 5
right = 5
mid = left + right // 2 = 5


"""

if __name__ == "__main__":
    inp = [11, 12, 13, 15, 16, 17]
    assert binary_search(inp, 14) == -1
    assert binary_search(inp, 17) == 5
