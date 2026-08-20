def dot_product(vec1: list[int], vec2: list[int]) -> int:
    return sum(i * j for (i, j) in zip(vec1, vec2, strict=False))


def is_matrix(m: list[list[int]]) -> bool:
    if len(m) == 0 or len(m[0]) == 0:
        return False
    return all(len(row) == len(m[0]) for row in m)


def matrix_product(m1: list[list[int]], m2: list[list[int]]) -> list[list[int]] | None:
    if (
        len(m1) == 0
        or len(m2) == 0
        or len(m1[0]) == 0
        or len(m2[0]) == 0
        or len(m1[0]) != len(m2)
    ):
        return None

    result = [[0] * len(m2[0]) for _ in range(len(m1))]
    for row in range(len(result)):
        for col in range(len(result[0])):
            m2_col = [m2_row[col] for m2_row in m2]
            m1_row = m1[row]
            result[row][col] = dot_product(m1_row, m2_col)

    return result


def matrix_product_improved(
    m1: list[list[int]], m2: list[list[int]]
) -> list[list[int]]:
    if not is_matrix(m1) or not is_matrix(m2):
        raise ValueError("Not matrix inputs")
    if len(m1[0]) != len(m2):
        raise ValueError("Incomptatible matrix dimensions")

    m2_t = list(zip(*m2, strict=False))

    return [
        [sum(a * b for a, b in zip(row, col, strict=False)) for col in m2_t]
        for row in m1
    ]


test_cases = [
    # 1. 1x1 * 1x1
    ([[5]], [[7]], [[35]]),
    # 2. 2x2 identity
    ([[1, 0], [0, 1]], [[3, 4], [5, 6]], [[3, 4], [5, 6]]),
    # 3. General 2x2
    ([[1, 2], [3, 4]], [[5, 6], [7, 8]], [[19, 22], [43, 50]]),
    # 4. 2x3 * 3x2
    ([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]], [[58, 64], [139, 154]]),
    # 5. 3x2 * 2x4
    (
        [[1, 2], [3, 4], [5, 6]],
        [[7, 8, 9, 10], [11, 12, 13, 14]],
        [[29, 32, 35, 38], [65, 72, 79, 86], [101, 112, 123, 134]],
    ),
    # 6. Zero matrix
    ([[0, 0], [0, 0]], [[1, 2], [3, 4]], [[0, 0], [0, 0]]),
    # 7. Negative numbers
    ([[1, -2], [-3, 4]], [[5, -6], [7, -8]], [[-9, 10], [13, -14]]),
    # 8. Rectangular with negatives
    ([[2, -1, 3]], [[4], [-2], [5]], [[25]]),
]

invalid_cases = [
    # 2x2 * 3x2
    ([[1, 2], [3, 4]], [[5, 6], [7, 8], [9, 10]]),
    # 1x3 * 2x2
    ([[1, 2, 3]], [[4, 5], [6, 7]]),
    # 3x1 * 2x2
    ([[1], [2], [3]], [[4, 5], [6, 7]]),
]
for A, B, expected in test_cases:
    print(matrix_product_improved(A, B))
    assert matrix_product_improved(A, B) == expected

for A, B in invalid_cases:
    assert matrix_product(A, B) is None
