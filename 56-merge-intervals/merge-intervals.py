class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i=0
        intervals.sort()
        while(i<len(intervals)-1):
            if intervals[i+1][0] >= intervals[i][0]:
                if intervals[i+1][0]<=intervals[i][1]:
                    if intervals[i+1][1]>=intervals[i][1]:
                        intervals[i][1]=intervals[i+1][1]
                    intervals.remove(intervals[i+1])
                else:
                    i=i+1
        return intervals