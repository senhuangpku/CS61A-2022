def line_stepper(start, k):
    """
    Complete the function line_stepper, which returns the number of ways there are to go from
    start to 0 on the number line by taking exactly k steps along the number line.

    >>> line_stepper(1, 1)
    1
    >>> line_stepper(0, 2)
    2
    >>> line_stepper(-3, 3)
    1
    >>> line_stepper(3, 5)
    5
    """
    "*** YOUR CODE HERE ***"

    def helper(position, steps):
        if steps == 0:
            if position == 0:
                return 1
            else:
                return 0
        else:
            return helper(position + 1, steps - 1) + helper(position - 1, steps - 1)

    return helper(start, k)
