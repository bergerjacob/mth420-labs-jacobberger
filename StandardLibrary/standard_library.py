# standard_library.py
"""Python Essentials: The Standard Library.
<Name>
<Class>
<Date>
"""

from math import sqrt

import calculator

import itertools


# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order, separated by a comma).
    """
    return min(L), max(L), sum(L)/len(L)


# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test integers, strings, lists, tuples, and sets. Print your results.
    """
    results = {}

    print("--- Testing Mutability ---")

    # 1. Test Integer (int)
    print("\nTesting int:")
    name1_int = 5          # Step 1: Create object and assign name
    name2_int = name1_int  # Step 2: Assign new name to first name
    print(f"Before modification: name1_int = {name1_int}, name2_int = {name2_int}")
    print(f"id(name1_int): {id(name1_int)}, id(name2_int): {id(name2_int)}") # Show they point to the same object initially

    name1_int += 1         # Step 3: Alter object via one name
    print(f"After modification:  name1_int = {name1_int}, name2_int = {name2_int}")
    print(f"id(name1_int): {id(name1_int)}, id(name2_int): {id(name2_int)}") # Show name1 now points to a new object

    results['int'] = 'Immutable' if name1_int != name2_int else 'Mutable' # Step 4: Check equality
    print(f"Conclusion for int: {results['int']} (name1_int == name2_int is {name1_int == name2_int})")

    # 2. Test String 
    print("\nTesting str:")
    name1_str = "hello"    # Step 1
    name2_str = name1_str  # Step 2
    print(f"Before modification: name1_str = '{name1_str}', name2_str = '{name2_str}'")
    print(f"id(name1_str): {id(name1_str)}, id(name2_str): {id(name2_str)}")

    name1_str += " world"  # Step 3
    print(f"After modification:  name1_str = '{name1_str}', name2_str = '{name2_str}'")
    print(f"id(name1_str): {id(name1_str)}, id(name2_str): {id(name2_str)}")

    results['str'] = 'Immutable' if name1_str != name2_str else 'Mutable' # Step 4
    print(f"Conclusion for str: {results['str']} (name1_str == name2_str is {name1_str == name2_str})")

    # 3. Test List (list)
    print("\nTesting list:")
    name1_list = [1, 2, 3] # Step 1
    name2_list = name1_list # Step 2
    print(f"Before modification: name1_list = {name1_list}, name2_list = {name2_list}")
    print(f"id(name1_list): {id(name1_list)}, id(name2_list): {id(name2_list)}")

    name1_list.append(4)   # Step 3: Use a method that modifies in-place
    print(f"After modification:  name1_list = {name1_list}, name2_list = {name2_list}")
    print(f"id(name1_list): {id(name1_list)}, id(name2_list): {id(name2_list)}") # IDs remain the same

    results['list'] = 'Mutable' if name1_list == name2_list else 'Immutable' # Step 4
    print(f"Conclusion for list: {results['list']} (name1_list == name2_list is {name1_list == name2_list})")

    # 4. Test Tuple (tuple)
    print("\nTesting tuple:")
    name1_tuple = (1, 2, 3) # Step 1
    name2_tuple = name1_tuple # Step 2
    print(f"Before modification: name1_tuple = {name1_tuple}, name2_tuple = {name2_tuple}")
    print(f"id(name1_tuple): {id(name1_tuple)}, id(name2_tuple): {id(name2_tuple)}")

    name1_tuple += (4,)     # Step 3: Use += as specified
    print(f"After modification:  name1_tuple = {name1_tuple}, name2_tuple = {name2_tuple}")
    print(f"id(name1_tuple): {id(name1_tuple)}, id(name2_tuple): {id(name2_tuple)}") # name1 points to a new object

    results['tuple'] = 'Immutable' if name1_tuple != name2_tuple else 'Mutable' # Step 4
    print(f"Conclusion for tuple: {results['tuple']} (name1_tuple == name2_tuple is {name1_tuple == name2_tuple})")

    # 5. Test Set (set)
    print("\nTesting set:")
    name1_set = {1, 2, 3}  # Step 1
    name2_set = name1_set  # Step 2
    print(f"Before modification: name1_set = {name1_set}, name2_set = {name2_set}")
    print(f"id(name1_set): {id(name1_set)}, id(name2_set): {id(name2_set)}")

    name1_set.add(4)       # Step 3: Use a method that modifies in-place
    print(f"After modification:  name1_set = {name1_set}, name2_set = {name2_set}")
    print(f"id(name1_set): {id(name1_set)}, id(name2_set): {id(name2_set)}") # IDs remain the same

    results['set'] = 'Mutable' if name1_set == name2_set else 'Immutable' # Step 4
    print(f"Conclusion for set: {results['set']} (name1_set == name2_set is {name1_set == name2_set})")


    # Final Conclusion Statement
    print("\n--- Final Conclusions ---")
    mutable_types = [k for k, v in results.items() if v == 'Mutable']
    immutable_types = [k for k, v in results.items() if v == 'Immutable']

    print(f"Mutable object types tested: {', '.join(mutable_types)}")
    print(f"Immutable object types tested: {', '.join(immutable_types)}")
    print("\nExplanation: When an object is mutated (changed in-place), all names referring to it reflect the change.")
    print("When an operation on an immutable object appears to change it, it actually creates a new object,")
    print("and only the name used in the operation is reassigned to the new object.")



# Problem 3
def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than sum(), product() and sqrt() that are
    imported from your 'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    a_squared = calculator.product(a, a)

    b_squared = calculator.product(b, b)

    sum_of_squares = calculator.sum(a_squared, b_squared)

    hypotenuse = calculator.sqrt(sum_of_squares)

    return hypotenuse


# Problem 4
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    elements = list(A)
    n = len(elements)

    subset_tuples = itertools.chain.from_iterable(
        itertools.combinations(elements, r) for r in range(n + 1)
    )

    power_set_list_of_sets = [set(subset) for subset in subset_tuples]

    return power_set_list_of_sets


# # Problem 5: Implement shut the box.
# def shut_the_box(player, timelimit):
#     """Play a single game of shut the box."""
#     raise NotImplementedError("Problem 5 Incomplete")

if __name__ == "__main__":
    print(prob1([1,2,3]))
    prob2()
    print(hypot(3,4))

    test_input = [1, 2]
    result = power_set(test_input)
    print(f"Power set of {test_input}: {result}")
