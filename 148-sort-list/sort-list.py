# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        stack = []
        while temp is not None:
            stack.append(temp.val)
            temp = temp.next
        stack.sort()
        stack = stack[::-1]
        temp = head
        while temp is not None:
            temp.val = stack.pop()
            temp = temp.next
        return head
        