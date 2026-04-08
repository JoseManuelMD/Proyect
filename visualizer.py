import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_histogram(ll):
    values = ll.get_values()
    if not values:
        print("Lista vacía")
        return

    max_val = max(values)
    print("\nHistograma:")
    for level in range(max_val, 0, -1):
        line = " ".join("██" if v >= level else "  " for v in values)
        print(line)
    print(" ".join(f"{v:2}" for v in values))
    print()
