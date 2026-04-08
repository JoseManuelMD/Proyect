from visualizer import clear_screen, print_histogram
import time


def bubble_sort(ll, delay):
    moves = 0
    if not ll.head or not ll.head.next:
        return 0

    swapped = True
    while swapped:
        swapped = False
        current = ll.head
        while current.next:
            if current.data > current.next.data:
                current.data, current.next.data = current.next.data, current.data
                swapped = True
                moves += 1
                clear_screen()
                print("=== Bubble Sort ===")
                print_histogram(ll)
                time.sleep(delay)
            current = current.next
    return moves
