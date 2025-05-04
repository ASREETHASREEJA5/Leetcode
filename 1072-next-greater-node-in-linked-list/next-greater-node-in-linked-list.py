# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        l = []
        ptr = head
        while ptr:
            temp = ptr.next
            while temp is not None and temp.val<=ptr.val:
                temp = temp.next
            if temp:
                l.append(temp.val)
            else:
                l.append(0)
            ptr = ptr.next
        return l

        