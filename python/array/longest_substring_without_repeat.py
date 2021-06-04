import unittest

'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        word_map = {}
        max_count = 0
        start_index = 0
        for i,c in enumerate(s):
            if c in word_map and word_map[c] >= start_index:
               start_index = word_map[c] + 1
            word_map[c] = i
            max_count = max(max_count, i - start_index + 1)
        return max_count

s = Solution()
inp = "abba"
print(s.lengthOfLongestSubstring(inp))
