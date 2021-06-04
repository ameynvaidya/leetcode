#!/usr/bin/python3
from typing import List
import unittest

'''
https://leetcode.com/problems/two-sum/
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for index, value in enumerate(nums):
            delta = target - value
            if delta in nums_map:
                return [nums_map[delta], index]
            else:
                nums_map[value] = index
        return []

class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        test_cases = []
        test_cases.append(([2, 7, 11, 15], 9, [0, 1]))
        test_cases.append(([2, 7, 11, 15], 18, [1, 2]))
        test_cases.append(([3, 2, 4], 6, [1, 2]))
        for test_case in test_cases:
            nums, target, expected_list = test_case
            with self.subTest(nums):
                s = Solution()
                actual_list = s.twoSum(nums, target)
                self.assertEqual(actual_list, expected_list)

if __name__ == '__main__':
    unittest.main(verbosity=2)