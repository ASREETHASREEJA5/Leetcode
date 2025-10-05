class Solution:
    def combinationSum(self, c: List[int], t: int) -> List[List[int]]:
        ans = []
        ds = []
        def comb(ind,t):
            if ind == len(c):
                if t==0:
                    ans.append(ds[:])
                return 
            if c[ind]<=t:
                ds.append(c[ind])
                comb(ind,t-c[ind])
                ds.pop()
            comb(ind+1,t)
        comb(0,t)
        return ans 
        