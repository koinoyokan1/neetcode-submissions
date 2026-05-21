'''
     -----
---         ----
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        for j in range(len(intervals)):
            i = intervals[j]
            if i[1] < newInterval[0]: 
                ans.append(i)
                continue

            if i[0] > newInterval[1]:
                ans.append(newInterval)
                ans.extend(intervals[j:])
                return ans

            newInterval[0] = min(newInterval[0], i[0])                 
            newInterval[1] = max(newInterval[1], i[1])                 

        ans.append(newInterval)

        return ans
          