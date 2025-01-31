import math
class Solution:
    def smallestDivisor(self, arr: List[int], threshold: int) -> int:
        n = len(arr)
        maxi = max(arr)
        i = 1
        j = maxi
        while(i<=j):
            mid = (i+j)//2
            c_sum = 0
            for k in range(n):
                c_sum+=math.ceil(arr[k]/mid)
            if c_sum<=threshold:
                j=mid-1
            else:
                i = mid+1
        return j+1


        