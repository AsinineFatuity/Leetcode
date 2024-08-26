"""
https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1
        return candidate


"""
NOTES ON BOYER-MOYER VOTING ALGORITHM
The Boyer-Moore Voting Algorithm is designed to be efficient in both time and space. It keeps track of just one candidate and adjusts its count as it iterates through the list.
It doesn't need to store counts for every element because it relies on the majority element's property of appearing more than half the time to ensure that the correct candidate is identified by the end of the iteration.
"""


class InefficientSolution:
    def majorityElement(self, nums: List[int]) -> int:
        num_count_dict = {}
        for num in nums:
            if num in num_count_dict:
                count = num_count_dict[num]
                num_count_dict[num] = count + 1
            else:
                num_count_dict[num] = 1
        max_count = max(num_count_dict.values())
        for k, v in num_count_dict.items():
            if v == max_count:
                return k


"""
Boyer-Moyer is more preferred since it's efficient when we assume a majority element has to exist and that it appears more than n/2 times
Also should equal count exist, it is undefined. The space complexity is 0(1) and time is 0(n)

My inefficient solution is desired where we don't care about distribution and have to return at least an element as majority.
It's space complexity is 0(n) since we create new dictionary and time is 0(n)
"""
