import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = list(range(n))
        heapq.heapify(available)

        busy = []
        count = [0] * n

        for start, end in meetings:
            duration = end - start

            while busy and busy[0][0] <= start:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                free_time, room = heapq.heappop(busy)
                new_end = free_time + duration
                heapq.heappush(busy, (new_end, room))

            count[room] += 1

        answer = 0
        for room in range(n):
            if count[room] > count[answer]:
                answer = room

        return answer