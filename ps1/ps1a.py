###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time


# ================================
# Part A: Transporting Space Cows
# ================================


# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cows = {}

    with open(filename) as cow_data:
        for line in cow_data.readlines():
            cow_name = line.split(",")[0]
            weight = int(line.split(",")[1])
            cows[cow_name] = weight

    return cows


# Problem 2
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    trips = [[]]
    sorted_cows = sorted(cows, key=cows.get, reverse=True)
    remaining_cows = list(cows.keys())

    while len(remaining_cows) > 0:
        for cow in sorted_cows:
            total_weight = sum([cows[cow] for cow in trips[-1]])
            cow_weight = cows[cow]

            if total_weight + cow_weight <= limit and cow in remaining_cows:
                trips[-1].append(cow)
                remaining_cows.remove(cow)

        trips.append([])

    trips.remove([])
    return trips


# Problem 3
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    all_cows = list(cows.keys())
    all_combinations = []
    valid_combinations = []

    for partition in get_partitions(all_cows):
        all_combinations.append(partition)

    for combination in all_combinations:
        is_valid = True

        for trip in combination:
            if sum([cows[cow] for cow in trip]) > limit:
                is_valid = False
                break

        if is_valid:
            valid_combinations.append(combination)

    return sorted(valid_combinations, key=len)[0]


# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # Load cows:
    cows = load_cows("ps1_cow_data.txt")

    # Greedy:
    t0 = time.time_ns()
    print("For greedy, number of trips:", len(greedy_cow_transport(cows)))
    print("Run time:", (time.time_ns() - t0) / 10 ** 9, "seconds")

    print()

    # Brute force:
    t0 = time.time_ns()
    print("For brute force, number of trips:", len(brute_force_cow_transport(cows)))
    print("Run time:", (time.time_ns() - t0) / 10 ** 9, "seconds")


compare_cow_transport_algorithms()
