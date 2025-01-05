class Solution:
    def isBalanced(self, num: str) -> bool:
        num = list(map(int,num))
        return sum(num[0:len(num):2]) == sum(num[1:len(num):2])
