class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_d = float('inf')
        l = []
        
        for i in range(len(arr)-1):
            min_d = min(min_d,arr[i+1]-arr[i])
        for i in range(0,len(arr)-1):
            if abs(arr[i]-arr[i+1]) == min_d:
                l.append([arr[i],arr[i+1]])
        return l
        