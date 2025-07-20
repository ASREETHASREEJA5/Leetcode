class Solution:
    def minDays(self, blo: List[int], m: int, k: int) -> int:
        if len(blo) < (m*k):
            return -1
        
        def is_pos(n):
            c = 0
            b = 0
            for i in range(len(blo)):
                if blo[i]<=n:
                    c+=1
                else:
                    b+=c//k
                    c = 0
            b+=c//k
            return b>=m

        l,r = min(blo),max(blo)
        while l<r:
            mid = (l+r)//2
            if is_pos(mid):
                r = mid
            else:
                l = mid+1
        return l

        