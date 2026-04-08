from visualizer import clear_screen, print_histogram
import time


def bubble_sort(self, delay):
    moves = 0
    if not self.head or not self.head.next:
        return 0

    swapped = True
    while swapped:
        swapped = False
        current = self.head
        while current.next:
            if current.data > current.next.data:
                current.data, current.next.data = current.next.data, current.data
                swapped = True
                moves += 1

                self.clear()
                print("=== Bubble Sort ===")
                self.print_histogram()
                time.sleep(delay)
            current = current.next
    return moves

def selection_sort(self, delay):
    moves = 0
    n = 0
    current = self.head
    while current:
        n += 1
        current = current.next

    for i in range(n):
        min_idx = i
        current = self.head
        for _ in range(i):
            current = current.next

        min_node = current
        temp = current.next
        j = i + 1
        while temp:
            if temp.data < min_node.data:
                min_node = temp
                min_idx = j
            temp = temp.next
            j += 1

        if min_idx != i:
            # Intercambio
            current = self.head
            for _ in range(i):
                current = current.next
            current.data, min_node.data = min_node.data, current.data
            moves += 1

            self.clear()
            print("=== Selection Sort ===")
            self.print_histogram()
            time.sleep(delay)
    return moves

def insertion_sort(self, delay):
    moves = 0
    if not self.head or not self.head.next:
        return 0

    current = self.head.next
    while current:
        key = current.data
        prev = None
        temp = self.head
        while temp != current and temp.data < key:
            prev = temp
            temp = temp.next

        if temp != current:
            # Mover el nodo (simplificado intercambiando valores)
            current.data = temp.data
            temp.data = key
            moves += 1

            self.clear()
            print("=== Insertion Sort ===")
            self.print_histogram()
            time.sleep(delay)

        current = current.next
    return moves

def merge_sort(self, delay):
    # Versión simplificada que ordena intercambiando valores para visualización
    values = self.get_values()
    moves = self._merge_sort_helper(values, 0, len(values) - 1, delay)
    # Aplicar valores ordenados a la lista
    current = self.head
    for val in values:
        current.data = val
        current = current.next
    return moves

def _merge_sort_helper(self, arr, left, right, delay):
    moves = 0
    if left >= right:
        return 0

    mid = (left + right) // 2
    moves += self._merge_sort_helper(arr, left, mid, delay)
    moves += self._merge_sort_helper(arr, mid + 1, right, delay)
    moves += self._merge(arr, left, mid, right, delay)
    return moves

def _merge(self, arr, left, mid, right, delay):
    moves = 0
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        moves += 1
        self.clear()
        print("=== Merge Sort ===")
        print("Lista actual:", arr)
        self.print_histogram_from_list(arr)
        time.sleep(delay)
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        moves += 1
        self.clear()
        print("=== Merge Sort ===")
        print("Lista actual:", arr)
        self.print_histogram_from_list(arr)
        time.sleep(delay)
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        moves += 1
        self.clear()
        print("=== Merge Sort ===")
        print("Lista actual:", arr)
        self.print_histogram_from_list(arr)
        time.sleep(delay)
        j += 1
        k += 1
    return moves

def print_histogram_from_list(self, values):
    if not values:
        return
    max_val = max(values)
    for level in range(max_val, 0, -1):
        line = ""
        for val in values:
            line += "██ " if val >= level else "   "
        print(line)
    print(" ".join(f"{v:2}" for v in values))
    print()

def quick_sort(self, delay):
    values = self.get_values()
    moves = self._quick_sort_helper(values, 0, len(values) - 1, delay)
    current = self.head
    for val in values:
        current.data = val
        current = current.next
    return moves

def _quick_sort_helper(self, arr, low, high, delay):
    moves = 0
    if low < high:
        pi, m = self._partition(arr, low, high, delay)
        moves += m
        moves += self._quick_sort_helper(arr, low, pi - 1, delay)
        moves += self._quick_sort_helper(arr, pi + 1, high, delay)
    return moves

def _partition(self, arr, low, high, delay):
    moves = 0
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            moves += 1
            self.clear()
            print("=== Quick Sort ===")
            print("Lista actual:", arr)
            self.print_histogram_from_list(arr)
            time.sleep(delay)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    moves += 1
    self.clear()
    print("=== Quick Sort ===")
    print("Lista actual:", arr)
    self.print_histogram_from_list(arr)
    time.sleep(delay)
    return i + 1, moves
