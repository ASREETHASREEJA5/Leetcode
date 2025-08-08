# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        temp = head
        c = 0
        while temp:
            c+=1
            temp = temp.next
        batch_size,extra = divmod(c,k)
        curr = head
        p = []
        for _ in range(k):
            dummy = ListNode()
            tail = dummy
            size = batch_size+(1 if extra>0 else 0)

            for _ in range(size):
                tail.next = curr
                curr = curr.next
                tail = tail.next
            if tail:
                tail.next = None
            p.append(dummy.next)
            if extra>0:
                extra-=1
        return p
            
        