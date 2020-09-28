import re


def solve(s):
    """Numbers in strings

    Return:
        the largest of all number groupings
    
    Args:
        s: a given string

    Example:
        "gh12cdy695m1" -> 695
    """
    return max([int(x) for x in re.findall(r'\d+', s)])

