"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        states = []
        for interval in intervals:
            states.append([interval.start, 1])
            states.append([interval.end, 0])
        
        states.sort()

        maxRooms = 0
        currRooms = 0

        for state in states:
            if state[1] == 1:
                currRooms += 1
                maxRooms = max(maxRooms, currRooms)
            else:
                currRooms -= 1
        
        return maxRooms


