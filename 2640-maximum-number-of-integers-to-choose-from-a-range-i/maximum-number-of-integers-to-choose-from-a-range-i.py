class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        c = 0
        t_sum = 0
        for i in range(1,n+1):
            if i not in banned:
                t_sum +=i
                if t_sum>maxSum:
                    break
                c+=1
        return c

