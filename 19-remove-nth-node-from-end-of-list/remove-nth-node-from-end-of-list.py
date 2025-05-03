# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        c = 0
        while ptr:
            c+=1
            ptr = ptr.next
        if c ==1 and n==1:
            return
        if c ==n :
            return head.next
         
        m = (c-n)
        ptr = head
        prev = None
        for i in range(m):
            prev = ptr
            ptr = ptr.next
        print(ptr.val)
        prev.next = ptr.next
        ptr = None
        return head



        
        

        
        

        