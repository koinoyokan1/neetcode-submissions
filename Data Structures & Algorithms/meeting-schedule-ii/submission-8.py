"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# 1, 5, 10, 15
# 5, 10, 15, 20
# 
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        meetings = [(i.start, 2) for i in intervals]
        meetings.extend([(i.end, 1) for i in intervals])

        meetings.sort()
        mxRooms = 0
        currRooms = 0

        for t, typ in meetings:
            if typ == 2: 
                currRooms += 1
                mxRooms = max(mxRooms, currRooms)
            else:
                currRooms -= 1
        
        return mxRooms
