# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:

            prev = None
            curr = head

            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            return prev    
        
        def mergeList(list1: Optional[ListNode], list2: Optional[ListNode]) -> None:

            while list1 and list2:
                tmp1 = list1.next
                tmp2 = list2.next
                list1.next = list2
                list2.next = tmp1
                list1 = tmp1
                list2 = tmp2                

        ptr1 = ptr2 = head

        while ptr2 and ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        
        list2 = ptr1.next

        if not list2:
            return

        ptr1.next = None    

        list2 = reverseList(list2) # contains the starting of the second list
        
        mergeList(head, list2)

            

