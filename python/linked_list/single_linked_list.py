from typing import List

class ListNode:
    def __init__(self, val=0, next=None, init_list=None):
        self.val = val
        self.next = next

    def printString(self) -> str:
        if self.next is not None:
            return str(self.val) + " -> " + self.next.printString()
        else:
            return str(self.val)
