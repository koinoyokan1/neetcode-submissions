import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ans = []

        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))

        for curr in range(k-1, len(nums)):
            heapq.heappush(heap, (-nums[curr], curr))

            while heap:
                val, i = heap[0]
                if curr - i >= k: 
                    heapq.heappop(heap)
                else:
                    break
            ans.append(-val) 
        
        return ans