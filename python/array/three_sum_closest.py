#!/usr/bin/python3
from typing import List

'''
https://leetcode.com/problems/3sum-closest/
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

Example:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
class Solution:

    def twoSumClosest(self, nums: List[int], i: int, target: int) -> int:
        l = i
        r = len(nums) - 1
        result = nums[l] + nums[r] # 1
        while (l < r):
            if (abs(target - nums[l] - nums[r]) < abs(target - result)):
                result = nums[l] + nums[r]
            if(nums[l] + nums[r] == target):
                return target
            elif(nums[l] + nums[r] < target):
                l = l + 1
            else:
                r = r - 1
        return result
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            closest_sum = nums[i] + self.twoSumClosest(nums, i + 1, target - nums[i])
            if (abs(target - closest_sum) < abs(target - result)):
                result = closest_sum
        return result

s=  Solution()
nums = [-1,2,1,-4]
target = 1
print(s.threeSumClosest(nums, target))