from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for idx, cur_el in enumerate(nums):
            if idx != len(nums) - 1:
                next_idx = idx + 1
                if cur_el == nums[next_idx]:
                    del nums[next_idx]
                    return self.removeDuplicates(nums)
        return len(nums)


sln = Solution()
to_test_lists = [[1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]
for i in to_test_lists:
    k = sln.removeDuplicates(i)
    print(f"k: {k}")
