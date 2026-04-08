import random

def generate_random_list(size, min_val=5, max_val=35):
    return [random.randint(min_val, max_val) for _ in range(size)]
