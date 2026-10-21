# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        curr = head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        curr = head
        target = count - n
        if target == 0:
            head = head.next
            return head
        prev = None
        while target > 0 and curr:
            target -= 1
            prev = curr
            curr = curr.next
        print(prev.val)
        print(curr.val)
        prev.next = curr.next
        return head
