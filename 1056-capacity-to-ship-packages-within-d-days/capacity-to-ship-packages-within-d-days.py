class Solution:
    def shipWithinDays(self, w: List[int], d: int) -> int:
        def is_pos(n):
            d = 1
            load = 0
            for i in range(len(w)):
                if load+w[i]>n:
                    d+=1
                    load = w[i]
                else:
                    load += w[i]
            return d

        l,r = max(w),sum(w)
        while l<r:
            mid = (r+l)//2
            ans = is_pos(mid)
            if ans<=d:
                r = mid
            else:
                l = mid+1
        return l