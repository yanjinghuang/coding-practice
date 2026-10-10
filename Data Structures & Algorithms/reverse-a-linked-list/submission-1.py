# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None 

        while curr:
            temp = curr.next  # store current next 
            curr.next = prev # flip
            prev = curr  # advance - update prev
            curr = temp # advance - update cur
        
        return prev 
        


        