def daily_temperatures(temperatures: list[int]) -> list[int]:
    """
    Return the number of days until a warmer temperature for each day.

    Args:
        temperatures: A list of daily temperatures.

    Returns:
        A list containing the number of days to wait for a warmer
        temperature. Returns 0 when no warmer day exists.
    """
    result = [0] * len(temperatures)

    for i in range(len(temperatures)):
        for j in range(i + 1, len(temperatures)):
            if temperatures[j] > temperatures[i]:
                result[i] = j - i
                break

    return result


def daily_temperatures_optimized(temperatures: list[int]) -> list[int]:
    """
    Return the number of days until a warmer temperature using a stack.

    Args:
        temperatures: A list of daily temperatures.

    Returns:
        A list containing the number of days to wait for a warmer
        temperature. Returns 0 when no warmer day exists.
    """
    result = [0] * len(temperatures)
    stack = []

    for i in range(len(temperatures) - 1, -1, -1):
        while stack and temperatures[stack[-1]] <= temperatures[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1] - i

        stack.append(i)

    return result


def main():
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

    print(
        "Daily Temperatures (Brute Force):",
        daily_temperatures(temperatures),
    )
    print(
        "Daily Temperatures (Optimized):",
        daily_temperatures_optimized(temperatures),
    )


if __name__ == "__main__":
    main()
