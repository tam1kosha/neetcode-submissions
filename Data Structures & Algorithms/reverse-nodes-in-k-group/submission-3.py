# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
        n = len(arr)
        for i in range(0, n - k + 1, k):
            for j in range(k // 2):
                arr[i + j], arr[i + k - j - 1] = arr[i + k - j - 1], arr[i + j]
        
        for i in range(0, n - 1):
            arr[i].next = arr[i + 1]
        arr[n - 1].next = None
        head = arr[0]
        return head
