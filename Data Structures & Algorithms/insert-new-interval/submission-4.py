'''
--------     -------       -------
               ---------------
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        mn, mx = 0, 1

        for i in range(len(intervals)):
            interval = intervals[i]

            if newInterval[mn] > interval[mx]:
                ans.append(interval) 

            elif newInterval[mx] < interval[mn]:
                ans.append(newInterval)
                ans.extend(intervals[i:])
                return ans
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        ans.append(newInterval) 
        
        return ans
