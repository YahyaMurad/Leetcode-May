# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse_list(self, head):
        curr = head
        reverse = None

        while curr:
            next = curr.next
            curr.next = reverse
            reverse, curr = curr, next

        return reverse

    def doubleIt(self, head):
        reverse = self.reverse_list(head)
        
        dummy = reverse
        prev = None
        carry = 0

        while dummy:
            val = dummy.val * 2 + carry
            dummy.val = val % 10

            carry = 1 if val > 9 else 0
            prev = dummy
            dummy = dummy.next

        if carry:
            prev.next = ListNode(carry)

        result = self.reverse_list(reverse)

        return result
