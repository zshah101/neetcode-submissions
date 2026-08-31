# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        prev = head
        while curr and curr.next:
            curr = curr.next.next
            prev = prev.next
        mid = prev.next
        prev.next = None

        void = None

        while mid:
            nxt = mid.next
            mid.next = void
            void = mid
            mid = nxt
        
        first = head
        second = void

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next
            
        

        

        
        

        


        
        