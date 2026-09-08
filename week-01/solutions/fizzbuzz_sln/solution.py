from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    Generate the FizzBuzz sequence from 1 to n.

    Args:
        n: The upper limit (inclusive).

    Returns:
        A list of strings representing the FizzBuzz sequence.
    """
    answer: List[str] = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))

    return answer


def fizzbuzz_print(n: int) -> None:
    """
    Print the FizzBuzz sequence from 1 to n.

    Args:
        n: The upper limit (inclusive).
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def fizzbuzz_mapped(n: int) -> List[str]:
    """
    Generate the FizzBuzz sequence using a dictionary mapping.

    Args:
        n: The upper limit (inclusive).

    Returns:
        A list of strings representing the FizzBuzz sequence.
    """
    legend = {
        3: "Fizz",
        5: "Buzz",
        7: "Zazz",
    }

    answer: List[str] = []
    for i in range(1, n + 1):
        result = ""

        for divisor, word in legend.items():
            if i % divisor == 0:
                result += word

        if not result:
            result = str(i)

        answer.append(result)

    return answer


def main() -> None:
    """Run the FizzBuzz demonstrations."""
    n = int(input("Enter a number: "))

    result = fizzbuzz(n)

    for item in result:
        print(item)

    print("\nNow printing using fizzbuzz_print function:")
    fizzbuzz_print(n)

    print("\nNow printing using fizzbuzz_mapped function:")
    result_mapped = fizzbuzz_mapped(n)

    for item in result_mapped:
        print(item)


if __name__ == "__main__":
    main()
