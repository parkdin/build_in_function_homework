def main(x,y):
    """
    Given a arguments called 'x' and 'y' type of int , calculate the value of expression and round the result to 2 decimal places, use the pow function use the round function ,return result:
    Args:
        x: int
        y: int
    Returns:
        result : float
    """
    return 3 * y ** 0.5 + x ** (2/3) 

print(main(8,4))