"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        meetings = [(st.start, 'start') for st in intervals]
        meetings.extend([(st.end, 'end') for st in intervals])
        meetings.sort()

        mxRooms = 0
        cnt = 0

        for m in meetings:
            if m[1] == 'start': 
                cnt += 1
                mxRooms = max(mxRooms, cnt)
            else: 
                cnt -= 1
        
        return mxRooms






