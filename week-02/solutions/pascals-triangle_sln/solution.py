def generate(num_rows: int) -> list[list[int]]:
    """
    Generate the first num_rows of Pascal's triangle.

    Args:
        num_rows: The number of rows to generate.

    Returns:
        A nested list containing Pascal's triangle.
    """
    result = []
    for i in range(num_rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = result[i - 1][j - 1] + result[i - 1][j]
        result.append(row)
    return result


def test_generate():
    assert generate(0) == []
    assert generate(1) == [[1]]
    assert generate(5) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
    ]


def main():
    num_rows = 5
    triangle = generate(num_rows)
    for row in triangle:
        print(row)


if __name__ == "__main__":
    main()
