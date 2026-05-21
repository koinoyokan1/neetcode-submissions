from collections import Counter
'''
if maxHeap: time + 1, q pop one
if not maxHeap and q: time + x

'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while maxHeap or q:
            if not maxHeap:
                cnt, time = q.popleft()
                heapq.heappush(maxHeap, cnt)
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append((cnt, time+n+1))
                if q and q[0][1] == time+1:
                        cnt, _ = q.popleft()
                        heapq.heappush(maxHeap, cnt)
                time += 1
        
        return time

