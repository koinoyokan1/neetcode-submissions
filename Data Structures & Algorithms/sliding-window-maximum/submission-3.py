class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(k-1): heapq.heappush(heap, (-nums[i], -i))
        
        ans = []
        for right in range(k-1, len(nums)):        
            heapq.heappush(heap, (-nums[right], -right))

            while -heap[0][1] <= right - k: 
                heapq.heappop(heap)
            ans.append(-heap[0][0])

        return ans