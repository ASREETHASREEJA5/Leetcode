class Solution:
    def canPlaceFlowers(self, fd: List[int], n: int) -> bool:
        c = 0
        i = 0
        while i<(len(fd)):
            if fd[i] == 0:
                e_f = (i == 0 or fd[i-1] == 0)
                e_r = (i == len(fd)-1 or fd[i+1] == 0)
                if e_f and e_r:
                    fd [i] = 1 
                    c+=1
                    if c>=n:
                        return True
                    i+=2
                    continue
            i+=1
        return c>=n
