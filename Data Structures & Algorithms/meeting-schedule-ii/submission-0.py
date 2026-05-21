"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    --------------
      ---
       -
         --------------
          
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        occupiedRooms = 0
        requiredRooms = 0

        roomOccupy = []
        for interval in intervals:
            roomOccupy.append((interval.start, True))
            roomOccupy.append((interval.end, False))

        roomOccupy.sort()

        for room in roomOccupy:
            if room[1]:
                occupiedRooms += 1
                requiredRooms = max(requiredRooms, occupiedRooms)
            else:
                occupiedRooms -= 1

        return requiredRooms
