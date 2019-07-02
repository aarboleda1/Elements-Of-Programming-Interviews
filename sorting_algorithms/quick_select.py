from heapq import heapify, heappushpop
import random
"""
Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

Leetcode: https://leetcode.com/problems/kth-largest-element-in-an-array/
Back to Back SWE: https://www.youtube.com/watch?v=hGK_5n81drs&t=616s
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Keep track of the 'left' and 'right' space in which the
        # k'th largest element can possibly be, we will use these bounds
        # to know what section to actually partition around a choosen pivot
        n = len(nums)
        left, right = 0, n - 1
        target_index = n - k


        # While the bounds stay valid continue doing directed partitioning
        while left <= right:
            # Pick a random pivot, bounds are left and right
            random_index = random.randint(left, right)
            idx_from_partition = self.partition(nums, left, right, random_index)
            if idx_from_partition == target_index:
                return nums[idx_from_partition]
            elif idx_from_partition > target_index:
                # k'th largest must be in the left partition. We "overshot" and need to go left
                # (and we do this by narrowing the right bound)
                right = idx_from_partition - 1
            else:
                # finalIndexOfChoosenPivot < n - k
                # k'th largest must be in the right partition. We "undershot" and need to go right
                # (and we do this by narrowing the left bound)
                left = idx_from_partition + 1
        return -1

    def partition(self, nums, left, right, idx):
        # Grab the value at the pivot index we passed in
        pivot_value = nums[idx]
        # Remember how partitioning works? We need to keep track of where
        # we last placed an item in the section of items "less than the
        # pivot

        # We keep track of the tail index of this section. We will
        # need this later
        lesser_item_tail_idx = left

        # Move the item at the 'pivotIndex' OUT OF THE WAY. We are about to
        # bulldoze through the partitioning space and we don't want it in
        # the way
        nums[idx], nums[right] = nums[right], nums[idx]
        # Iterate from the left bound to 1 index right before the right bound
        # (where the choosen pivot value is now sitting in saftey)
        for i in range(left, right):

            # If this item is less than the 'pivotValue' then we need to move
            # this item to the section of items "less than the pivot"
            # 'lesserItemsTailIndex' keeps track of where we need to swap into
            # next...after doing the swap we advance it...you see how this is
            # coming together?
            if nums[i] < pivot_value:
                nums[i], nums[lesser_item_tail_idx] = nums[lesser_item_tail_idx], nums[i]
                lesser_item_tail_idx += 1
        # Ok...partitioning is done. Swap the pivot item BACK into the space we just
        # partitioned at the 'lesserItemsTailIndex'...that's where the pivot item
        # belongs
        # In the middle of the "sandwich".
        nums[right], nums[lesser_item_tail_idx] = nums[lesser_item_tail_idx], nums[right]

        # Return the index of where we just put the pivot so that the caller knows its
        # final resting place (so that the caller can make the decisions it needs)
        return lesser_item_tail_idx
