"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)

def f(x):
    return x * 4 + 6

function_values = dict()

sums_to_known_tuples = dict()
differences_to_known_tuples = dict()

for number1 in q:

    if number1 not in function_values:
        function_values[number1] = f(number1)

    for number2 in q:
        
        if number2 not in function_values:
            function_values[number2] = f(number2)

        tuple_1_2 = (number1, number2)
        tuple_2_1 = (number2, number1)

        pair_sum = function_values[number1] + function_values[number2]
        pair_difference = function_values[number1] - function_values[number2]

        if pair_sum not in sums_to_known_tuples:
            sums_to_known_tuples[pair_sum] = set()
        
        sums_to_known_tuples[pair_sum].add(tuple_1_2)
        sums_to_known_tuples[pair_sum].add(tuple_2_1)

        if pair_difference not in differences_to_known_tuples:
            differences_to_known_tuples[pair_difference] = set()

        differences_to_known_tuples[pair_difference].add(tuple_1_2)

        if -pair_difference not in differences_to_known_tuples and number1 != number2:
            differences_to_known_tuples[-pair_difference] = set()

        differences_to_known_tuples[-pair_difference].add(tuple_2_1)

shared_values = set(sums_to_known_tuples.keys()).intersection(set(differences_to_known_tuples.keys()))

def print_solutions(show_all_possibilities=True):

    solutions = 0

    for value in shared_values:

        known_sum_tuples = sums_to_known_tuples[value]
        known_difference_tuples = differences_to_known_tuples[value]

        solutions += len(known_sum_tuples) * len(known_difference_tuples)

        if show_all_possibilities:

            for sum_tuple in known_sum_tuples:

                for difference_tuple in known_difference_tuples:

                    a, b = sum_tuple
                    c, d = difference_tuple

                    print(f"f({a}) + f({b}) = f({c}) - f({d})    {function_values[a]} + {function_values[b]} = {function_values[c]} - {function_values[d]}")

    print("\n\n", solutions, "solutions found for q =", q)

print_solutions()