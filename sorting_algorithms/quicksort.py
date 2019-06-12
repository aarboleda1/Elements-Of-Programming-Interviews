"""Quicksort
Notes:

3 major steps of quicksort:
1) Pick a pivot by choosing an element (can be a random el, last el, first el),
then sandwich the pivot between items less than it, and items greater than it.
After finding it's final resting place, return this index to the caller
2) Partition the array by the pivot index from step 1, and recurse



2 major ideas of quick sort
Terminology:
    Pivot: The value within the partitioning space that I
        want to find a value for
    Partition subroutine:
        In the partition method, the job is to find the proper index
        of the pivot value, such that all elements to the left are
        less than pivot and all elements greater than that element
        are to the right
        pivot = 4
        A = [3, 2, 9, 8, 4]
# pseudocode
def quicksort(A, l, r):
    if l < r:
        pivot = partition(A, l, r)
        quicksort(A, l, pivot - 1)
        quicksort(A, pivot + 1, r)
"""

def quicksort(A) -> None:
    _quicksort(A, 0, len(A) - 1)

def _quicksort(A, left, right) -> None:
    """Recursive function that splits data based after placing a given pivot value
    in its correct place, and then operates on subarrays
    """
    if left < right:
        # Partition array from left to right and find out where the selected
        # pivot belongs
        p = partition(A, left, right)

        # Call quicksort with items to the left of the pivot, and to the right
        # of the pivot
        _quicksort(A, left, p - 1)
        _quicksort(A, p + 1, right)

def partition(A, left, right) -> int:
    """Partition method that chooses a pivot, partitions array
    around that pivot, places pivot value where it belongs,
    and returns the index of the pivot where it finally lies
    """
    # In this implementation, we pick the last item in the partition space
    pivot = A[right]

    # Keep track of the "tail" section of items less than the pivot, so that
    # at the end, we can "sandwich" the pivot between the section less than it
    # and the section greater than it
    i = left - 1
    for j in range(left, right):
        n = A[j]
        if n <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    # Swap pivot value right after section of items less than the pivot, i keeps
    # the tail of this section
    A[i + 1], A[right] = A[right], A[i + 1]
    return i + 1

if __name__ == "__main__":
    A = [3, 2, 1]
    quicksort(A)
    assert A == [1, 2, 3]
    A = [5, 1, 2, 3]
    quicksort(A)
    assert A == [1, 2, 3, 5]
