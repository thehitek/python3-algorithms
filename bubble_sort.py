import random


def bubble_sort(arr: list[int]):


    """Bubble Sort
    Example input:     7 7 6 4 3\n
    On each iteration, swap two adjacent numbers if they are not in the correct order.

    Iteration 1: (7)(7) 6  4  3 -> (7)(7) 6  4  3\n
    Iteration 2:  7 (7)(6) 4  3 ->  7 (6)(7) 4  3\n
    Iteration 3:  7  6 (7)(4) 3 ->  7  6 (4)(7) 3\n

    And so on, until on the next iteration it turns out that all elements are in the correct order.
    """
    is_sorted = False
    arr_len = len(arr)
    counter_iterations = 0

    # Go through N-1 times, because at most each element needs to be moved to another place
    for _ in range(arr_len - 1):
        is_sorted = True
        for i in range(arr_len - 1):
            counter_iterations += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
        if is_sorted:
            print(f"Iterations: {counter_iterations}")
            break

    print(f"Iterations: {counter_iterations}")


if __name__ == "__main__":
    inp = [random.randint(0, i) for i in range(100)]
    bubble_sort(inp)
    print(inp)
