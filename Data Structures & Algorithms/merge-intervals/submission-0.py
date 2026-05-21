class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]

        for interval in intervals:
            if interval[0] > res[-1][1]:
                res.append(interval)
                continue
            
            res[-1][1] = max(res[-1][1], interval[1])
        
        return res
        