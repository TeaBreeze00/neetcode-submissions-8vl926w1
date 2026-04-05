# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # This is the plan, I'll iterate over the list and get the length
        # of the list, then I'll subtract the given thing from the list, which will
        # give me the node number immediately preceeding the list. Then it's about removing the right
        # element

        count = 0
        curr = head

        while curr:
            count+=1
            curr = curr.next

        idx = count - n
        
        if idx == 0:
            head = head.next
            return head
            
        curr = head
        count = 0

        for i in range(idx - 1):
            count+=1
            curr = curr.next


        tmp = curr.next
        curr.next = tmp.next

        return head    
            