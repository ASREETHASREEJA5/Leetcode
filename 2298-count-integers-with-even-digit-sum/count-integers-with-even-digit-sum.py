class Solution:
    def countEven(self, num: int) -> int:
        c = 0
        for i in range(2,num+1):
            s = str(i)
            a =0
            for j in s:
                a+=int(j)
            if a%2 ==0:
                c+=1
        return c
            


        