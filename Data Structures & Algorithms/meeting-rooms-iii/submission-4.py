import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        # Available rooms by room number
        available = list(range(n))
        heapq.heapify(available)

        # Busy rooms: (end_time, room_number)
        busy = []

        count = [0] * n

        for start, end in meetings:
            duration = end - start

            # Free all rooms that have finished
            while busy and busy[0][0] <= start:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                # Assign smallest available room
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                # Delay meeting until earliest room becomes free
                free_time, room = heapq.heappop(busy)

                new_end = free_time + duration

                heapq.heappush(busy, (new_end, room))

            count[room] += 1

        answer = 0
        for room in range(1, n):
            if count[room] > count[answer]:
                answer = room

        return answer