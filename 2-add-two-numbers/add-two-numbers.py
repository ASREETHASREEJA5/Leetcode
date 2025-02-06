# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        s2 = ""
        temp1 = l1
        temp2 = l2
        while temp1:
            s1+=str(temp1.val)
            temp1 = temp1.next
        while temp2:
            s2+=str(temp2.val)
            temp2 = temp2.next
        ans = str(int(s1[::-1])+int(s2[::-1]))
        ans = ans[::-1]
        newhead = ListNode(int(ans[0]))
        temp = newhead
        for i in range(1,len(ans)):
            temp.next = ListNode(int(ans[i]))
            temp = temp.next
        return newhead

        
