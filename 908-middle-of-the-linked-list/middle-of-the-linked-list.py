# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp = head
        c = 0
        while temp:
            c+=1
            temp = temp.next
        mid = c//2

        temp = head
        for i in range(mid):
            temp = temp.next
        return temp
        
        

        