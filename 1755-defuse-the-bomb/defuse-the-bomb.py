class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        l = [0]*n
        if k == 0:
            return l
        for i in range(n):
            if k>0:
                l[i] = sum(code[(i+j)%n] for j in range(1,k+1))
            else:
                l[i] = sum(code[(i+j)%n] for j in range(k,0))
        return l

        