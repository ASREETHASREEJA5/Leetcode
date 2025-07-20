class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time_req(pi,s):
            t = 0
            for i in range(len(pi)):
                t+=math.ceil(pi[i]/s)
            return t
        l,r = 1,max(piles)
        while l<r:
            mid = (l+r)//2
            ans = time_req(piles,mid)
            if ans<=h:
                r=mid
            else:
                l = mid+1
        return l
        