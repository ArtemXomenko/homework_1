import random

def get_numbers_ticket(min_val, max_val, quantity):

    if not (1 <= min_val <= max_val <= 1000):
        return []
    if quantity > (max_val - min_val + 1):
        return []

    numbers = random.sample(range(min_val, max_val + 1), quantity)
    return sorted(numbers)
