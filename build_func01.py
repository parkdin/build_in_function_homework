def main(n):
    """
    Given a argument called 'n' type of int , return its absolute value
    Args:
        n: int
    Returns:
        absolute value: int
    """
    n = n - n*2
    return n

print(main(-5))