from test_framework import generic_test

"""
If we look at a small subproblem of this question, we can see that the water
trapped is L * W where L = length, and W = width. So, we can work inwards
and keep two pointers, we take min(left, right) which will give us the height,
so amount of water trapped will be H * W
"""
def get_max_trapped_water(heights):

    i, j, max_water = 0, len(heights) - 1, 0
    while i < j:
        width = j - i
        max_water = max(max_water, width * min(heights[i], heights[j]))
        if heights[i] > heights[j]:
            j -= 1
        else:  # heights[i] <= heights[j].
            i += 1
    return max_water


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "max_trapped_water.py", "max_trapped_water.tsv", get_max_trapped_water
        )
    )
