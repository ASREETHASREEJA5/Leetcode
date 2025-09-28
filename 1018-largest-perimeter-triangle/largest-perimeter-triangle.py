class Solution:
    def largestPerimeter(self, eve: List[int]) -> int:
        eve.sort(reverse=True)
        for i in range(len(eve)-2):
            if eve[i+1]+eve[i+2] > eve[i]:
                return eve[i]+eve[i+1]+eve[i+2]
        return 0
        