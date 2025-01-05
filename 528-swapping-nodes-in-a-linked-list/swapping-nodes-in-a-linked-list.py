# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        a = k
        while a>1:
            temp = temp.next
            a-=1
        ptr = head
        c = 0
        while ptr:
            ptr = ptr.next
            c+=1
        b = c-k+1
        ptr = head
        while b>1:
            ptr = ptr.next
            b-=1
        value = temp.val
        temp.val = ptr.val
        ptr.val = value
        return head
            

        