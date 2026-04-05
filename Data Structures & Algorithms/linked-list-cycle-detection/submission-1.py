# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Okay for this, I only know a solution which can be of
        # O (n^2) time complexity in the worst case
        pointer1 = pointer2 = head #This is the slow pointer
        
        # If pointer2 does not exit, then it means that the linkedlist is still going on, slow and fast pointer may meet at some point
        while pointer2 and pointer2.next:

            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
            
            if (pointer1 == pointer2):
                return True

        # If pointer2 exits, then it means there is no cycle: return false 
        return False     

