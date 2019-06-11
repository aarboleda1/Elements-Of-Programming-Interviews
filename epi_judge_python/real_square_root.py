from test_framework import generic_test
import math
"""11.5 Square root computations can be implemented using sophisticated numerical
tehniques involving iterative methods and logarithms. However, if you were
asked to implement a square root function, you would not be expected to know
these techniques.

Implement a function which takes as input a floating point value and returns
its square root.

Hint: Iteratively compute a sequence of intervals, each contained in the previous
interval, that contain the result.

[ ATTEMPTED ] 6/
"""

def square_root(x):
    if not x:
        return 0

    lo, hi = 1, x
    sqrt = 0.0
    while not math.isclose(lo, hi):
        print(lo, hi)
        sqrt = (lo + hi) / 2
        product = sqrt * sqrt
        # print(sqrt)

        if product > x:
            hi = sqrt
        else:
            lo = sqrt
    return lo


if __name__ == '__main__':
    # print(square_root(2.0))
    # print(square_root(10.1))
    # print(square_root(1.0))
    print(square_root(8.1))
    # exit(
        # generic_test.generic_test_main("real_square_root.py",
                                       # 'real_square_root.tsv', square_root))
