import operator

from math import sqrt
from helpers import clockit


def largest_product_in_grid(c=4, grid=None):
    """
    P11. Finds the largest product of c adjacent numbers in a grid. Looks at all
    directions (across, down, diagonal-right, diagonal-left).
    """
    if not grid:
        grid = [[8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8],
                [49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0],
                [81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65],
                [52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91],
                [22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80],
                [24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50],
                [32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70],
                [67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21],
                [24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72],
                [21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95],
                [78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92],
                [16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57],
                [86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58],
                [19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40],
                [4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66],
                [88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69],
                [4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36],
                [20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16],
                [20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54],
                [1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48]]

    def make_diag(grid_, right=True):
        """Pads the grid rows with zeros to line up diagonals."""
        diag = []
        zeros = [0] * (len(grid) - 1)
        for y, row in enumerate(grid_):
            if right:
                # diagonals down and to the right
                adjusted_row = zeros[y:] + row + zeros[:y]
            else:
                # diagonals down and to the left
                adjusted_row = zeros[:y] + row + zeros[y:]
            diag.append(adjusted_row)
        # transpose rows and columns
        return [list(e) for e in zip(*diag)]

    def get_max_prod(grid_):
        max_prod = 0
        for y, row in enumerate(grid_):
            for o in xrange(0, len(row)):
                chunk = row[o:o+c]
                prod = reduce(operator.mul, chunk)
                if prod > max_prod:
                    max_prod = prod
        return max_prod

    across = grid
    down = [list(r) for r in zip(*grid)]
    rdiag = make_diag(grid, right=True)
    ldiag = make_diag(grid, right=False)

    return max(get_max_prod(across), get_max_prod(down), get_max_prod(rdiag),
               get_max_prod(ldiag))


def highly_divisible_triangular_number(divisors=500):
    """
    P12. Finds the value of the first triangle number to have over x divisors.

    A triangle number n is the sum of all digits preceding it 1-to-n.
    Like a factorial with sums instead of multiplication.
    """
    i, tn = 0, 0
    factors = set()
    while len(factors) <= divisors:
        i += 1
        tn += i
        factors.clear()
        for j in xrange(1, int(sqrt(tn)) + 1):
            if tn % j == 0:
                factors.add(j)
                factors.add(tn//j)
    else:
        return tn


if __name__ == '__main__':
    # print largest_product_in_grid(c=4)
    print highly_divisible_triangular_number(500)
    pass