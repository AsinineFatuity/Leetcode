from typing import List


class RecursiveSolution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for idx, cur_el in enumerate(nums):
            if idx != len(nums) - 1:
                next_idx = idx + 1
                if cur_el == nums[next_idx]:
                    del nums[next_idx]
                    return self.removeDuplicates(nums)
        return len(nums)


class NonRecursiveSolution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        to_insert_idx = 1  # initialize the index to insert the next unique element
        for i in range(
            1, len(nums)
        ):  # Loop through the list starting from the second element
            if nums[i] != nums[i - 1]:
                nums[to_insert_idx] = nums[i]
                to_insert_idx += 1
        return to_insert_idx


sln_classes = [RecursiveSolution, NonRecursiveSolution]
for cls in sln_classes:
    sln = cls()
    to_test_lists = [[1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]
    for i in to_test_lists:
        k = sln.removeDuplicates(i)
        print(f"{cls.__name__}, k: {k}")
