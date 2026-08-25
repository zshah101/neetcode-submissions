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
    # c          
    # A - A' - B - B' - C - C' - None
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next
        newhead = head.next
        
        curr = head
        while curr:
            copy = curr.next
            if curr.random:
                copy.random = curr.random.next
            curr = curr.next.next
        
        curr = head
        while curr:
            new = curr.next
            curr.next = new.next
            if new.next:
                new.next = new.next.next
            curr = curr.next
        return newhead
        
            
            
            
            
        
            
            



        


            
        