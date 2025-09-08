def insertion_sort(arr):
    for i in range(1, len(arr), 1):
    # TODO: can be optimized with binary search
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break


if __name__ == "__main__":
    inp = [5, 4, 3, 2, 6]
    insertion_sort(inp)
    print(inp)
