def main(x,y):
    """
    Given a arguments called 'x' and 'y' type of int , calculate the value of expression and return result:
    Args:
        x: int
        y: int
    Returns:
        result : int
    """
    z = 5 * x ** 2 * y ** 3 + x * y ** 2
    return z

print(main(7,1))