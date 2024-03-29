def sqrt(number: int):
    """
    This function helps to return the squaereroot of a provided number
    input:number(int)
    return:float

    """
    return number ** 2


solution = sqrt(3)
print(solution)


def get_cuberoot(number: int) -> int:
    """
    This function helps to get the cube root of a provided number.

    Args:
        number (int): The number for which the cube root is to be calculated.

    Returns:
        float: The cube root of the provided number.
    """
    # Calculate the cube root using the exponentiation operator (**)
    cube_root = number ** (1 / 3)

    # Return the result
    return cube_root


result = get_cuberoot(8)
print(result)
