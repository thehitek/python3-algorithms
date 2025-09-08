import random
from utils import swap


def heapify(heap, index, heap_size):
    """heapify down for max-heap"""
    left_child_index = 2 * index + 1
    right_child_index = 2 * index + 2
    largest = index

    if left_child_index < heap_size and heap[left_child_index] > heap[largest]:
        largest = left_child_index

    if right_child_index < heap_size and heap[right_child_index] > heap[largest]:
        largest = right_child_index

    if largest != index:
        swap(heap, index, largest)
        heapify(heap, largest, heap_size)


def heap_sort(arr):
    arr_len = len(arr)
    # Build a binary heap from the array in O(n)
    for i in range((arr_len - 2) // 2, -1, -1):
        heapify(arr, i, arr_len)

    for j in range(1, arr_len - 1):
        # Swap the root of the heap (its maximum) with its last element
        swap(arr, 0, arr_len - j)
        # Restore the heap by applying heapify down to arr[0],
        # thus moving that last element to its correct place,
        # and finding the new root of the heap
        heapify(arr, 0, arr_len - j)
        # Stop condition: arr_len - j >= 2


if __name__ == "__main__":
    inp = [random.randint(-i, i) for i in range(1000000)]
    heap_sort(inp)
    print(inp)
