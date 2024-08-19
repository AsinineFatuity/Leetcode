"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        to_insert_idx = 1  # initialize the index to insert the next unique element
        num_repeats = 0
        for i in range(
            1, len(nums)
        ):  # Loop through the list starting from the second element
            if nums[i] != nums[i - 1]:
                nums[to_insert_idx] = nums[i]
                to_insert_idx += 1
                num_repeats = 0
            else:
                num_repeats += 1
                if num_repeats < 2:
                    nums[to_insert_idx] = nums[i]
                    to_insert_idx += 1
        return to_insert_idx


sln = Solution()
to_test_lists = [[1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [1, 1, 1, 2, 2, 3]]
for i in to_test_lists:
    k = sln.removeDuplicates(i)
    print(f"k: {k}")
    print(f"i: {i}")
