# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return
        s = []
        temp = head
        while temp:
            s.append(temp.val)
            temp = temp.next
        temp = head
        k = k%len(s)
        l = s[-k:]+s[:-k]
        l = l[::-1]
        while temp:
            temp.val = l.pop()
            temp = temp.next
        return head
            
        