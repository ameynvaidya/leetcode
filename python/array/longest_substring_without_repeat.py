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
            max_count = max([i - start_index + 1, max_count])
        return max_count

class TestLengthOfLongestSubstring(unittest.TestCase):
    def test_run(self):
        test_cases = []
        test_cases.append(("abcabcabc",  3))
        test_cases.append(("",  0))
        test_cases.append(("aaaaaa",  1))
        test_cases.append(("pwwkew",  3))
        test_cases.append(("aaaaabcadefg",  7))
        for test_case in test_cases:
            input_string, expected_count = test_case
            with self.subTest(input_string):
                s = Solution()
                actual_ans = s.lengthOfLongestSubstring(input_string)
                self.assertEqual(actual_ans, expected_count)

if __name__ == '__main__':
    unittest.main(verbosity=2)