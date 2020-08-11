#!/usr/bin/python3
from typing import List
import unittest

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for index, value  in enumerate(nums):
            complement = target - value
            if complement in table:
                return [index, table[complement]]
            else:
                table[value] = index
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
                self.assertEqual(actual_list.sort(), expected_list.sort())

if __name__ == '__main__':
    unittest.main(verbosity=2)