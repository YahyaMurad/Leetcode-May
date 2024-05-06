# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head):
        dummy = head
        stack = []

        while dummy:
            while stack and stack[-1].val < dummy.val:
                stack.pop()
            stack.append(dummy)
            dummy = dummy.next
        
        next = None
        while stack:
            dummy = stack.pop()
            dummy.next = next
            next = dummy

        return dummy