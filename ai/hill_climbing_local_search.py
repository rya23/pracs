import random


def obj_function(x):

    return -((x - 3) ** 2) + 10


def hill_climb(start, step_size, max_iteration):

    current_x = start

    current_value = obj_function(current_x)

    for i in range(max_iteration):

        candidate_x = current_x + random.choice([step_size, -step_size])

        candidate_value = obj_function(candidate_x)

        if candidate_value > current_value:
            current_x = candidate_x
            current_value = candidate_value

        if i % 10 == 0:

            print(f"Iteration {i} current X {current_x} Value of X {candidate_value}")

    return current_x, current_value


start = 0
step_size = 0.1
max_iteration = 100

x, value = hill_climb(start, step_size, max_iteration)

print(f"\nBest solution: x = {x}, value = {value}")
