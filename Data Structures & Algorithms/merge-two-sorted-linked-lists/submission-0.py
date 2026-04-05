# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # This is the plan: I will follow a 3 pointer approach, I will initialize a 
        # null node with current, then I will initialize pointer 1 for list 1 and 
        # pointer 2 for list 2. Then I will traverse the 2 lists until they're empty, then
        # just attach the remaining list to the end of the merged list

        curr = ListNode()
        head = curr
        
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next        
            curr = curr.next

        # After the operation, just attach the rest of the list whichever is not null
        curr.next = list1 or list2

        return head.next
