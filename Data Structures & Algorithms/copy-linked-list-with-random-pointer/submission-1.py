"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: 
            return None
        real = head
        hmp = {}
        while real:
            copy = Node(real.val, None, None)
            hmp[real] = copy
            real = real.next
        
        real = head
        while real:
            if real.next:
                hmp[real].next = hmp[real.next]
            if real.random:
                hmp[real].random = hmp[real.random]                 
            real = real.next
        
        randomhead = hmp[head]
        return randomhead