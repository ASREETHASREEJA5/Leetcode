# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        max_val = float('-inf')
        current = prev  
        dummy = ListNode(0)
        tail = dummy
        
        while current:
            if current.val >= max_val:
                max_val = current.val
                tail.next = current
                tail = current
            current = current.next
        
        tail.next = None  
        
        prev = None
        current = dummy.next
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev



        