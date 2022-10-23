def main(n,x):
    """
    Given a argument called 'n' and 'x' type of int , calculate the value of expression and return result:
    Args:
        n: int
        x: int
    Returns:
        result : int
    """
    y = x ** n + n ** x
    return y
print(main(3, 6))