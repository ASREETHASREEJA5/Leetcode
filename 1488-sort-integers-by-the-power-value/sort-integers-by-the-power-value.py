class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        l = {}
        for i in range(lo,hi+1):
            c = 0
            n = i
            while n != 1:
                if n%2 == 0:
                    n = n//2
                else:
                    n = 3*n+1
                c+=1
            l[i] = c
        sorted_items = sorted(l.items(), key=lambda x: (x[1], x[0]))
        return sorted_items[k - 1][0]
            
