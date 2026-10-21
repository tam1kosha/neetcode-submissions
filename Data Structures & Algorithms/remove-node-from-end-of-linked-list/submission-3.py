# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None

        prev, left, right = head, head, head

        while right and n > 0:
            right = right.next 
            n -= 1 

        if right == None:
            return left.next

        while right:
            prev = left
            left = left.next
            right = right.next
        
        prev.next = left.next

        return head