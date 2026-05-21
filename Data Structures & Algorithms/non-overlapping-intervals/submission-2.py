'''
-------         --------       -----------------           
                                ----  ---  ---  ----
       
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        cnt = 0
        last = intervals[0]

        for interval in intervals[1:]:
            if last[1] <= interval[0]:
                last = interval
                continue
            cnt += 1
            last[1] = min(last[1], interval[1])
        
        return cnt
