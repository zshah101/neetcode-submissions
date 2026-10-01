# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = []
        curr = head
        while curr:
            node.append(curr)
            curr = curr.next

        removeIndex = len(node) - n
        if removeIndex == 0:
            return head.next
        
        node[removeIndex - 1].next = node[removeIndex].next
        return head 



    
        
        
        