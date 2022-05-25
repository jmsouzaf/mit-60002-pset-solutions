###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

# ================================
# Part B: Golden Eggs
# ================================

# Problem 1
def dp_make_weight(egg_weights, target_weight):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always an egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit

    Returns: int, the smallest number of eggs needed to make target weight
    """
    table = [None for _ in range(target_weight + 1)]
    table[0] = []

    for i in range(target_weight + 1):
        if table[i] is not None:
            for weight in egg_weights:
                if i + weight <= target_weight:
                    new_table = table[i] + [weight]
                    if table[i + weight] is None:
                        table[i + weight] = new_table
                    elif len(new_table) < len(table[i + weight]):
                        table[i + weight] += new_table

    return len(table[target_weight])


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected output: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
