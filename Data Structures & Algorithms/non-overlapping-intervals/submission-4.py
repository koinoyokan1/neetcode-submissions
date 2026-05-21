'''
----  -----  ---
        ------
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        ans = 0
        lastEnd = intervals[0][1]
        for i in intervals[1:]:
            if i[0] >= lastEnd: 
                lastEnd = i[1]
                continue
            ans += 1
            lastEnd = min(lastEnd, i[1])
        
        return ans