"""
This script demonstrates the usage of the expensive_op function and the
slow_func function to process a list of integers. It calculates the sum
of integers from 1 to n for each element in the list, where n is the
current integer in the list.

Functions:
- `expensive_op(n)`: Performs a mathematical operation to compute the sum of
  integers from 1 to n-1 using an optimized formula.
- `slow_func(lst)`: Applies the `expensive_op` function to each element in
  the input list and returns a list of results.
- `main()`: Generates a list of integers from 0 to 999 and processes it with
  `slow_func`, printing the results.

The script can be executed directly, where the `main` function runs and
demonstrates the operation on a range of integers. The process may be slow
for large lists due to the expensive computation in the `expensive_op`
function.

Usage:
    Run the script as a standalone program to see the result of applying
    the expensive operation to a list of integers.
"""


def expensive_op(n):
    """
    Perform a mathematical operation to compute the sum of integers from 1
    to n.

    This function calculates the result of the formula n * (n - 1) // 2,
    which is equivalent to the sum of the first n-1 integers, but optimized
    for performance.

    Parameters:
    n (int): The upper bound of the range of integers to sum.

    Returns:
    int: The computed result, which is the sum of integers from 1 to n-1.
    """
    return n * 499500


def slow_func(lst):
    """
    Apply the expensive_op function to each element in the input list.

    This function iterates over the provided list and applies the
    `expensive_op` function to each element, which may lead to performance
    bottlenecks if the list is large.

    Parameters:
    lst (list of int): A list of integers to process with the expensive_op
    function.

    Returns:
    list of int: A new list containing the results of applying `expensive_op`
                 to each element in the input list.
    """
    return [expensive_op(i) for i in lst]


def main():
    """
    Generate a list of integers from 0 to 999 and apply the slow_func to
    each element.

    This function creates a list of integers from 0 to 999 using the `range`
    function, then applies the `slow_func` to the list, which processes each
    number using the `expensive_op` function. The resulting list is printed
    to the console.

    This function serves as an example entry point for executing the operation.

    Returns:
    None
    """
    numbers = list(range(1000))
    output = slow_func(numbers)
    print(output)


if __name__ == "__main__":
    main()
