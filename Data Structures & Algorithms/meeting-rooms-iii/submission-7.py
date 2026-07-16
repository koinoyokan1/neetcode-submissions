import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        free = [i for i in range(n)]
        heapq.heapify(free)
        meetings.sort()
        busy = []
        roomUseCnt = defaultdict(int)

        for m in meetings:
            start, end = m[0], m[1]

            while busy and busy[0][0] <= start:
                lastEnd, roomNo = heapq.heappop(busy)
                heapq.heappush(free, roomNo)
            
            if not free:
                lastEnd, roomNo = heapq.heappop(busy)
                end = lastEnd + end - start
            else:
                roomNo = heapq.heappop(free)
            roomUseCnt[roomNo] += 1
            heapq.heappush(busy, (end, roomNo))
        
        roomUse = [(-roomUseCnt[key], key) for key in roomUseCnt.keys()]
        roomUse.sort()
        return roomUse[0][1]


