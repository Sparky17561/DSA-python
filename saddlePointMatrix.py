def saddle_points(matrix):
    """
    Returns a list of tuples (i, j, value) for each saddle point in `matrix`,
    where matrix[i][j] is the minimum in row i and maximum in column j.
    """
    points = []
    n_rows = len(matrix)
    if n_rows == 0:
        return points
    n_cols = len(matrix[0])

    for i, row in enumerate(matrix):
        # 1) find the minimum value in the row
        min_val = min(row)

        # there may be multiple minima in the row
        for j, val in enumerate(row):
            if val != min_val:
                continue

            # 2) extract column j
            col = [matrix[r][j] for r in range(n_rows)]

            # 3) check if this val is the maximum in its column
            if val == max(col):
                points.append((i, j, val))

    return points


if __name__ == "__main__":
    # Example usage:
    mat = [
        [ 0, -2,  3,  2],
        [ 4,  3,  1,  5],
        [ 6,  4,  2,  0],
        [ 7,  8,  9,  3]
    ]
    saddles = saddle_points(mat)
    if saddles:
        for i, j, v in saddles:
            print(f"Saddle point at row {i}, col {j} → value {v}")
    else:
        print("No saddle points found.")
