def climb_stairs(n: int) -> int:
    """
    Calculate the number of distinct ways to climb n stairs.

    You can climb 1 or 2 steps at a time.

    Args:
        n: Number of stairs

    Returns:
        Number of distinct ways to climb to the top
    """
    prev2, prev1 = 1, 1

    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current

    return prev1