class Solution:
    def findPoisonedDuration(self, ti: List[int], du: int) -> int:
        if not ti:
            return 0
        t = 0
        for i in range(1,len(ti)):
            r = ti[i]-ti[i-1]
            t+=min(r,du)
        t+=du
        return t
        