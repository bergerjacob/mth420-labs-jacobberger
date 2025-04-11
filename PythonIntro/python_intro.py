# python_intro.py
"""Python Essentials: Introduction to Python.
<Name>
<Class>
<Date>
"""


# Problem 1 (write code below)
if __name__ == "__main__":
    print("Hello, world!")


# Problem 2
def sphere_volume(r):
    """ Return the volume of the sphere of radius 'r'.
    Use 3.14159 for pi in your computation.
    """
    return 4/3*3.14159* r**3


# Problem 3
def isolate(a, b, c, d, e):
    """ Print the arguments separated by spaces, but print 5 spaces on either
    side of b.
    """
    print(a, b, c, sep=" "*5, end=" ")
    print(d,e)


# Problem 4
def first_half(my_string):
    """ Return the first half of the string 'my_string'. Exclude the
    middle character if there are an odd number of characters.

    Examples:
        >>> first_half("python")
        'pyt'
        >>> first_half("ipython")
        'ipy'
    """
    return my_string[:len(my_string)//2]

def backward(my_string):
    """ Return the reverse of the string 'my_string'.

    Examples:
        >>> backward("python")
        'nohtyp'
        >>> backward("ipython")
        'nohtypi'
    """
    return my_string[::-1]


# Problem 5
def list_ops():
    """ Define a list with the entries "bear", "ant", "cat", and "dog".
    Perform the following operations on the list:
        - Append "eagle".
        - Replace the entry at index 2 with "fox".
        - Remove (or pop) the entry at index 1.
        - Sort the list in reverse alphabetical order.
        - Replace "eagle" with "hawk".
        - Add the string "hunter" to the last entry in the list.
    Return the resulting list.

    Examples:
        >>> list_ops()
        ['fox', 'hawk', 'dog', 'bearhunter']
    """
    list = ["bear", "ant", "cat", "dog"]
    list.append("eagle")
    list[2] = "fox"
    list.pop(1)
    list.sort(reverse=True)
    list[list.index("eagle")] = "hawk"
    list[-1] += "hunter"

    return list


# Problem 6
def pig_latin(word):
    """ Translate the string 'word' into Pig Latin, and return the new word.

    Examples:
        >>> pig_latin("apple")
        'applehay'
        >>> pig_latin("banana")
        'ananabay'
    """
    vowels = {'a','e','i','o','u'}

    if len(word) == 0:
        return ''
    if word[0] in vowels:
        return word + "hay"
    else:
        return word[1:] + word[0] + "ay"


# Problem 7
def palindrome():
    """ Find and retun the largest panindromic number made from the product
    of two 3-digit numbers.
    """
    best_num = 0

    for num1 in range(100,1000):
        for num2 in range(100,1000):
            prod = num1 * num2
            is_palindrome = str(prod) == str(prod)[::-1]
            is_best = prod > best_num
            if (is_palindrome and is_best):
                best_num = prod
    return best_num

# Problem 8
def alt_harmonic(n):
    """ Return the partial sum of the first n terms of the alternating
    harmonic series, which approximates ln(2).
    """
    list = [(-1)**(i+1) / i for i in range(1, n+1)]
    print(list)
    return sum(list)


if __name__ == "__main__":
    print(sphere_volume(2))
    isolate(1,2,3,4,5)
    print(first_half("python"))
    print(backward("python"))
    print(list_ops())
    print(pig_latin("apple"))
    print(pig_latin("banana"))
    print(pig_latin(""))
    print(palindrome())
    print(alt_harmonic(500000))
