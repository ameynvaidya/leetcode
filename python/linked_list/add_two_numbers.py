from single_linked_list import ListNode
import unittest

'''
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_start = ListNode()
        result = result_start
        while l1 is not None or l2 is not None:
            l1_val = 0 if l1 is None else l1.val
            l2_val = 0 if l2 is None else l2.val
            sum = (result.val + l1_val + l2_val)
            result.val = sum % 10
            carry = (sum // 10)
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            if l1 is not None or l2 is not None or carry > 0:
                result.next = ListNode(carry)
                result = result.next
        return result_start

class TestAddTwoNumbers(unittest.TestCase):
    def test_two_sum(self):
        test_cases = []
        test_cases.append((
            ListNode(2, ListNode(4, ListNode(3))), 
            ListNode(5, ListNode(6, ListNode(4))), 
            ListNode(7, ListNode(0, ListNode(8)))
        ))
        test_cases.append((
            ListNode(2, ListNode(4, ListNode(3))), 
            ListNode(val=0), 
            ListNode(2, ListNode(4, ListNode(3))), 
        ))
        test_cases.append((
            ListNode(val=0), 
            ListNode(2, ListNode(4, ListNode(3))), 
            ListNode(2, ListNode(4, ListNode(3))), 
        ))
        test_cases.append((
            ListNode(val=0),
            ListNode(val=0),
            ListNode(val=0),
        ))
        for test_case in test_cases:
            l1, l2, expected_ans = test_case
            with self.subTest(l1.printString() + " " + l2.printString()):
                s = Solution()
                actual_ans = s.addTwoNumbers(l1, l2)
                self.assertEqual(expected_ans.printString(), actual_ans.printString())

if __name__ == '__main__':
    unittest.main(verbosity=2)

