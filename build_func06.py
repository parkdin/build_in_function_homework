def main(a):
    """
    Given a argument called 'a' type of int , round the result to 2 decimal places return result:
    Args:
        a: float
    Returns:
        result : float
    """
    a = round(a, 2)
    return a

print(main(3.456))